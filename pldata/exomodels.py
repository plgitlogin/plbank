
class Try(models.Model):
	"""
	Information d'un essai d'un étudiant
	"""
	state  = #  try/starting/success 
	serverId = RELATION
	studentCode = models.TextField("studentcode")
	studentId = RELATION/IDENTIFIANT




class Exercice(models.Model):
	"""
	structure de stockage des exercices
	les champs de type FileField sont des fichiers
	ils sont stocké dans une model plfiles qui permet d'éviter d'avoir trop
	de fichiers identiques stoké a des endrois différents.
	"""

	exercise:raw = models.TextField("raw")
	exercise:author = models.CharField("author",max_length=50)
	exercise:code = models.TextField("enonce")
	exercise:concept = models.CharField("concept",max_length=100) # devrai être une relation ManyToManyField ou OneToMany comme la relation inverse ne nous intéresse pas 
	exercise:expectedoutput = models.CharField("author",max_length=200)
	exercise:feedback = models.TextField("enonce")
	exercise:feedbackfalse
	exercise:files
	exercise:grader = models.TextField("grader") 
	exercise:help 
	exercise:input = models.TextField("grader") 
	exercise:inputgenerator = models.TextField("grader") 
	exercise:name = models.CharField("name",max_length=200)
	exercise:pl_path = models.CharField("name",max_length=1000)
	exercise:pltest = models.TextField("pltest") 
	exercise:repository = models.ManyToManyField("repository")
	exercise:soluce = models.TextField("soluce") 
	exercise:taboo = models.CharField("taboo",max_length=200)
	exercise:tag = models.ManyToManyField("repository")
	exercise:testcode  = models.TextField("testcode") 
	exercise:text  = models.TextField("text") 
	exercise:title = models.CharField("title",max_length=200)

class Repository(models.Model):
	repository:name = models.CharField("name",max_length=200)
	repository:url = models.CharField("url",max_length=200) # un type specifique serai bien vue
	repository:login = models.CharField("login",max_length=100)
	repository:password = models.CharField("password",max_length=200)

class Tag(models.Model):
	tag:name
	tag:longname
	tag:description
	tag:url

class Grade(models.Model):
	gradeData
	gradeData:grade:value = models.IntegerField('niveau', default=-1)
	gradeData:grade:error
	gradeData:grade:errormessage
	gradeData:grade:errormessages
	gradeData:grade:execution
	gradeData:grade:execution:stderr
	gradeData:grade:execution:stdout
	gradeData:grade:feedback
	gradeData:grade:other
	gradeData:grade:plateforme
	gradeData:grade:result 
	gradeData:grade:stderr
	gradeData:grade:stdout
	gradeData:grade:success
	gradeData:platform_error


