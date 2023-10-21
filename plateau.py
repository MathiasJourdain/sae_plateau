import tkinter as tk
import random 

COULOIR = 0
MUR = 1
AVENTURIER = 3
DRAGON = 8

APPARENCE = {
    COULOIR: ('', '#EEEEEE', '#FFFFFF'),   
    MUR: ('', 'black', '#111111'),          
    AVENTURIER: ('A', '#8888FF', '#AAAAFF'),  
    DRAGON: ('D', '#FF5555', '#FF7777')       
}

def coordonnees_aventurier(d):
    nbl = len(d)
    nbc = len(d[0])

    for y in range(nbl):
        for x in range(nbc):
            if d[y][x] == AVENTURIER:
                return (x, y)


def est_case_proche(d, x, y, xA, yA):
    if (x - 1) == xA and y == yA:
        return True
    elif (x + 1) == xA and y == yA:
        return True
    elif x == xA and (y - 1) == yA:
        return True
    elif x == xA and (y + 1) == yA:
        return True
    else:
        return False

def intervertir(d, x1, y1, x2, y2):
    temp = d[y1][x1]
    d[y1][x1] = d[y2][x2]
    d[y2][x2] = temp

def tentative_deplacement(d, x, y):
    (xA, yA) = coordonnees_aventurier(d)
    if est_case_proche(d, x, y, xA, yA):
        intervertir(d, x, y, xA, yA)
        return True
    else:
        return False



def configurer_fenetre(fe):
    fe.geometry("1200x600")
    fe.title("Plateau de jeu Star Wars")
    fe.configure(bg="black")


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


def modifier_apparence_case(case, v):
    if v in APPARENCE.keys():
        case.configure(text=APPARENCE[v][0])
        case.configure(bg=APPARENCE[v][1])


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


def gerer_clic_case(e, w, d):
    case = e.widget
    x = case.colonne
    y = case.ligne
    if tentative_deplacement(d, x, y):
        modifier_apparence_cases(w, d)


if __name__ == '__main__':

    import doctest
    doctest.testmod()


    complement = [-1, 0]
    C = COULOIR
    M = MUR
    A = AVENTURIER
    D = DRAGON


    donnees = [
        [M, C, C, M, M, C],
        [M, C, D, M, M, C],
        [M, C, C, C, D, C],
        [A, C, C, C, M, M],
        [M, C, M, C, M, C],
        [M, C, M, C, C, C]
    ]


    fenetre = tk.Tk()
    configurer_fenetre(fenetre)

    widgets = creer_cases(fenetre, donnees)
    modifier_apparence_cases(widgets, donnees)

    nbl = len(widgets)
    nbc = len(widgets[0])
    for y in range(nbl):
        for x in range(nbc):
            widgets[y][x].bind('<Enter>', lambda event: eclaircir(event, widgets, donnees))
            widgets[y][x].bind('<Leave>', lambda event: assombrir(event, widgets, donnees))
            widgets[y][x].bind('<Button-1>', lambda event: gerer_clic_case(event, widgets, donnees))

    fenetre.mainloop()