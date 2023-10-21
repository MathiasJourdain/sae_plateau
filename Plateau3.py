import tkinter as tk
import random
from menu2 import Menu
import time
import tkinter.font as tkFont

# Définition des constantes
COULOIR = 0
MUR = 1
HERO = 3
VADOR = 8
STORMTROOPER = 5
BLASTER = 4
KYLO = 2

temps_debut_partie = None

# Définition des apparences des cases
APPARENCE = {
    COULOIR: ('', '#EEEEEE', '#FFFFFF'),   
    MUR: ('', 'black', '#111111'),          
    HERO: ('H', '#8888FF', '#AAAAFF'),  
    VADOR: ('V', '#FF5555', '#FF7777'),  
    STORMTROOPER: ('S', '#FF5555', '#FF7777'),  
    BLASTER: ('B','#EE82EE','#9400D3'), 
    KYLO: ('K','#FF5555','#FF7777')
}

#Qui permet de trouver les coordonnées du héro
def coordonnees_hero(d):
    nbl = len(d)
    nbc = len(d[0])

    for y in range(nbl):
        for x in range(nbc):
            if d[y][x] == HERO:
                return (x, y)


#Qui permet de déplacer le héro dans les cases proches
def est_case_proche(d, x, y, xA, yA):
    if (x - 1) == xA and y == yA:
        return True
    elif (x + 1) == xA and y == yA:
        return True
    elif x == xA and (y - 1) == yA:
        return True
    elif x == xA and (y + 1) == yA:
        return True
    elif (x - 1) == xA and (y - 1) == yA:
        return True
    elif (x + 1) == xA and (y - 1) == yA:
        return True
    elif (x - 1) == xA and (y + 1) == yA:
        return True
    elif (x + 1) == xA and (y + 1) == yA:
        return True
    else:
        return False

#Qui permet d'intervertir les cases
def intervertir(d, x1, y1, x2, y2):
    temp = d[y1][x1]
    d[y1][x1] = d[y2][x2]
    d[y2][x2] = temp
    
#Qui permet de déplacer le héro dans les cases proches
def tentative_deplacement(d, x, y):
    (xA, yA) = coordonnees_hero(d)
    destination = d[y][x]
    if est_case_proche(d, x, y, xA, yA) and (destination == COULOIR or destination == VADOR or destination == STORMTROOPER):
        intervertir(d, x, y, xA, yA)
        return True
    else:
        return False

    
#Qui permet de configurer la fenêtre
def configurer_fenetre(fe):
    fe.geometry("1200x600")
    fe.title("Plateau de jeu Star Wars")
    fe.configure(bg="black")

    # Créez un label pour afficher le temps en haut à droite
    temps_label = tk.Label(fe, text="Temps: 0", font=("Helvetica", 16))
    temps_label.place(x=1000, y=10)

    # Fonction pour mettre à jour le temps
    def mettre_a_jour_temps():
        temps_debut = time.time()
        while True:
            temps_actuel = int(time.time() - temps_debut)
            temps_label.config(text=f"Temps: {temps_actuel} sec")
            fe.update()
            time.sleep(1)

    # Lancez la fonction de mise à jour du temps dans un thread
    import threading
    temps_thread = threading.Thread(target=mettre_a_jour_temps)
    temps_thread.daemon = True
    temps_thread.start()

#Qui permet de créer les cases
def creer_cases(fe, d):
    nbl = len(d)
    nbc = len(d[0])


    w = [[None for x in range(nbc)] for y in range(nbl)]


    for y in range(nbl):
        for x in range(nbc):

            numero = x + y * nbc


            w[y][x] = tk.Label(fe, text=numero, fg="white", bg='grey', width=10, height=5)


            px = 20 + x * 90
            py = 20 + y * 85
            w[y][x].place(x=px, y=py)


            w[y][x].numero = numero
            w[y][x].colonne = x
            w[y][x].ligne = y


    return w

#Qui permet de modifier l'apparence des cases
def modifier_apparence_case(case, v):
    if v in APPARENCE.keys():
        case.configure(text=APPARENCE[v][0])
        case.configure(bg=APPARENCE[v][1])

