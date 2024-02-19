import pickle
import random


def resolution(etat_actuel, etat_fin, etat_deja_apparue):
    i=0
    while i<500:
        mouvement_possible=recherche_mouvement_possible(etat_actuel)
        etat_fils = recherche_etat_fils(etat_actuel, mouvement_possible)
        etat_actuel=etat_suivant(etat_deja_apparue[len(etat_deja_apparue)-1], etat_fils, etat_fin, etat_deja_apparue )
        ajouter_etat_deja_apparue(etat_deja_apparue, etat_actuel)
        if etat_actuel==etat_fin:
            break
        i+=1
    
    if i==500:
        return False
    else:
        
        return True

def est_resoluble(etat):
    nb_inversions = 0
    liste_elements = [elem for sublist in etat for elem in sublist if elem != 0]  # Extraction des éléments de l'état

    for i in range(len(liste_elements)):
        for j in range(i + 1, len(liste_elements)):
            if liste_elements[i] > liste_elements[j]:
                nb_inversions += 1

    return nb_inversions % 2 == 0  # Renvoie True si le nombre d'inversions est pair (état résoluble), sinon False
    
def etat_aleatoire_taquin():
    liste_complete = [i for i in range(9)]  # Crée une liste ordonnée de 0 à 8
    random.shuffle(liste_complete)  # Mélange aléatoirement la liste

    # Crée une liste de trois sous-listes de trois chiffres chacune
    etat_aleatoire = [[liste_complete[0],liste_complete[1],liste_complete[2]],
                      [liste_complete[3],liste_complete[4],liste_complete[5]],
                      [liste_complete[6],liste_complete[7],liste_complete[8]]]
    
    return etat_aleatoire

def ajouter_etat_deja_apparue(m, n):
    if n not in m:
        m.append(n)
    return m

def supprimer_liste_si_presente(m, n, x):
    if n in x:
        m.remove(n)
    return m

def distance_de_manhattan(etat_actuel, etat_but):
    #fonction mi-calcule distance de manhattan entre 2 etat , 1 état père et in état fils
    distance = 0
    for i in range(3):
        for j in range(3):
            if etat_actuel[i][j]!=etat_but[i][j] and etat_actuel[i][j]!=0:
                valeur_case = etat_actuel[i][j]
                for x in range(3):
                    for y in range(3):
                        if etat_but[x][y]==valeur_case:
                            distance+= abs(x-i) + abs(y - j)
                    
    return distance

def recherche_mouvement_possible(etat_actuel):
    mouvement_possible=[]
    for i in range(3):
        for j in range(3):
            #verification des mouvement possible a partir de l'etat actuel
            if etat_actuel[i][j]==0:
                if i > 0:  # Déplacement vers le haut
                    mouvement_possible.append((i - 1, j))
                if i < 2:  # Déplacement vers le bas
                    mouvement_possible.append((i + 1, j))
                if j > 0:  # Déplacement vers la gauche
                    mouvement_possible.append((i, j - 1))
                if j < 2:  # Déplacement vers la droite
                    mouvement_possible.append((i, j + 1))
    return mouvement_possible

def recherche_etat_fils(etat, mouvement_possible):
    #fonction manao ny mouvement 
    etat_fils=[]
    for i in range(3):
        for j in range(3):
            if etat[i][j]==0:
                if len(mouvement_possible)==2:
                    p1=mouvement_possible[0]; p2=mouvement_possible[1]
                    case1=etat[i][j];case2=etat[p1[0]][p1[1]]
                    case3=etat[p2[0]][p2[1]]
                    etat_fils.append([row[:] for row in etat])
                    etat_fils.append([row[:] for row in etat])
                    etat_fils[0][i][j]=case2; etat_fils[0][p1[0]][p1[1]]=case1
                    etat_fils[1][i][j]=case3; etat_fils[1][p2[0]][p2[1]]=case1                     
                if len(mouvement_possible)==3:
                    p1=mouvement_possible[0]
                    p2=mouvement_possible[1]
                    p3=mouvement_possible[2]
                    case1=etat[i][j]
                    case2=etat[p1[0]][p1[1]]
                    case3=etat[p2[0]][p2[1]]
                    case4=etat[p3[0]][p3[1]]
                    etat_fils.append([row[:] for row in etat])
                    etat_fils.append([row[:] for row in etat])
                    etat_fils.append([row[:] for row in etat])
                    etat_fils[0][i][j]=case2
                    etat_fils[0][p1[0]][p1[1]]=case1
                    etat_fils[1][i][j]=case3
                    etat_fils[1][p2[0]][p2[1]]=case1
                    etat_fils[2][i][j]=case4
                    etat_fils[2][p3[0]][p3[1]]=case1

                if len(mouvement_possible)==4:
                    p1=mouvement_possible[0]
                    p2=mouvement_possible[1]
                    p3=mouvement_possible[2]
                    p4=mouvement_possible[3]
                    case1=etat[i][j]
                    case2=etat[p1[0]][p1[1]]
                    case3=etat[p2[0]][p2[1]]
                    case4=etat[p3[0]][p3[1]]
                    case5=etat[p4[0]][p4[1]]
                    etat_fils.append([row[:] for row in etat])
                    etat_fils.append([row[:] for row in etat])
                    etat_fils.append([row[:] for row in etat])
                    etat_fils.append([row[:] for row in etat])
                    etat_fils[0][i][j]=case2
                    etat_fils[0][p1[0]][p1[1]]=case1
                    etat_fils[1][i][j]=case3
                    etat_fils[1][p2[0]][p2[1]]=case1
                    etat_fils[2][i][j]=case4
                    etat_fils[2][p3[0]][p3[1]]=case1
                    etat_fils[3][i][j]=case5
                    etat_fils[3][p4[0]][p4[1]]=case1
    return etat_fils

def etat_suivant(etat_precedent, etat_fils, etat_fin, etat_deja_apparue):
    heuristique = []
    
    if etat_precedent in etat_fils:
        etat_fils.remove(etat_precedent)
    
    for etat in etat_fils:
        if etat in etat_deja_apparue:
            etat_fils.remove(etat)
    
    for i in range(len(etat_fils)):
        heuristique.append(distance_de_manhattan(etat_fils[i], etat_fin))
    indice_etat_fils = 0
    h=heuristique[0]
    for i in range(len(heuristique)-1):
            if h>heuristique[i+1]:
                h=heuristique[i+1]
                indice_etat_fils = i+1
    
    return etat_fils[indice_etat_fils]


'''with open("donne.bin", "wb") as fichier:
    donne = pickle.Pickler(fichier)
    donne.dump(etat_actuel)

with open("donne.bin", "rb") as fichier:
    donne = pickle.Unpickler(fichier)
    text= donne.load()
'''