from fonction import * 
import time
import os
import flet 
from flet_core.control_event import ControlEvent

from flet import * 

valeur=[1,2,3,4,5,6,7,8,0]
etat_fin=[
    [1,2,3],
    [4,5,6],
    [7,8,0]
]


etat_actuel=[]
etat_deja_apparue=[]
def initialiser():
    etat_actuel=etat_aleatoire_taquin()
    etat_deja_apparue=[]
    while est_resoluble(etat_actuel)==False:
        etat_actuel=etat_aleatoire_taquin()
    
    teste=False
    while teste==False:
        etat_actuel=etat_aleatoire_taquin()

        while est_resoluble(etat_actuel)==False:
            etat_actuel=etat_aleatoire_taquin()

        etat_deja_apparue=[]
        etat_deja_apparue.append(etat_actuel)
        teste=resolution(etat_actuel, etat_fin, etat_deja_apparue)
    return etat_deja_apparue






def main(page: Page) ->None:
    page.title= "Taquin"
    #page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.window_max_height=405
    page.window_max_width=340
    page.window_min_height=405
    page.window_min_width=340
    case1:Text = Text(valeur[0], TextAlign.CENTER, size=50)
    case2:Text = Text(valeur[1], TextAlign.CENTER, size=50)
    case3:Text = Text(valeur[2], TextAlign.CENTER, size=50)
    case4:Text = Text(valeur[3], TextAlign.CENTER, size=50)
    case5:Text = Text(valeur[4], TextAlign.CENTER, size=50)
    case6:Text = Text(valeur[5], TextAlign.CENTER, size=50)
    case7:Text = Text(valeur[6], TextAlign.CENTER, size=50)
    case8:Text = Text(valeur[7], TextAlign.CENTER, size=50)
    case9:Text = Text(valeur[8], TextAlign.CENTER, size=50)
    def afficher_resolution(e:ControlEvent):
        with open("donne.bin", "rb") as fichier:
            donne = pickle.Unpickler(fichier)
            etat_deja_apparue= donne.load()
        #print("teste1")
        #print(etat_deja_apparue)
        for i in range(len(etat_deja_apparue)):
            #print("teste")
            #print("{}\n{}\n{}\n".format(etat_deja_apparue[i][0],etat_deja_apparue[i][1],etat_deja_apparue[i][2]))
            
            
            valeur=[
                etat_deja_apparue[i][0][0],
                etat_deja_apparue[i][0][1],
                etat_deja_apparue[i][0][2],
                etat_deja_apparue[i][1][0],
                etat_deja_apparue[i][1][1],
                etat_deja_apparue[i][1][2],
                etat_deja_apparue[i][2][0],
                etat_deja_apparue[i][2][1],
                etat_deja_apparue[i][2][2]
            ]
            for j in range(len(valeur)):
                if valeur[j]==0:
                    valeur[j]=""
            
            case1.value = str(valeur[0])
            case2.value = str(valeur[1])
            case3.value = str(valeur[2])
            case4.value = str(valeur[3])
            case5.value = str(valeur[4])
            case6.value = str(valeur[5])
            case7.value = str(valeur[6])
            case8.value = str(valeur[7])
            case9.value = str(valeur[8])
            cout.value = "cout : {}".format(i)
            page.update()
            time.sleep(1)
            
    
    def melanger(e:ControlEvent):
        page.update()
        etat_deja_apparue = initialiser()
        valeur=[
            etat_deja_apparue[0][0][0],
            etat_deja_apparue[0][0][1],
            etat_deja_apparue[0][0][2],
            etat_deja_apparue[0][1][0],
            etat_deja_apparue[0][1][1],
            etat_deja_apparue[0][1][2],
            etat_deja_apparue[0][2][0],
            etat_deja_apparue[0][2][1],
            etat_deja_apparue[0][2][2]
        ]
        for j in range(len(valeur)):
                if valeur[j]==0:
                    valeur[j]=""
        
        with open("donne.bin", "wb") as fichier:
            donne = pickle.Pickler(fichier)
            donne.dump(etat_deja_apparue)
        with open("valeur.bin", "wb") as fichier:
            donne = pickle.Pickler(fichier)
            donne.dump(valeur)
        print(valeur)
        case1.value = str(valeur[0])
        case2.value = str(valeur[1])
        case3.value = str(valeur[2])
        case4.value = str(valeur[3])
        case5.value = str(valeur[4])
        case6.value = str(valeur[5])
        case7.value = str(valeur[6])
        case8.value = str(valeur[7])
        case9.value = str(valeur[8])
       


        page.update()
    
    cout: Text = Text("cout : ")
    page.add(
         Row([
             Container(
                  content=cout,
                  width=100,
                  height=55,
             ),
             FloatingActionButton(text="melanger", width=100, on_click=melanger),
             FloatingActionButton(text="resoudre", width=100, on_click=afficher_resolution),
        ])
    )
    page.add(
            Row(
                [
                    Container(
                        width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.bottom_right,
                                            end=alignment.top_left, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                        
                        content=case1,
                        alignment=alignment.center,
                        border_radius=20,
                    ),
                    Container(
                        width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.top_center,
                                            end=alignment.bottom_center, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                        content=case2,
                        alignment=alignment.center,
                        border_radius=20,
                    ),
                    Container(
                        width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.bottom_left,
                                            end=alignment.top_right, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                        content=case3,
                        alignment=alignment.center,
                        border_radius=20,
                    ),
            ]),
            Row(
                [
                Container(
                    width=100,
                    height=100,
                    gradient=LinearGradient(begin=alignment.center_left,
                                            end=alignment.center_right, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                    content=case4,
                        alignment=alignment.center,
                        border_radius=20,
                ),
                Container(
                    width=100,
                        height=100,
                        gradient=RadialGradient(colors=[colors.GREEN, colors.GREEN,colors.BLUE]),
                    content=case5,
                        alignment=alignment.center,
                        border_radius=20,
                ),
                Container(
                    width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.center_right,
                                            end=alignment.center_left, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                    content=case6,
                        alignment=alignment.center,
                        border_radius=20,
                ),
            ]),
            Row(
                [
                Container(
                    width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.top_right,
                                            end=alignment.bottom_left, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                    content=case7,
                        alignment=alignment.center,
                        border_radius=20,
                ),
                Container(
                    width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.bottom_center,
                                            end=alignment.top_center, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                    content=case8,
                        alignment=alignment.center,
                        border_radius=20,
                ),
                Container(
                    width=100,
                        height=100,
                        gradient=LinearGradient(begin=alignment.top_left,
                                            end=alignment.bottom_right, colors=[colors.BLUE,colors.GREEN, colors.BLUE,colors.BLUE]),
                    content=case9,
                        alignment=alignment.center,
                        border_radius=20,
                ),
            ]),
            
        )
        
    
    page.update()
        
     

for j in range(len(valeur)):
            if valeur[j]==0:
                valeur[j]=""

if __name__ == '__main__':
    app(target=main)