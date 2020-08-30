import pickle

mon_fichier_dico = open('/Users/cchauvin/Documents/RH-Perso/Scrabble/visu/Dico.bin','rb')
dict_tableau_vers_mot = pickle.load(mon_fichier_dico)
mon_fichier_dico.close()

valeur_des_lettres = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':10,'L':1,'M':2,'N':1,'O':1,'P':3,'Q':8,'R':1,'S':1,'T':1,'U':1,'V':4,'W':10,'X':10,'Y':10,'Z':10}

lettres = 'UW'
meslettres = sorted(lettres)

def quel_score(mot):
    score = 0
    for letter in mot:
        score = score + valeur_des_lettres.get(letter)
    return score

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


toutes_les_combinaisons = trouve_les_combinaisons(lettres)  # toutes les combinaisons en tableau 

toutes_les_solutions=[]
for combinaison in toutes_les_combinaisons:
    solutions = dict_tableau_vers_mot.get(combinaison) 
    if solutions is not None:
        if isinstance(solutions,list):
            for solution in solutions:
                toutes_les_solutions.append(solution)
        else:
            toutes_les_solutions.append(solutions)


tutu = set(toutes_les_solutions)
for i in tutu:
    print('******* '+ i+' ********'+str(quel_score(i)))


#test