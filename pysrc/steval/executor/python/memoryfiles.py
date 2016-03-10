#! /usr/bin/env python3
"""
Keep files in memory without using the filesystem
"""

class VirtualFileManager(object):
	def __init__(self, individual_max_size=100000, global_max_size=1000000):
		self.individual_max_size = individual_max_size # individual maximal size of a file
		self.global_max_size = global_max_size
		self.supplied_files = {}
		self.created_files = {}
		self.size = 0
	def _get_stream(self, binary=True):
		return io.BytesIO if binary else io.StringIO
	def preload_directory_files(self, directory, condition=lambda x: True):
		"""Preload all the files from a directory"""
		for (dirpath, filedirs, filenames) in os.walk(directory):
			for filename in filenames:
				filepath = os.path.join(dirpath, filename)
				if condition(filepath):
					self.preload_file(filepath, binary=True)
	def preload_file(self, filepath, mode):
		with open(filepath, "r" + ("b" if binary else "")) as f:
			content = f.read(self.individual_max_size)
			if len(f.read(1)) > 0:
				raise IOError("Local overquota for file {}".format(filepath))
			if len(content) + size > self.global_max_size:
				raise IOError("Global overquota error: reached {} bytes".format(self.global_max_size))
			self.supplied_files[filepath] = self._get_stream(content)
	def open(self, filepath, mode, *kargs, **kwargs):
		"""Open the file"""
		class IOWrapper(object):
			def __init__(self, underlying, read_only=True):
				self._underlying = underlying
				self.read_only = read_only
			def close(self):
				pass  # do nothing on close to allow future uses of the stream
			def write(self, content):
				if self.read_only:
					raise IOError("Write cannot be used in read-only mode")
				return self._underlying.write(content)
			def __getattr__(self, key):
				return getattr(self._underlying)
		stream = self._get_stream("b" in mode)
		if "w" in mode:
			if filepath in self.supplied_files:
				raise IOError("Cannot overwrite supplied file {}".format(filepath))
			else:
				self.created_files[filepath] = stream()
				return IOWrapper(self.created_files[filepath], False)
		elif "a" in mode:
			if filepath in self.supplied_files:
				raise IOError("Cannot overwrite supplied file {}".format(filepath))
			else:
				if filepath not in self.created_files:
					self.created_files[filepath] = stream()
				self.created_files[filepath].seek(0, 2)
				return IOWrapper(self.created_files[filepath], False)
		else:
			read_only = "+" not in mode
			if filepath in self.supplied_files:
				if read_only:
					return IOWrapper(self.supplied_files[filepath], True)
				else:
					raise IOError("Cannot modify a supplied file")
			else:
				if filepath not in self.created_files:
					self.created_files[filepath] = stream()
				return IOWrapper(self.created_files[filepath], False)
