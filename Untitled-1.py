##----- Importation des Modules -----##
from tkinter import *


##----- Définition des Variables globales -----##



##----- Définition des Fonctions -----##
def afficher(event) :
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la case du clic de souris"""
    abscisse = event.x
    ordonnee = event.y
    l = (ordonnee-2)//100                  # Ligne du clic
    c = (abscisse-2)//100                  # Colonne du clic
    message.configure(text='Clic en ligne = {} et colonne = {}'.format(l, c))


##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Plateau de jeu')


##----- Zones de texte -----##
message = Label(fen, text="Bienvenu dans l'Etoile de la Mort !")
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


##----- Boutons -----##
bouton_quitter = Button(fen, text='Quitter', command = fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx = 3, pady = 3, sticky = S+W+E)

bouton_reload = Button(fen, text='Recommencer')
bouton_reload.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = S+W+E)


##----- Canevas -----##
dessin = Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)


##----- La grille -----##
lignes = []
for i in range(4):
    lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
    lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


##-----Evenements-----##
dessin.bind('<Button-1>', afficher)


##----- Programme principal -----##
dessin.bind('<Button-1>', afficher)
fen.mainloop()                      # Boucle d'attente des événements