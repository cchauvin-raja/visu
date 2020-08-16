import pickle

mon_fichier_dico = open('/Users/cchauvin/Documents/RH-Perso/Scrabble/visu/Dico.bin','rb')
dict_tableau_vers_mot = pickle.load(mon_fichier_dico)
mon_fichier_dico.close()

# print('Veuillez entrer les lettres : ')
# lettres = input('Veuillez entrer les lettres : ')
lettres = 'oolpag'
meslettres = sorted(lettres)

def combinaison_lettres(tirage, longueur):
    # permet de faire toutes les combinaisaons de k lettre à partir d'un tableau
    # à transformer avec chaines
    p = []
    i, imax = 0, 2**len(tirage)-1
    while i<=imax:
        s = []
        j, jmax = 0, len(tirage)-1
        while j<=jmax:
            if (i>>j)&1==1:
                s.append(tirage[j])
            j += 1
        if len(s)==longueur:
            p.append(''.join(sorted(s)))
        i += 1 
    return p

def trouve_les_combinaisons(lettres):
    tableau_combi=[]
    for z  in range(len(lettres)):
        for combinaison in combinaison_lettres(lettres,z):
            if len(combinaison) >= 2 :
                tableau_combi.append(combinaison)
    tableau_combi.append(lettres)
    return tableau_combi


toutes_les_combinaisons = trouve_les_combinaisons(lettres)

toutes_les_solutions=[]
for combinaison in toutes_les_combinaisons:
    solutions = dict_tableau_vers_mot.get(combinaison) 
    if solutions is not None:
        if isinstance(solutions,list):
            for solution in solutions:
                toutes_les_solutions.append(solution)
        else:
            toutes_les_solutions.append(solutions)


tutu = dict_tableau_vers_mot.get(lettres)
if isinstance (tutu,list):
    for i in tutu:
        print('******* '+ i+' ********')
else:
    print('******* '+ tutu+' ********')

test