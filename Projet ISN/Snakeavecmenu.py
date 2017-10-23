
########################################################################################################################
########################################################################################################################
########################################################################################################################
##################################################PROJET SNAKE ISN######################################################
#####################################Loïc Chef, Melissa Da Costa, Kévin Zerbib##########################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

#On importe le module tkinter pour l'interface graphique
from tkinter import *
# pour l'aléatoire
from random import randint
#On importe pygame pour la musique et le menu
import pygame
from pygame.locals import*

########################################################################################################################

# création de la fenêtre du menu
FenetreMenu = Tk()

# on donne un nom à cette fenêtre
FenetreMenu.title("Menu du Snake")

# création du canvas
canvas = Canvas(FenetreMenu, width = 1500, height = 450, background = "black")
photo = PhotoImage(file="logo 1.png")
canvas.create_image(0, 0, anchor=NW, image=photo)
# on place le canvas
canvas.pack()

# on crée les boutons du menu 
Button(FenetreMenu, text ="Play", fg="yellow", bg="grey", command = FenetreMenu.destroy, relief = FLAT).pack(side = TOP, padx = 10, pady = 10)
# la boucle de la fenêtre du menu s'arrêtera lorsqu'on appuiera sur la croix rouge
FenetreMenu.mainloop()

# création surface d'affichage
FenetreMenu = pygame.display.set_mode((300,300))
# on initialise le module mixer
pygame.mixer.init()

# le programme va chercher dans les fichiers le son format WAV 
# on créer l'objet sound à l'aide du module mixer de pygame 
son = pygame.mixer.Sound("Most_awesome_8-bit_song_ever.wav")
# le son se lance avec ses paramètres
son.play(loops = -1, maxtime = 0, fade_ms= 0)
####################################################################################################################################
#On créer une fenêtre grâce à la fonction Tk()
fenetre = Tk()

#On change le titre de la fenêtre
fenetre.title('The Snake')

##########################################################################################################################
#On récupère les dimensions de l'écran
hauteur = fenetre.winfo_screenheight()
largeur = fenetre.winfo_screenwidth()

#On convertie les données de la hauteur (H) et de la largeur (L) en int, puis en string,
#et on modifie les dimensions voulues
H = str(int(hauteur/1.1))
L = str(int(largeur/2))

#On applique la taille voulue à la fenêtre grâce à l'appel de fonction geometry(wxh+X+Y) où:
# w, h sont respectivement la largeur et la hauteur
# X et Y sont les coordonnées du point d'origine relativement au coin haut-gauche de la fenêtre
# le x et les deux + sont des séparateurs
# pour insérer les variables, on les concatène avec des chaînes de caractères au moyen de l'opérateur de concaténation +
fenetre.geometry(L + "x" + H + "+0+0")

########################################################################################################################

#On définition des dimensions du plateau de jeu
LargeurPlateau = largeur /2
HauteurPlateau = hauteur /1.2

#On crée un Canvas pour le plateau de jeu
Plateau = Canvas(fenetre, width = LargeurPlateau, height = HauteurPlateau, bg = "pink")
#"side" désigne l'endroit où débute le canvas
Plateau.pack(side="bottom")

#On crée un Canvas pour le score
Barre = Text(fenetre, width = int(largeur /2), height = int(HauteurPlateau / 10), bg = "light blue")
#On place la barre
Barre.pack(side="top")
#On écrit le score initial dans la barre
Barre.insert(END, "score: 0\n")

#On défini le nombre de cases du plateau
NombreDeCases= 75

#On défini les dimenssions d'une case
LargeurCase = (LargeurPlateau / NombreDeCases)
HauteurCase = (HauteurPlateau / NombreDeCases)

########################################################################################################################

#Fonction qui détermine la taille des cases du plateau et qui les colore en vert pour symboliser le serpent
def remplir_case (x, y):

    #On défini les coordonnées (origine_caseX1; origine_caseY1) du point en haut à gauche de la case
    #et (origine_caseX2;origine_caseY2) du point en bas à droite de la case
    OrigineCaseX1 = x * LargeurCase
    OrigineCaseY1 = y * HauteurCase
    OrigineCaseX2 = OrigineCaseX1 + LargeurCase
    OrigineCaseY2 = OrigineCaseY1 + HauteurCase

    #remplissage du rectangle
    Plateau.create_rectangle(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="green")

#On renvoie une case aléatoire
def case_aleatoire():

    AleatoireX = randint(0, NombreDeCases - 1)
    AleatoireY = randint(0, NombreDeCases - 1)

    return (AleatoireX, AleatoireY)

# affichee le serpent, l'argument étant la liste snake
def dessine_serpent(snake):

    #tant qu'il y a des cases dans snake
    for case in snake:

        # on récupère les coordonées de la case
        x, y = case
        # on colorie la case
        remplir_case(x, y)

########################################################################################################################

#On retourne le chiffre 1 si la case est dans le snake, 0 sinon
def etre_dans_snake(case):

    if case in SNAKE:
        EtreDedans = 1
    else:
        EtreDedans = 0

    return EtreDedans

