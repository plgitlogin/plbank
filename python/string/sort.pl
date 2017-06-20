# not working

title=Tri récursif
author=chilowi
taboo=["sort","sorted"]
template=/python/0PLG/template.pl
text==
Écrivez une fonction nommée //tidy// qui trie une liste d'éléments par n'importe quel moyen.

Attention, vous n'avez pas le droit d'utiliser la méthode sort ou la fonction globale sorted. Il faut donc implanter soi-même un algorithme de tri.
On impose une contrainte supplémentaire : l'usage de boucles while ou for est interdit. Il faut ainsi utiliser systématiquement la récursion et //filter//.
==
code==
import collections

# An answer using a quicks0rt
@arguments_generator(map(lambda x: generator.random_list(x), range(128, 130)))
def tidy(x):
        if len(x) == 0:
                return []
        elif len(x) == 1:
                return x
        else:
                pivot = x[len(x)//2] # arbitrary pivot
                a = list(filter(lambda e: e < pivot, x))
                b = list(filter(lambda e: e == pivot, x))
                c = list(filter(lambda e: e > pivot, x))
                if len(a) == 0 and len(c) == 0:
                        return b
                else:
                        return tidy(a) + tidy(b) + tidy(c)
==
