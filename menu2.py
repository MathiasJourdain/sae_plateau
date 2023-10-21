import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class Menu:
    personnages = ["R2D2", "Yoda", "Luke", "Chewbacca"]

    def __init__(self):
        self.fenetre = fenetre 
        self.joueurs = 0
        self.personnages_disponibles = list(Menu.personnages)

        self.fenetre_personnages = tk.Toplevel(fenetre)
        self.fenetre_personnages.title(f"Joueur {self.joueurs + 1} - Sélection du Héro")
        label_choix_personnage = tk.Label(self.fenetre_personnages, text=f"Joueur {self.joueurs + 1}, choisis ton Héro:", font=("Helvetica", 16))
        label_choix_personnage.pack(pady=20)
        

        self.frame_images = tk.Frame(self.fenetre_personnages)
        self.frame_images.pack()

        for i, personnage in enumerate(self.personnages_disponibles):
            nom_image = personnage.replace(" ", "_") + ".jpg"
            chemin_image = os.path.join("heros", nom_image)
            image_personnage = Image.open(chemin_image)
            image_personnage = image_personnage.resize((200, 200), Image.BILINEAR)
            image_personnage = ImageTk.PhotoImage(image_personnage)

            bouton_personnage = tk.Button(self.frame_images, text=personnage, command=lambda p=personnage: self.choisir_personnage_pour_joueur(p), font=("Helvetica", 14))
            bouton_personnage.config(image=image_personnage, compound=tk.TOP)
            bouton_personnage.image = image_personnage
            bouton_personnage.pack(side=tk.LEFT, padx=10, pady=10)
            
        

    def fermer_menu_principal(self):
        self.fenetre.destroy()
    
    
    def choisir_personnage_pour_joueur(self, personnage):
        self.joueurs += 1
        self.personnages_disponibles.remove(personnage)
        self.frame_images.destroy()

        if self.joueurs < variable_joueurs.get():
            self.fenetre_personnages.title(f"Joueur {self.joueurs + 1} - Sélection du Héro")
            label_choix_personnage = tk.Label(self.fenetre_personnages, text=f"Joueur {self.joueurs + 1}, choisis ton Héro:", font=("Helvetica", 16))
            label_choix_personnage.pack(pady=20)

            self.frame_images = tk.Frame(self.fenetre_personnages)
            self.frame_images.pack()

            for i, personnage in enumerate(self.personnages_disponibles):
                nom_image = personnage.replace(" ", "_") + ".jpg"
                chemin_image = os.path.join("heros", nom_image)
                image_personnage = Image.open(chemin_image)
                image_personnage = image_personnage.resize((200, 200), Image.BILINEAR)
                image_personnage = ImageTk.PhotoImage(image_personnage)

                bouton_personnage = tk.Button(self.frame_images, text=personnage, command=lambda p=personnage: self.choisir_personnage_pour_joueur(p), font=("Helvetica", 14))
                bouton_personnage.config(image=image_personnage, compound=tk.TOP)
                bouton_personnage.image = image_personnage
                bouton_personnage.pack(side=tk.LEFT, padx=10, pady=10)
        else:
            self.fenetre_personnages.destroy()
            if self.joueurs == variable_joueurs.get():
                print("Démarrer la partie avec les personnages choisis.")
                fenetre.destroy()  # Affiche à nouveau la fenêtre principale
            else:
                messagebox.showerror("Erreur", "Tous les joueurs ont déjà choisi un personnage.")
                self.joueurs = 0
                self.personnages_disponibles = list(Menu.personnages)

def afficher_anciennes_sauvegardes():
    fenetre_sauvegardes = tk.Toplevel(fenetre)
    fenetre_sauvegardes.title("Sauvegardes")

def fermer_fenetre():
    fenetre.destroy()

def lancer_partie():
    choix_joueurs = variable_joueurs.get()
    if choix_joueurs in [1, 4]:
        menu = Menu()
    else:
        messagebox.showerror("Erreur", "Veuillez choisir un nombre de joueurs (1 ou 4) avant de démarrer la mission.")

def quitter_jeu():
    fenetre.quit()

fenetre = tk.Tk()
fenetre.title("Menu de jeu")

largeur_fenetre = fenetre.winfo_screenwidth()
hauteur_fenetre = fenetre.winfo_screenheight()

image_fond = Image.open("fond3.jpg")
image_fond = image_fond.resize((largeur_fenetre, hauteur_fenetre), Image.BILINEAR)
image_fond = ImageTk.PhotoImage(image_fond)

canvas_fond = tk.Canvas(fenetre, width=largeur_fenetre, height=hauteur_fenetre)
canvas_fond.pack()
canvas_fond.create_image(0, 0, anchor=tk.NW, image=image_fond, tags="background")

cadre_widgets = tk.Frame(fenetre, bg="#282c34")  
cadre_widgets.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_titre = tk.Label(cadre_widgets, text="Star Wars le jeu", font=("Comic Sans MS", 24), fg="blue")
label_titre.pack(pady=20)

variable_joueurs = tk.IntVar()

bouton_1_joueur = tk.Radiobutton(cadre_widgets, text="1 Joueur", variable=variable_joueurs, value=1,
                                  fg="blue", selectcolor='#FF0000', font=("Comic Sans MS", 18))
bouton_1_joueur.config(bg='#282c34')
bouton_1_joueur.pack(pady=10)

bouton_4_joueurs = tk.Radiobutton(cadre_widgets, text="4 Joueurs", variable=variable_joueurs, value=4,
                                  fg="blue", selectcolor='#FF0000', font=("Comic Sans MS", 18))
bouton_4_joueurs.config(bg='#282c34')
bouton_4_joueurs.pack(pady=10)

bouton_lancer_partie = tk.Button(cadre_widgets, text="Démarrer la mission", command=lancer_partie,
                                 fg="black", bg='#FF0000', font=("Comic Sans MS", 20))
bouton_lancer_partie.pack(pady=20)

bouton_quitter = tk.Button(cadre_widgets, text="Quitter", command=quitter_jeu,
                            fg="black", bg='#FF0000', font=("Comic Sans MS", 20))
bouton_quitter.pack(pady=20)

fenetre.attributes("-fullscreen", True)
fenetre.mainloop()
