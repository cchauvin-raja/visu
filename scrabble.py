# scrabble.py
# chauvin
# def enleve_accents(mot):
import unidecode
import pickle

fname = '/Users/cchauvin/Documents/RH-Perso/Scrabble/visu/' + 'liste.de.mots.francais.frgut.txt'
with open(fname) as f:
    mots_bruts = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
mots_bruts = [x.strip() for x in mots_bruts]
mots_bruts = [unidecode.unidecode(x) for x in mots_bruts]
set_de_mots = set(mots_bruts)

dict_tableau_vers_mot ={}
for mot in set_de_mots:
    liste_de_lettres = [x for x in mot]
    liste_de_lettres.sort()
    valeur_du_dict = dict_tableau_vers_mot.get(''.join(liste_de_lettres))
    if valeur_du_dict is None:
        dict_tableau_vers_mot[''.join(liste_de_lettres)] = mot
    elif isinstance(valeur_du_dict,str):
        tableau_temp = []
        tableau_temp.append(valeur_du_dict)
        tableau_temp.append(mot)
        dict_tableau_vers_mot[''.join(liste_de_lettres)] = tableau_temp
    else:
        dict_tableau_vers_mot[''.join(liste_de_lettres)] = valeur_du_dict.append(mot)
    # si plusieurs mots pour un litste fair un tablea
    pass
mon_fichier_dico = open('/Users/cchauvin/Documents/RH-Perso/Scrabble/visu/Dico.bin','wb')
pickle.dump(dict_tableau_vers_mot,mon_fichier_dico)
mon_fichier_dico.close

# liaison entre un mot et un tableau de lettres trié
# quand je prend un tirage je le transforme en tableau trié et je voies les mots possibles

# télécharger la liste des mots http://www.pallier.org/liste-de-mots-francais.html
#  pip install Unidecode
# transformer tous les mots avec b= unidecode.unidecode(a)
# en faire un set
# retirer les mots composés
#############################
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
#############################

# class reglette:
#     def __init__(self):
#         lettre
    
#     def tire_lettre(self,sac_de_lettre):

#     def pose_mot(self,grille):
#         # pour tous les mots de la grille, l'ajout de lettres fait il un mot 

# class grille_scrabble:
#     def __init__(self):

#     def ajoute(mot):

#     def valorise_mot(mot,coord_x,coord_y)