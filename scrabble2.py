import pickle

mon_fichier_dico = open('/Users/cchauvin/Documents/RH-Perso/Scrabble/visu/Dico.bin','rb')
dict_tableau_vers_mot = pickle.load(mon_fichier_dico)
mon_fichier_dico.close()

print('Veuillez entrer les lettres : ')
lettres = input('Veuillez entrer les lettres : ')

tutu = dict_tableau_vers_mot.get(lettres)
if isinstance (tutu,list):
    for i in tutu:
        print('******* '+ i+' ********')
else:
    print('******* '+ tutu+' ********')