#Qui permet de modifier l'apparence des cases
def modifier_apparence_cases(w, d):
    nbl = len(d)
    nbc = len(d[0])

    for y in range(nbl):
        for x in range(nbc):
            modifier_apparence_case(w[y][x], d[y][x])


def eclaircir(e, w, d):
    case = e.widget
    y = case.ligne
    x = case.colonne
    code = d[y][x]
    if case.cget('bg') != APPARENCE[MUR][1] and code in APPARENCE:
        nouvelle_couleur = APPARENCE[code][2]
        case.configure(bg=nouvelle_couleur)


def assombrir(e, w, d):
    case = e.widget
    y = case.ligne
    x = case.colonne
    code = d[y][x]
    if case.cget('bg') != APPARENCE[MUR][1] and code in APPARENCE:
        nouvelle_couleur = APPARENCE[code][1]
        case.configure(bg=nouvelle_couleur)

def fenetre_combat():
    fenetre_combat = tk.Toplevel()
    fenetre_combat.geometry("400x200")
    fenetre_combat.title("Combat")

    # Étiquettes pour afficher les noms des personnages et leurs barres de vie
    label_hero = tk.Label(fenetre_combat, text="Héro:")
    label_ennemi = tk.Label(fenetre_combat, text="Ennemi:")
    label_hero.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    label_ennemi.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Barres de vie
    barre_vie_hero = tk.Progressbar(fenetre_combat, orient="horizontal", length=200, mode="determinate")
    barre_vie_ennemi = tk.Progressbar(fenetre_combat, orient="horizontal", length=200, mode="determinate")
    barre_vie_hero.grid(row=0, column=1, padx=10, pady=5)
    barre_vie_ennemi.grid(row=1, column=1, padx=10, pady=5)

    # Boutons "Attaquer" et "Se soigner"
    bouton_attaquer = tk.Button(fenetre_combat, text="Attaquer")
    bouton_soigner = tk.Button(fenetre_combat, text="Se soigner")
    bouton_attaquer.grid(row=2, column=0, padx=10, pady=10)
    bouton_soigner.grid(row=2, column=1, padx=10, pady=10)

    print("Vous entrez dans une phase de combat !") 

    fenetre_combat.mainloop()


#Qui permet de gérer le clic sur les cases
def gerer_clic_case(e, w, d):
    case = e.widget
    x = case.colonne
    y = case.ligne

    if est_case_proche(d, x, y, *coordonnees_hero(d)):
        destination = d[y][x]
        if destination in [COULOIR, VADOR, STORMTROOPER, KYLO]:
            if destination in [VADOR, STORMTROOPER, KYLO]:
                fenetre_combat()
            d[coordonnees_hero(d)[1]][coordonnees_hero(d)[0]] = COULOIR
            d[y][x] = HERO
            modifier_apparence_cases(w, d)
        else:
            print(f'Déplacement impossible : ({x}, {y})')
    else:
        print(f'Déplacement impossible : ({x}, {y})')


def intervertir(d, x1, y1, x2, y2):
    temp = d[y1][x1]
    d[y1][x1] = d[y2][x2]
    d[y2][x2] = temp
    print(f'Déplacement : ({x1}, {y1}) -> ({x2}, {y2})')

def gerer_clic_case(e, w, d):
    case = e.widget
    x = case.colonne
    y = case.ligne
    if tentative_deplacement(d, x, y):
        modifier_apparence_cases(w, d)
        print(f'Déplacement réussi : ({coordonnees_hero(d)})')
    else:
        print(f'Déplacement impossible : ({x}, {y})')

