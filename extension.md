
# Extension du langage

## fichiers pl
simplevalue=value # saisie d'une valeur comme réponse à la question
				# à la place de l'editeur de code un formulaire 

nbtry=3 # Nombre d'essai autorisés de la question
		# par exemple pour un qcm un seul essai





## fichier pltp

direct=True|False # le success est indiqué ou pas 

mode=default|maze|bot|random| ???  # les modes 
	les modes permettent de spécifier comment les questions contenues dans un fichier pltp sont utilisés par l'apprenant.


# les grains

## fichier **.plmd

Les fichiers **.plmd contiennent des grains de connaissance au format markdown

les fichiers **.plmd sont stockés dans la partie static du site (ou dans une partie de ce type si c'est du moodle,dans du mahara par exemple).


# Navigation du GIT 

## Filtre de navigation des exercices

Il faut pouvoir naviger dans le git.

git ls-files --full-name

après on filtre sur le nom ou le contenu.

filtres de base:
	.pl ou .pltp 
filtre sur le contenu :
	author=value # author contient value 
	tag=value  # un des tag est value
	clog=value # un des clog est value
	text=value # le text contient value (in)

n'importe quel élement peut être utilisé pour filtrer
si l'élément n'éxiste pas le test est négatif le fichier n'est pas sélectionné.

 