#On renvoie un fruit aléatoire qui n'est pas dans le serpent
def fruit_aleatoire():

    # choix d'un fruit aléatoire
    FruitAleatoire = case_aleatoire()

    # tant que le fruit aléatoire est dans le serpent
    while (etre_dans_snake(FruitAleatoire)):
        # on prend un nouveau fruit aléatoire
        FruitAleatoire = case_aleatoire

    return FruitAleatoire

#On dessine le fruit, idem que pour colorier une case, mais on utilise create_oval à la place
def dessine_fruit():

    global FRUIT

    x, y = FRUIT

    OrigineCaseX1 = x * LargeurCase
    OrigineCaseY1 = y * HauteurCase
    OrigineCaseX2 = OrigineCaseX1 + LargeurCase
    OrigineCaseY2 = OrigineCaseY1 + HauteurCase

    #On remplie l'ovale en rouge pour le fruit

    Plateau.create_oval(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill = "red")

########################################################################################################################

#Ces quatres fonctions permettent le déplacement dans quatres directions du serpent
#elles mettent à jour les coordonées du mouvement
def left_key(event):
    global MOUVEMENT
    MOUVEMENT = (-1, 0)

def right_key(event):
    global MOUVEMENT
    MOUVEMENT = (1, 0)

def up_key(event):
    global MOUVEMENT
    MOUVEMENT = (0, -1)

def down_key(event):
    global MOUVEMENT
    MOUVEMENT = (0, 1)

# indique les fonctions à appeler suite à une pression sur les flèches (ne fonctionne que si la fenêtre a le focus)
fenetre.bind("<Left>", left_key)
fenetre.bind("<Right>", right_key)
fenetre.bind("<Up>", up_key)
fenetre.bind("<Down>", down_key)

########################################################################################################################

# met à jour la variable PERDU indiquant si on a perdu
def serpent_mort(NouvelleTete):

    global PERDU

    NouvelleTeteX, NouvelleTeteY = NouvelleTete

    # si le serpent se mange lui-même (sauf au démarrage, c'est-à-dire: sauf quand MOUVEMENT vaut (0, 0))
    # OU si on sort du canvas
    if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= NombreDeCases or NouvelleTeteY >= NombreDeCases:
        # alors, on a perdu
        PERDU = 1

# met à jour le score
def mise_a_jour_score():

    global SCORE

    SCORE = SCORE + 1
    Barre.delete(0.0, 3.0)
    Barre.insert(END, "score: " + str(SCORE) + "\n")

# met à jour le snake
def mise_a_jour_snake():

    global SNAKE, FRUIT

    # on récupère les coordonées de la tête actuelle
    (AncienneTeteX, AncienneTeteY) = SNAKE[0]
    # on récupère les valeurs du mouvement
    MouvementX, MouvementY = MOUVEMENT
    # on calcule les coordonées de la nouvelle tête
    NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)
    # on vérifie si on a perdu
    serpent_mort(NouvelleTete)
    # on ajoute la nouvelle tête
    SNAKE.insert(0, NouvelleTete)

    # si on mange un fruit
    if NouvelleTete == FRUIT:
        # on génère un nouveau fruit
        FRUIT = fruit_aleatoire()
        # on met à jour le score
        mise_a_jour_score()
    # sinon
    else:
        # on enlève le dernier élément du serpent (c'est-à-dire: on ne grandit pas)
        SNAKE.pop()

#######################################################################################################################################
        
# réinitialise les variables pour une nouvelle partie
def reinitialiser_jeu():

    global SNAKE, FRUIT, MOUVEMENT, SCORE, PERDU

    # serpent initial
    SNAKE = [case_aleatoire()]
    # fruit initial
    FRUIT = fruit_aleatoire()
    # mouvement initial
    MOUVEMENT = (0,0)
    # score initial
    SCORE = 0
    # variable perdu initiale (sera mise à1 si le joueur perd)
    PERDU = 0

# fonction principale
def tache():

    # on met à jour l'affichage et les événements du clavier
    fenetre.update
    fenetre.update_idletasks()
    # on met à jour le snake
    mise_a_jour_snake()
    # on supprime tous les éléments du plateau
    Plateau.delete("all")
    # on redessine le fruit
    dessine_fruit()
    # on redessine le serpent
    dessine_serpent(SNAKE)

    # si on a perdu
    if PERDU:
        # on efface la barre des scores
        Barre.delete(0.0, 3.0)
        # on affiche perdu
        Barre.insert(END, "Perdu avec un score de " + str(SCORE))
        # on prépare la nouvelle partie
        reinitialiser_jeu()
        # on rappelle la fonction principale
        fenetre.after(70, tache)
    # sinon
    else:
        # on rappelle la fonction principale
        fenetre.after(70, tache)

########################################################################################################################

# le snake initial: une liste avec une case aléatoire
SNAKE = [case_aleatoire()]
# le fruit initial
FRUIT = fruit_aleatoire()
# le mouvement initial, une paire d'entiers représentant les coordonées du déplacement, au départ on ne bouge pas
MOUVEMENT = (0, 0)
# le score initial
SCORE = 0
# la variable permettant de savoir si on a perdu, sera mise à 1 si on perd
PERDU = 0

# on appellera la fonction principale pour la première fois juste après être entré dans la boucle de la fenêtre
fenetre.after(0, tache())

#On crée une boucle qui va afficher la fenêtre
#tant que l’utilisateur ne clique pas sur la croix rouge en haut à droite
fenetre.mainloop()