#Qui permet de générer un plateau aléatoire        
def generer_plateau_aleatoire():
    """
    Génère aléatoirement un nouveau plateau de jeu.
    """
    elements = [COULOIR, MUR]  

    nouveau_plateau = []

    nbl = 8
    nbc = 8

    for _ in range(nbl):
        ligne = [random.choice(elements) for _ in range(nbc)]
        nouveau_plateau.append(ligne)

    # Placez 4 héros aléatoirement
    for _ in range(4):
        x_hero = random.randint(0, nbc - 1)
        y_hero = random.randint(0, nbl - 1)
        while nouveau_plateau[y_hero][x_hero] != COULOIR:
            x_hero = random.randint(0, nbc - 1)
            y_hero = random.randint(0, nbl - 1)
        nouveau_plateau[y_hero][x_hero] = HERO

    # Placez Vador aléatoirement
    vador_place = False
    while not vador_place:
        x_vador = random.randint(0, nbc - 1)
        y_vador = random.randint(0, nbl - 1)
        if nouveau_plateau[y_vador][x_vador] == COULOIR:
            nouveau_plateau[y_vador][x_vador] = VADOR
            vador_place = True
    
    # Placez KYLO REN aléatoirement
    kylo_place = False
    while not kylo_place:
        x_kylo = random.randint(0, nbc - 1)
        y_kylo = random.randint(0, nbl - 1)
        if nouveau_plateau[y_kylo][x_kylo] == COULOIR:
            nouveau_plateau[y_kylo][x_kylo] = KYLO
            kylo_place = True

    # Placez 4 Stormtroopers aléatoirement
    stormtroopers_places = 0
    while stormtroopers_places < 4:
        x_stormtrooper = random.randint(0, nbc - 1)
        y_stormtrooper = random.randint(0, nbl - 1)
        if nouveau_plateau[y_stormtrooper][x_stormtrooper] == COULOIR:
            nouveau_plateau[y_stormtrooper][x_stormtrooper] = STORMTROOPER
            stormtroopers_places += 1
            
    # Placez 2 Blasters aléatoirement
    blasters_places = 0
    while blasters_places < 2:
        x_blasters = random.randint(0, nbc - 1)
        y_blasters = random.randint(0, nbl - 1)
        if nouveau_plateau[y_blasters][x_blasters] == COULOIR:
            nouveau_plateau[y_blasters][x_blasters] = BLASTER
            blasters_places += 1

    return nouveau_plateau

def quitter_jeu():
    global temps_debut_partie
    temps_fin_partie = time.time()

    if temps_debut_partie is not None:
        duree_partie = int(temps_fin_partie - temps_debut_partie)
        print(f"La partie a duré {duree_partie} secondes.")
    
    fenetre.destroy()


def retourner_au_menu():
    fenetre.destroy()
    Menu()
    
# Programme principal
if __name__ == '__main__':
    # Générez un plateau aléatoire avec un seul héros
    donnees = generer_plateau_aleatoire()

    import doctest
    doctest.testmod()

    complement = [-1, 0]
    C = COULOIR
    M = MUR
    H = HERO
    V = VADOR
    K = KYLO
    S = STORMTROOPER
    B = BLASTER

    
    fenetre = tk.Tk()
    configurer_fenetre(fenetre)

    temps_debut_partie = time.time()
    
    widgets = creer_cases(fenetre, donnees)
    modifier_apparence_cases(widgets, donnees)

    nbl = len(widgets)
    nbc = len(widgets[0])
    for y in range(nbl):
        for x in range(nbc):
            widgets[y][x].bind('<Enter>', lambda event: eclaircir(event, widgets, donnees))
            widgets[y][x].bind('<Leave>', lambda event: assombrir(event, widgets, donnees))
            widgets[y][x].bind('<Button-1>', lambda event: gerer_clic_case(event, widgets, donnees))

    # Créez une police personnalisée pour les boutons
    custom_button_font = tkFont.Font(family="Comic Sans MS", size=12, weight="bold")

    # Créez un bouton "Menu" avec la police personnalisée
    bouton_menu = tk.Button(fenetre, text="Menu", command=retourner_au_menu, fg="black", bg='#FF0000', font=custom_button_font)
    bouton_menu.place(x=1000, y=400)

    #   Créez un bouton "Quitter" avec la police personnalisée
    bouton_quitter_plateau = tk.Button(fenetre, text="Quitter", command=quitter_jeu, fg="black", bg='#FF0000', font=custom_button_font)
    bouton_quitter_plateau.place(x=1000, y=500)

    fenetre.mainloop()
