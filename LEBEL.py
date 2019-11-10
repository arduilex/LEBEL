####################################################################
# Copyright (C) 2019-2019 BADER Alexandre <alexandrebader3@gmail.com>
#
# This file is part of LEBEL.
#
# LEBEL can not be copied and/or distributed without the express
# permission of Alexandre
####################################################################

# Ce programme est la v4.0 du projet LEBEL
# Fait le 07/11/2019
# Par Alexandre BADER

# Définie la procédure apprendre() avec les paramètres <list1> et  <list2>
def apprendre(list1, list2):
    # Cette procédure permet d'apprendre
    # Tout les mots en les affichants un par un
    # Initialisation de <int> <N> au nombre de mots que contient la liste <str> <list1>
    print("Bienvenue dans le mode APPRENDRE\n")
    for i in range(len(list1)):      # Pour i allant de 0 au nombre de mot dans <list1>
        # Affiche le mot de <list1> et sa traduction de <list2>
        print(i+1, '. ', list1[i], ' = ', list2[i], sep='', end=' ')
        input()  # attend que l'utilisateur ai retenue les 2 mots
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin de l'apprentissage\nAppuiez sur entrée pour revenir au menu...")

# Définie la procédure reviser() avec les paramètres <list1>, <list2> et <list3>
def reviser(list1, list2, list3):
    # Cette procédure permet de réviser ses mots
    # avec un simple affichage du mot de la langue choisit
    # Lorsque l'utilisateur à trouver la traduction dans sa tête
    # il peut vérifier si cette dernière est juste en affichant la traduction correcte
    print("Bienvenue dans le mode REVISER\n")
    # Demande si l'utilisateur veut afficher les mots à traduires en langue 1 ou langue 2 (de la <list3>)
    print("Vous voulez réviser en ",
          list3[0], '(1)/', list3[1], "(2) : ", sep='', end='')
    langue = input()    # Saisir la langue voulu
    # <list1> et <list2> sont des adresses des listes misent en paramètres lors de l'appelle de cette procédure
    # Afin de ne pas modifier les listes de mot <global> dans le programme principal
    # une copie des valeurs des 2 listes (par adresse) est effectuée
    # sur leurs intervalles complets [:] = [0:len(list)]
    fr, et = list1[:], list2[:]     # Copie des liste <list1> et <list2> dans <fr> et <et>
    for i in range(len(list1)):      # Pour i allant de 0 au nombre de mot dans <list1>
         # Affecter à r un nombre aléatoire compris entre 0 et la longeur de <fr> -1 pour ne pas dépasser l'index maximal de la liste
        r = randint(0, len(fr)-1)
        if langue == '1':   # Si la langue désirée est la première de <list3>
            # Affecter à <mot> le mot <str> d'index <r> de <fr>(list1) et à <trad> sa traduction qui est l'index <r> de <et>(list2)
            mot, trad = fr[r], et[r]
        else:               # Si la langue choisit est la deuxième
            # Affecter à <mot> le mot <str> d'index <r> de <et>(list2) et à <trad> sa traduction qui est l'index <r> de <fr>(list1)
            mot, trad = et[r], fr[r]
        print(i+1, '/', len(list1), " La traduction de <", mot, "> est...", sep='', end='')   # Affiche le premier mot
        input()     # Attend que l'utilisateur trouve la traduction dans sa tête
        print('>', trad, end='')  # Affiche la bonne traduction
        input()     # Attend que l'utilisateur appuie sur entrée pour passer au mot suivant
        del fr[r]   # Supprime le mot <fr> d'index <r> pour ne pas qu'il soit réutilisé
        del et[r]   # Supprime le mot <fr> d'index <r> pour ne pas qu'il soit réutilisé
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin de la revision\nAppuiez sur entrée pour revenir au menu...")

# Définie la fonction test() avec les paramètres <list1>, <list2> et <list3>
def test(list1, list2, list3):
    # Cette procédure permet de tester ses connaissaces
    # sans que la note n'est d'impacte sur le fichier score.txt ou la variable <pointF>
    # Le test est semblable à reviser() à la différence que la traduction doit être écrite
    # Puis le script vérifie si cette réponse correspond à la tradcution
    # Si, ce n'est pas le cas afficher directement la bonne réponse
    global base     # Informe à Python que la variable base peut être utiliser partout dans le programme
    N = len(list1)      # Initialisation de <int> <N> à la longeur de  <list1>
    p = 0       # Initialisation de <int> <p> (pour point) à 0
    print("Bienvenue dans le mode TEST\n")
    # Demande si l'utilisateur veut afficher les mots à traduires en langue 1 ou langue 2 (de la <list3>)
    print("Vous voulez réviser en ",
          list3[0], '(1)/', list3[1], "(2) : ", sep='', end='')
    langue = input()        # Saisir la langue voulu
    fr, et = list1[:], list2[:]     # Copie des liste <list1> et <list2> dans <fr> et <et>
    for i in range(N):      # Pour i allant de 0 à N
        # Affecte à <r> un entier aléatoire entre 0 et len(fr)-1
        r = randint(0, len(fr)-1)
        if langue == '1':   # Si la langue désirée est la première de la <list3>
            # Affecter à <mot> le mot <str> d'index <r> de <fr>(list1) et à <trad> sa traduction qui est l'index <r> de <et>(list2)
            mot, juste = fr[r], et[r]
        else:
            # Affecter à <mot> le mot <str> d'index <r> de <et>(list2) et à <trad> sa traduction qui est l'index <r> de <fr>(list1)
            mot, juste = et[r], fr[r]
        # Demande la tradcution de la variable <str> mot
        print(i+1, '/', N-p, " Donne moi la traduction de <", mot, '> : ', sep='', end='')
        reponse = input()       # Enregistre la réponse dans la variable <str> <reponse>
        if reponse == juste:    # Si la réponse est identique à la bonne traduction
            print(">BRAVO !")
            p += 1          # Incrémenter 1 à la variable <p>
        else:
            print(">FAUX, la réponse était <", juste, '>',
                  sep='')     # Affiche la bonne traduction
        # Supprime l'index <r> de la lsite <fr> pour ne pas que la fonction randint() ressorte le même index
        del fr[r]       # Supprime l'index <r> de la liste <fr>
        del et[r]       # Supprime l'index <r> de la liste <et>
    # Affiche la note sur le nombre total de mots et une autre note sur <base>
    print("\nFin du test ", p, "/", N, ' (', round(p/N*base), '/', base, ')', sep='')
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("Appuiez sur entrée pour revenir au menu...")

# Définie la procédure controle() avec les paramètres <list1>, <list2> et <list3>
def controle(list1, list2, list3):
    # Cette procédure est la plus avancée dans l'apprentissage des mots
    # Chaque bonne et mauvaise réponse a un impacte sur la liste <pointF>(list3)
    # La variable <note> affecte la variable local <score> de controle(), si ce dernier est meilleur que la varaible <note>
    global base, note   # Déclaration des variables <base> et <note> comme étant global donc utilisables partout
    N = len(list1)      # Initialisation de la variable <int> <N> à la longueur de <list1>
    print("Bienvenue dans le mode CONTROLE\n")
    fr, et = list1[:], list2[:]     # Copie des liste <list1> et <list2> dans <fr> et <et>
    p = 0  # Nomre de point pour chaque réponse juste
    # Initialisation à vide de la liste <str> <corrige>
    # Qui contiendra les corrections si des traductions sont fausses
    corrige = []    # Initialisation de la lsite <corrige>
    for i in range(N):  # Pour i allant de 0 à N
        r = randint(0, len(fr)-1)   # Choisit un rang <r> entre 0 et la longeur de <fr> -1
        if randint(0, 1):       # Une chance sur deux de traduire le mot dans la langue 1 ou 2
            mot, juste = fr[r], et[r]   # Affecte les mots du rang <r> des listes <fr> et <et> dans les variables, de types string, <mot> et <juste>
            corrige.append(mot)     # Ajoute à la liste <corrige> le mot à traduire <mot>
            index = list2.index(juste)  # Affecte à la variable <int> <index> l'index i du mot <juste> de la liste <list2>
                                        # grâce la fonction .index() qui retourne l'index de la valeur recherchée dans la liste demandée
        else:   # Le mot à traduire sera en langue 2
            mot, juste = et[r], fr[r]   # Affecte les mots du rang <r> des listes <et> et <fr> dans les variables de types string <mot> et <juste>
            corrige.append(mot)     # Ajoute à la liste <corrige> le mot à traduire <mot>
            index = list1.index(juste)  # Affecte à la variable <int> <index> l'index i du mot <juste> de la liste <list2>
        # Affiche le mot à traduire <mot> en précisant combien il en reste en affichant sur <N> la variable local <i>
        print(i+1, '/', N, ' <', mot, sep='', end='> : ')
        reponse = input()   # Saisir la tradution dans la variable <str> <reponse>
        if reponse == juste:    # Si la réponse correspond bien à la bonne tradution
            # Script pour gérer les point faibles du mot actuelle
            if list3[index] > 0:    # Si le mot actuelle est une difficulté
                list3[index] -= 4   # Enlever 3 points de difficulté pour avoir eu juste
                if list3[index] < 0:    # Si la nouvelle valeur de l'index <index> de la liste <list3> est négative
                    list3[index] = 0    # Remettre la valeur de cette index à 0
            p += 1  # Ajoute 1 point à la variable <p> pour la note
            del corrige[-1] # Supprime le dernier élément de <corrige> car le mot demandé à bien été traduit
        else:       # Sinon (si la traduction saisie est fausse)
            list3[index] += 6   # Ajouter à lindex de la liste des point faibles <list3> 6 points de difficulté
            corrige.append(juste)   # Ajoute le mot juste à la liste <corrige>
            if reponse:     # Si la traduction saisie contient au moins 1 caractère (!=vide)
                corrige.append(reponse)     # Ajouter à la lsite <corrige> la réponse fausse saisie <reponse>
            else:   # Sinon (si la réponse est vide)
                corrige.append('<vide>')    # Informe que la réponse était vide
        # Supprime l'index <r> de la lsite <fr> pour ne pas que la fonction randint() ressorte le même index
        del fr[r]   # Supprime l'index <r> de la liste <fr>
        del et[r]   # Supprime l'index <r> de la liste <et>
    score = round(p/N*base)     # Convertie le score sur la base définie
    print("\nFin du contrôle ", score, '/', base, sep='')   # Affiche le score sur la <base> (ex: 10/20)
    if p != N:  # Si Il y a eu au moins 1 fautes
        reponse = input("Voulez voir le corrigé ? (Y/n) : ")    # Demande pour afficher le corriger
        if reponse in ['Y', 'y']:  # Si l'utilisateur valide la demande
            for i in range(N-p):     # Pour i allant de 0 à N-p (= nombre de fautes)
                # Affiche Le mot suivi de sa tradution et la mauvaise tradution répondue
                # Pour afficher ces 3 éléments de la liste <corriger>
                # L'index i de la boucle for est multiplié par 3 puis il y est additionné par l'entier (1 ou 2) pour acccéder à l'élément voulu
                print(i+1, '/', N-p, " La traduction de <",corrige[i*3], "> est <", corrige[i*3+1], "> (≠", corrige[i*3+2], ")", sep='', end='')
                input()     # Attendre que l'utilisateur prenne connaissance de son erreur
            print()     # Saute une ligne
    # Enregistre le score dans la liste <note>
    note[0].append(score) # <note> étant un tableau global sa nouvelle valeur sera conservée à la sortie de la procédure
    now = datetime.now()
    note[1].append(now.strftime('%H:%M'))
    if p == N or reponse in ['Y', 'y']:   # Si il n'y a pas de corrigé ou à l'inverse si le corrigé à bien été lu
        # Pour ne pas avoir un retour trop brusque sur le menu
        input("Appuiez sur entrée pour revenir au menu...")

# Définie la procédure hard() avec les paramètres <list1>, <list2>, <list3> et <list4>
def hard(list1, list2, list3, list4):
    # Cette procédure est la plus complexe du fait de la difficulté à gérer les difficultés des mots individuellement
    # Après une analyse et triage de tous les points de difficultés de la liste <list3>
    # Un sous menu est lancé semblable au menu principale 
    # à la différenc prêt que les mots mis en arguments correspondent uniquement aus mots à point faible
    # Ici les points de déifficultés ne peuvent être modifiés
    # Il faut se rendre dans le menu principale et lancer un controle() pour réduire ces pointF  
    N = len(list1)      # Initialistion de la variable <int> <N> au nombre de mots contenues dans <list1>
    print("Bienvenue dans le mode POINT FAIBLE\n")    # Affiche un petit message de bienvenue
    # Initialisation du tableau <top> 
    # La première liste du tableau correspond à la copie de la <list3> contenant les pointF de chaque mot
    # La deuxième liste du tableau contient une suite arithmétique de raison 1 
    # Cette suite sert à garder l'index correspondant au mot une fois le tableau trier par les pointF de la 1ere liste
    top = [list3[:], [i for i in range(len(list3))]]    # Initialisation du tableau <int> <top>
    # La 2eme liste est égale à i. Or i correspond à la variable de la boucle pour i allant de 0 à longueur de <list3>
    # Donc la 2eme liste comprendra tout les entiers positifs de 0 à longueur de <list3>
    trier = True    # Initialisation de la variable <bool> <trier> à l'état True pour entrer dans la boucle while
    while trier:    # Tant que <trier> n'est pas égale à rien (!=0)
        trier = False   # Conjecturer que la liste 1 du tableau <top> est bien trier dans l'ordre décroissant des pointF
        for i in range(len(top[0])-1):      # Pour i allant de 0 au nombre de pointF -1
            if top[0][i] < top[0][i+1]:     # Si la valeur la plus grande dans l'intervalle [i;i+1] est à droite de la liste
                trier = True    # Affecter à <trier> l'état True pour continuer à trier
                for j in range(2):  # Répéter 2 fois
                    top[j][i], top[j][i+1] = top[j][i+1], top[j][i] # Inverser les valeurs i et i+1 de la 1ere et 2eme liste du tableau <top> 
    # Vérifie si la première liste de <top> contient que des 0
    if top[0].count(0) == len(top[0]):      # Si le nombre, par la fonction .count(), de 0 contenu dans la liste d'index 0 du tableau <top> est le même que la longueur de cette même liste
        print("Félicitation ! Vous n'avez aucune difficultée :)")   # Cela signifie qu'il n'y a aucun mot qui pose difficulté
        input("\nAppuyez sur entrée pour revenir au menu...")
    else:
        print("Ce mode analyse vos points faibles\nEt vous permet de vous concentrez sur vos difficultées\n")
        if 0 in top[0]: # Si il y a au moins un 0 dans la 1ère liste du tablau <top> 
            total = top[0].index(0) # Le nombre total de mot difficiles correspond au permier rang contenant un 0 (car la liste commence à l'index 0) 
        else:   # Si tout les mots ont des difficultés
            total = N   # <int> <total> est égale au nomre de mot <N>
        if total > 1:   # Si il y a plus d'un mot difficile
            print("Tu as", total, "difficultées sur", N, "mots\n")  # Afficher la proportion de difficulté sur le nombre total <N> de mot
        n = total   # copie de <total> dans la variable <n> qui correspond au nombre de mot à travailler
        if n > int(N/2):    # Si la proportion des mots mot à difficultés est supérieur que tout les mots / 2
            n = 0   # Reset <n> à 0
            pc = int(input("Quelle quantitée en % voulez vous trvailler ? : ")) # Convertie la saisie en <int>
            n = int(pc * total / 100)   # Produit en croix pour obtenir la quantité n de mot à travailler en fonction du % voulu du total des mots à travailler
            if n < 1:   # Si le produit en croix donne 0
                n = 1   # Forcer le nombre de mot à travailler à être supérieur à 0
            elif n > N:
                n = N
        # Ces 2 lignes suivantes sont très compressées et donc optimisées
        # Prenons l'exemple de <motFR>
        # La liste est initialiser depuis la liste <list1> qui contient TOUT les mots en français
        # Or nous ne voulons que les mots à travailler donc difficiles
        # Pour se faire seul les mots de <list1> dont leurs index correspondent aux valeurs de la 2eme liste du tableau <top> sont utilisés
        # Afin d'accéder à tout les index voulu, la boucle for est appellée
        # pour affecter chaque mot de <list1> d'index (valeur du 2eme tableau) i dans la liste <motFR>
        motFR = [list1[top[1][i]] for i in range(n)]    # Initialisation de <str> <motFR>
        motET = [list2[top[1][i]] for i in range(n)]    # Initialisation de <str> <motET>
        play = True     # Initialisation de la la variable <bool> à l'état True pour entrer dans la boucle while
        while play:     # Tant que play != 0
            if n == 1:  # Si il n'y a qu'un seul mot à travailler
                print("\nTa plus grande difficulté est : ")
            else:   # sinon (si il y a plus d'un mot à traivailler)
                print("\nTes mots les plus difficiles sont dans l'ordre décroissant : ")
            # Afficher les mots difficiles avec leurs points de difficultés, précédament trié dans l'ordre décroissant 
            for i in range(n):  # Pour i allant de 0 à <n> 
                print('<', list1[top[1][i]],'>(', top[0][i]/10, ')', sep='', end='  ')  # Affciher l'index i de la 1ère et 2eme liste du tableau <top>
            # Afficher le sous menu de la procédure hard()
            # Son fonctionnement est le même que le menu principal
            print("\n\nQue veux tu faire pour t'améliorer ? ")
            print("1. Apprendre")
            print("2. Reviser")
            print("3. Test")
            print("4. Quitter(Menu)")
            choix = input("Lancer le mode :") # Saisir le choix voulu
            print()     # Saute une ligne
            if choix == '1':
                # Appel de la procédure apprendre() avec comme arguments <motFR> et <motET>
                # Et non <list1> car on veut travailler que sur les mot à difficultés 
                apprendre(motFR, motET) 
            elif choix == '2':          
                reviser(motFR, motET, list4)    # Appel de la procédure reviser() avec comme arguments <motFR>, <motET> et <list4>
            elif choix == '3':
                test(motFR, motET, list4)   # Appel de la procédure test() avec comme arguments <motFR>, <motET> et <list4>
            elif choix == '4':
                play = False    # Sortir de la boucle while
            else:
                print("Choix inconnu, erreur...")

# Définie la procédure pendu() avec les paramètres <list1>, <list2> et <list3>
def pendu(list1, list2, list3):
    # Le jeu du pendu à été créer
    # pour se détendre entre deux séance de test() ou controle()
    # Il permet aussi de reviser l'écriture d'un mot
    # Le principe de jeux est simple
    # Après avoir choisi la langue du mot à trouver
    # Afficher le mot en cachant ses lettres par des '_' (sauf la première)
    # A chaque bonne lettre trouvée, remplacer '_' par la bonne lettre
    # A chaque mauvaise lettre, enlever un point de vie et afficher la potence
    def espace(mot):    # Définie la fonction espace() avec le paramètre <mot>
        # Retourne la chaine de caractère <mot> avec des espaces entre chaque caractères
        a = ''      # Initialise la variable <str> <a> à une chaine de caractère vide
        for i in mot:  # Pour i allant de 0 à longueur du paramètre
            a += i + ' '    # Ajouter par concaténation à <a> la lettre i du <mot> et un espace = ' '
        return a    # retourner la variable <a> 
    def check(lettre):      # Définie la fonction check() avec le paramètre <lettre>
        # Cette fonction vérifie si la lettre propsoer est dans la variable word
        # Si c'est le cas retourner False
        # Si la lettre proposer n'est pas dans la variable <str> word retourner True
        # Vérifie dans un premier temps
        # 1.Si la lettre est valide pour être comparer avec <word>
        # 2.Si la longueur est différente de 1 et différente de 'exit'
        if len(lettre) != 1 and lettre != 'exit':
            print('Erreur...')      # Afficher "Erreur"
            return 0        # Sortir de la fonction en retournant 0
        # Vérifie dans un second temps si la lettre n'a pas déjà été utilisée
        if lettre in use:   # Si la liste <use> contient la lettre
            print('Vous avez déjà utilisé cette lettre...')
            return 0    # Sortir de la fonction en retournant 0
        perdu = True    # Conjecture que la lettre n'est pas dans word
        # Si la lettre est valide, vérifier si elle appartient à <word>
        for i in range(len(find)):  # Pour i allant de 0 à la longueur de la lsite <find>
            # Si la lettre correspond à l'index i du mot à trouver <word>
            if lettre == word[i]:
                find[i] = lettre    # Affecter au rang i de <find> la <lettre>
                perdu = 0           # Sortir de la foncction en retournant False
                # Sinon si le mot <word> contient des accents (é, è,...)
                # et que la <lettre> est 'e'
                # alors si l'index i du mot à trouver <word> contient un des accents de la liste <checkE>
            elif accent == True and lettre == 'e' and (word[i] in checkE) == True:
                # Affecter au rang i de <find> la lettre d'index i du mot à trouver
                find[i] = word[i]
                perdu = 0   # Affecter à perdu False
        return perdu  # retourner la variable <bool> <perdu>

    def graph(vie, affiche):      # Définie la fonction graph() avec les paramètres <vie> et <affiche>
        # Cette profcédure affiche un "dessin" d'une potence dans le terminal avec des '#'
        # Définie la fonction l() pour 'ligne' avec les paramètre <ligne>, <mini> et <max>
        def l(ligne, mini, max):
            # Cette procédure affecte l'intervale [mini;max] de la liste d'index <ligne> du tableau <potence> des '#'
            while mini < max:   # Répéter jusqu'à que la variable <mini> soit égale à <max>
                # Affecter au rang <mini> de l'index <ligne> du tableau <potence> le caractère '#'
                potence[ligne][mini] = '#'
                mini += 1       # Incrémente 1 à la variable <int> <mini>

        # Définie la fonction c() pour colonne avec les paramètre <colonne>, <mini> et <max>
        def c(colonne, mini, max):
            # Cette procédure affecte l'intervale [mini;max] de la liste d'index <ligne> du tableau <potence> des '#'
            while mini < max:   # Répéter jusqu'à que la variable <mini> soit égale à <max>
                # Affecter au rang <mini> de l'index <colonne> du tableau <potence> le caractère '#'
                potence[mini][colonne] = '#'
                mini += 1   # Incrémente 1 à la variable <mini>
        # En fonction des vies restantes ajouter les différentes parties (poutre(verticales, horizontales), corde,...) de la potence
        if vie == 7:
            # 1ère poutre horizontal
            l(7, 0, 9)  # Apelle de la fonction l() avec 7, 0, 9 en arguments
        elif vie == 6:
            # 2eme poutre appartenant et perpendiculaire à la première
            c(3, 2, 7)  # Apelle de la fonction c() avec 3, 2, 7 en arguments
        elif vie == 5:
            # 3eme poutre parallèle à la première, passant par le segment de la 2eme poutre et perpendiculaire à cette dernière
            l(1, 3, 13)  # Apelle de la fonction l() avec 1, 3, 13 en arguments
        elif vie == 4:
            # Bout de bois de maintien dans le coin de la 3eme et 2eme poutre
            # Affecter à l'index 4 du rang 3 du tableau <potence> le caractère '#'
            potence[3][4] = '#'
            # Affecter à l'index 6 du rang 2 du tableau <potence> le caractère '#'
            potence[2][6] = '#'
        elif vie == 3:
            # Corde
            # Affecter à l'index 12 du rangx 12 du tableau <potence> le caractère '|'
            potence[2][12] = '|'
        elif vie == 2:
            # Tête
            # Affecter à l'index 12 du rang 3 du tableau <potence> le caractère '0'
            potence[3][12] = '0'
        elif vie == 1:
            # Tronc du corps
            c(12, 4, 7)  # Apelle de la fonction c() avec 12, 4, 7 en arguments
        elif vie == 0:
            # Bras du corps
            l(4, 10, 15)    # Apelle de la fonction l() avec 4, 10, 15 en arguments
        # Si le parmamètre <bool> <affiche> est vrai alros afficher la potence
        if affiche == True:
            # Double boucle pour afficher le tableau à 2 dimenssions
            for i in range(8):
                for j in range(17):     # boucle pour j car i est déjà utilisé
                    print(potence[i][j], end='')
                print()  # Revenir à la ligne après chaque affichage d'une ligne

    def gagner(vie):    # Définie la fonction gagner() avec le paramètre <vie>
        # Cette fonction permet de vérifier si toutes les lettres ont été trouvées
        # Si c'est le cas la fonction renvoie -1
        # pour sortir de la boucle et ne pas passer par la condition <if vie == 0>
        # Si il reste des lettres introuvées la fonction renvoie la même vie reçu en paramètre
        for i in find:  # Pour i allant de la lettre d'index 0 du mot find à sa dernière
            if i == '_':    # Si la lettre est égale à une lettre pas encore trouvée
                return vie  # Renvoyer la vie actuelle
        return -1   # Si la boucle s'est fini (sans return) alors renvoyer -1

    # Programme principal
    vie = 8     # Initialise la variable <int> <vie> à 8
    # Conjecture que le mot n'a pas d'accent (é, è, ê,...)
    # Avec l'initialisation de la variable <bool> <accent>
    accent = False
    use = []        # Initialise la liste <str> <use> des mots utilisées
    potence = []    # Initialise le tableau (liste à 2 dimmensions) <str> <potence> pour afficher la potence
    print("Bienvenue dans le jeux du PENDU\nTapez 'exit' pour abandonner\n")
    # Demande dans quelle langue le mot à trouver doit être devinée
    # En fonction des index 0 et 1 de <list3>
    print("Vous voulez jouer en ",
          list3[0], '(1)/', list3[1], "(2) : ", sep='', end='')
    langue = input()    # Enregistre la réponse dans la variable <str> <langue>
    if langue == '1':   # Si la langue choisie est la première de <lit3>
        # Affecter à <word> un mot aléatoire de tout les mots de la liste <list1>
        word = list1[randint(0, len(list1)-1)]
    else:   # Sinon
        # Affecter à word un mot aléatoire de la liste <list2>
        word = list2[randint(0, len(list2)-1)]
    # Initialiser la liste <checkE> correspondant aus accents de la lettre 'e'
    checkE = ['é', 'è', 'ê', 'ë']
    # Initialisation du mot à trouver <find> par une liste <str> contenant des caracrtères underscore = '_'
    # fois la longueur du mot à trouver <word>
    find = ['_']*len(word)
    # Analyse du mot <word> afin de trouver si :
    # 1.Il comporte des 'e' avec accent
    # 2.Il comporte des caractères spéciaux (comme un tiret ou une apostrophe)
    #      qui devront être directements visibles dans le mot caché <find>
    #      Car ce n'est pas un lettre à trouver !
    for i in range(len(word)):  # Pour i allant de 0 à la longueur de <word>
        if word[i] in checkE:   # Si la lettre i de <word> appartient à la liste <checkE>
            accent = True       # Affecter à accent l'état True
        elif word[i] == "'":    # sinon si le ieme caractère de <word> est égale à "'" 
            # Remplacer la valeur i de <find> par le même caractère i de <word>
            find[i] = "'"
        elif word[i] == '-':    # Sinon si l'index i de <word> contient un autre caractère spécial
            # Rempalcer la valeur i de <find> par ce même caractère.
            find[i] = '-'
    # Initialisation du tableau 17x8 <potence> pour afficher graphiquement la potence et le pendu
    for i in range(8):  # Pour i allant de 0 à 8
        # Ajouter à la liste <potence>, une liste vide de 17 espaces ' '
        potence.append([' ']*17)
    # Afficher la première lettre du mot <word> dans la liste <find>
    find[0] = word[0]

    # Boucle principale du jeu pendu()
    # Tant qu'il reste de la vie ou que le mot est trouvé (vie=-1)
    while vie > 0:
        # Affciher le mot à trouver <find> avec la fonction espace()
        print(espace(find))
        # Demande de saisie d'une lettre dans la variable <str> <lettre>
        lettre = input("Entrez une lettre : ")
        # Vérifie si la lettre est juste avec l'appelle de la fonction check()
        # L'appelle de cette fonction se fait avec l'argument <lettre>
        # La fonction retourne soit True pour "la lettre est juste"
        # La fonction retourne False pour "la lettre ne correspond pas au mot <word>"
        if check(lettre):   # Si la fonction retourne False
            vie -= 1        # Retirer une vie à la variable <vie>
            use.append(lettre)  # Ajoute la lettre saisie dans la liste <use>
        if lettre == 'exit':    # Si la variable <lettre> contient la demande 'exit'
            # Passer une par une les vies jusq'à 0
            # Tout en appelant la procédure graph() sans aficher la potence 
            # Pour affciher par la suite la potence en entier
            for i in range(vie):    # Pour i allant de 0 à <vie>
                graph(vie, False)   # Appelle de la procédure graph() avec comme arguments <vie> et 0
                vie -= 1        # Enlever 1 vie à la variable <vie>
        graph(vie, True)    # Afficher la potence grâce à l'argument True de la procédure graph()
        vie = gagner(vie)   # Envoie en argument <vie> à la fonction gagner() qui revoie la nouvelle valeur de <vie>
    if vie == 0:    # Si <vie> est nulle alors le mot n'a pas été trouver par manque de vie
        print('\nPERDU\nLe mot était <', word, '>', sep='') # Afficher la bonne réponse
    else:   # Sinon si <vie> = -1 cela signifie que le mot à été trouvé
        print(espace(word))     # Affiche le mot <word> avec la fonction espace()
        print('\nFELICITATION !')   # Affiche la récompense de l'utilisateur
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin du jeu pendu\nAppuiez sur entrée pour revenir au menu...")

# Définie la procédure parametre() avec les paramètres <list1>, <list2>, <list3> <list4> et <list5>
def parametre(list1, list2, list3, list4, list5, list6):
    # Cette procédure permet 3 actions:
    # 1. Ajouter des mots, afin de na pas à avoir le faire depuis un éditeur texte en dehors du progrmame
    # 2. Reset les point faibles, si par exemple une autre personne veut apprendre les mots
    # 3. Changer la base de note, si une note sur 10 ne vous convient pas vous pouvez la changer sur n'importe quelle autre base dans l'intervale [1; +infini[
    #    Pour ne pas a avoir à changer la base à chaque redémarrage du programme, cette valeur est sauvegardée dans le fichier score.txt
    global base   # Définie la variable <base> comme global car elle va être modifiée
    def setBase():
        global base   # Redéfinie la variable <base> comme global car dans chaque fonction les varaibles sont prioritairements local
        # Cette procédure change la base de la note pour les procédures test() et controle() ainsi que l'enregistrement du meilleur score
        # de la partie dans le fichier score.txt Or si la base change la note du meilleur score change aussi !
        # Il faut donc reconvertir avec les produits en croix la note pour qu'elle corresponde avec la nouvelle base (ex : 5/10 -> 10/20)
        print("La base actuelle est de <note/", base, ">", sep='')  # Affiche la base actuelle avec la variable global <base>
        newBase = 0   # Pour rentrer dans la boucle while
        while newBase <= 0:     # Tant que la nouvelle base ne corresponde pas aux critères de validités
            newBase = int(input("Entrez votre nouvelle base : "))   # Saisir la nouvelle base dans <str> <newBase>
            if newBase <= 0:   # Si la base est négative ou nulle
                print("La base doit être positive !")
        for i in range(len(list5[0])):   # Pour i allant de 0 au nombre de note compris dans la liste d'index 0 du tablau note
            list5[0][i] = round(list5[0][i] / base * newBase)     # Convertir la note de <list5> en fonction de la nouvelle base
        for i in range(len(list6[0])):
            list6[0][i] = round(list6[0][i] / base * newBase)     # Convertir la note de <list6> en fonction de la nouvelle base
        base = newBase  # Affecter à la variable global <base>, la variable local <newBase>
    def reset():
        # Ce reset est déconsillé d'être effectué car il ne sera plus possible de connaître ses plus grosses difficultées
        # C'est pourquoi une demande de confirmation est demandée pour continuer
        if input("Cette commande est irréverssible ! Poursuivre ? (Y/n) : ") in  ['Y', 'y']:    # Si l'avertissement est accepté 
            # Affecter à tout les index de <list3> la valeur 0
            for i in range(len(list3)): # Pour i allant de 0 au nombre de valeur de <list3>
                list3[i] = 0    # Affecter à l'index i de <list3> la valeur 0
    def add():
        # Pour ajouter des mots, 3 listes doivent être affectées : <list1>, <list2> et <list3>
        # Il n'y pas plus à faire, et ces mots seront bien enregistrés dans le fichier mot.txt lors de la fermeture du programme
        print("Pour ajouter des mots suivez les instructions !")
        ajout = True    # Initialise la variable <bool> <ajout> à True pour entrer dans la boucle while
        while ajout:    # Tant que ajout != 0
            print("Entrez le mot", list4[0], ': ', end='')  # Demande le premier mot dans la langue de l'élément 0 de <list4>
            # Ajoute le mot saisie par input() dans la liste <list1> qui est un paramètre par adresse
            # Donc la liste mise en argument lors de l'appelle de la procédure sera bien affectée
            list1.append(input())   # Ajoute le mot saisie dans <list1>
            print("Entrez sa traduction en", list4[1], ': ', end='')    # Demande la traduction du mot dans la langue de l'élément 1 de <list4>
            list2.append(input())   # Ajoute la traduction saisie dans <list2>
            list3.append(0)     # Ajoute 0 dans la liste <list3> (pour 0 point de difficulté pour la nouvelle paire de mot)
            if not input("Encore un autre ? (Y/n) : ") in ['Y','y']:  # Si la réponse ne correspond pas au 'Y' de Yes, quitter la boucle
                ajout = False   # Affecter à <ajout> la valeur 0 pour quitter la boucle while
    print("Bienvenue dans le menu PARAMETRE !")
    play = True     # Initialise la variable <bool> <play> à True pour entrer dans la boucle while
    while play:     # Tant que play != 0
        # Affiche le sous menu
        print("\nQue souhaitez vous faire ?")
        print("1. Ajouter des mots")
        print("2. Reset points faibles")
        print("3. Changer base note")
        print("4. Quitter(menu)")
        # Saisir le choix 1, 2, 3 ou 4
        choix = input("Executer le paramètre : ")
        print()  # Saute une ligne
        if choix == '1':    # Si le choix est égale à '1'
            add()   # Appelle de la procédure add() sans argument
        elif choix == '2':      # Si le choix est 'Reset les pointF'
            reset()   # Appelle de la procédure reset() sans argument
        elif choix == '3':  # Si le choix est centré sur la modification de la base pour les notes ()
            setBase()   # Appelle de la procédure setBase() sans argument
        elif choix == '4':  # Si le choix signifie 'Sortir du sous menu pour retourner au menu principal'
            play = False    # Affecter à <play> la valeur 0 pour quitter la boucle while
        else:   # Si aucune des condition ne correspondent au choix
            print("Choix inconnu, erreur...")   # Informer que le choix n'existe pas
        # Pour ne pas avoir un retour trop brusque sur le menu
        # Mais uniqement si l'utilisateur sort d'une procédure
        if choix in ['1', '2', '3']:  # Si la variable <str> <choix> appartient à la liste des choix correspondants à une procédure  
            input("\nLa commande s'est terminée avec succès !\nAppuiez sur entrée pour revenir au menu...")   # Bloque le programme jusq'à une action de l'utilisateur

# Définie la procédure save() avec les paramètres <list1>, <list2>, <list3> et <var>
def graphique(list1, list2, list3, var):
    # Cette procédure, grâce au module 'turtle' afficher un graphique sur un repère x, y 
    # Les ordonnées représentent la note sur 20 en fonction du temps (absisses) qui précisons, n'est pas à l'échelle 
    # On peut afficher 2 catégories de note différentes!
    #   - Les dernières notes actuelles du tableau <note> 
    #     C'est à dire les notes produites par controle(), depuis l'ouverture du programme
    #   - Toutes les meilleures notes du fichier score.txt
    # Avant de débuté le graphique il faut avoir convertie les notes sur une base de 20
    def s(x, y):
        # Afin de ne pas écrire à chaque fois la même longue procédure
        t.goto(t.xcor()+x, t.ycor()+y)      # Ajoute à x et y la valeur en plus ou en moins voulu 
    def fleche():
        # Trace une flèche au bout du repère
        t.right(135)    # Tourne à droite de 135 degrés
        t.down()    # Pose le stylo
        t.forward(9)    # Avance de 9
        t.up()  # Lève le stylo
        t.backward(9)   # Recule de 9
        t.left(270) # Tourne à gauche de 270 degrés
        t.down()    # Pose le stylo
        t.forward(9)    # Avance de 9
        t.up()      # Lève le stylo
        t.backward(9)   # Recule de 9
        t.right(135)    # Tourne de 135 degrés
    def ecrire(str, x, y, taille):
        # Ecrit la chaine de caractère voulu en se déplacant de <x> ou <y> et avec une <taille> de police
        t.up()  # Lève le stylo
        s(x, y) # Se déplace de x et y
        t.write(str, font=("Arial", taille, "normal"))   # Ecrit la chaine de caractère <str> avec la police Arial en taille 9
        s(-x, -y)   # Revient sur les coordonnées précédentes 
    def point():
        #Trace un gros point en bleu à chque valeur d'une note
        t.width(9)  # Règle l'épaisseur du stylo à 9
        t.color(colorPoint) # Règle la couleur du stylo
        s(0, 0)     # Fait semblant davancer pour que le stylo "imprime"
        t.width(4)  # Remet l'épaisseur su stylo à 4
        t.color(colorCourbe)  # Remet la couleur du stylo comme avant

    # Programme principale 
    print("Bienvenue dans le mode GRAPHIQUE")
    print("\nVous voulez afficher : ")
    print("1. Vos dernières notes de cette séance")
    print("2. Vos meilleures notes du fichier score.txt")
    choix = input("Votre choix : ")
    total = 0   # Initialise la variable <total> pour le calcule de la moyenne
    if choix == '1':
        noteGraph = list2[0][:]     # Copie la liste <list2> dans <noteGraph> SANS ADRESSE !
        tempsGraph = list2[1][:]     # Affecte à <tempsGraph> toutes les heures aux quelles controle() à été appelée
        for i in list2[0]:   # Calcule le total des note de la liste <list2>
            total += i      # Incrémente l'index i de <list2[0]> à <total>
        n = len(list2[0])    # Initialise <n> au nombre de note dans <list2[0]>
    else:   # Si choix == '2'
        noteGraph = list3[0][:]     # Copie la liste <list3> dans <noteGraph> SANS ADRESSE !
        tempsGraph = []         # Initialsiation de la liste <tempsGraph>
        for i in list3[1]:      # Analyse de toutes les notes de <list3>
            temp = i.split('/')    # Sépare la chaine de caractère i 
            tempsGraph.append(temp[0][3:]+'/'+temp[1])      # Affecte à <tempsGraph> toutes la date jour/mois de la variable temp
        for i in list3[0]:   # Calcule le total des note de la liste <list3>
            total += i      # Incrémente l'index i de <list3[0]> à <total>
        n = len(list3[0])    # Initialise <n> au nombre de note dans <list3[0]>
    if len(noteGraph) < 2:  # Si la quantité de note empêche la création d'un graphique
        print("\nIl n'y a pas assez de notes...\n")
    else:   # Si il y a assez de notes
        moyenne = round((total/var*20)/n) # Calcule la moyenne et affecte le résultat à <moyenne>
        if var != 20:     # Si la <var> est déjà à 20 il est inutile de convertir les notes avec une base 20...
            for i in range(len(noteGraph)): # Affecte à chaque index de <noteGraph>
                noteGraph[i] = round(noteGraph[i]/var*20)    # La note convertie sur une base de 20
        print("\nOuverture de la fenêtre turtle.py...", end='')
        try:    # Essaye
            # Si la fenêtre s'est déjà fermé, une erreur se produit lors de la re ouverture
            # Mais si on execute une deuxième fois la commande, alors le module fonctionne à nouveau
            t.reset()
        except:
            print("ERREUR !\n2eme tentative d'ouverture...", end='')
        ############################
        x = 550     # Dimenssion global X
        y = 500     # Dimenssion global Y
        ############################
        xDec = -300  # Recule dans les négatif de x par rapport à x=0
        yDec = -240  # Descente dans les négatif de y par rapport à y=0
        dec = 30     # Décalage entre le bout du repère et le bout de la courbe
        miniDec = 4  # Pour ne pas que le dégradé touche l'axe y
        colorRepere = '#4261CA'     # Bleu clair
        colorCourbe = '#9D2fF5'     # Violet 
        colorPoint = '#D287D6'      # Violet clair
        colorMoyenne = '#F34141'    # Rouge clair
        # Initialisation de la liste <degrader> comportant un dégarder du rauge --> vert en #hexadécimal
        # Chaque index correspond à une couleur décomposer en RGB
        # Par exemple #FD 0D 01
        #             253 13  1
        #              R  G   B
        # La couleur R=red=rouge étant dominante on obtient du rouge
        colorDegrader = ['#FD0D01', '#FB2803', '#F94205', '#F85F06', '#F67708', '#F48F0A', '#F2A90C', '#F0BF0E', '#EFD50F', '#EDED11', '#D6EB13', '#BEE915', '#A5E816', '#90E618', '#78E41A', '#64E21C', '#52E01E', '#3CDF1F', '#2ADD21', '#23DB2C']
        t.reset()   # Remet tout les réglage à 0 et ouvre une fenêtre si ce n'est pas le cas
        t.bgcolor("black")  #Règle la couleur de l'arrière plan à noir
        t.color(colorRepere) # Règle la couleur du stylo à bleu
        t.speed(0)  # Règle la vitesse de déplacement à 4
        t.width(5)  # Règle l'épasseur du stylo à 3
        t.ht()      # Cache le stylo
        t.up()      # Relève le stylo
        # Affiche axe x et y
        print("OK !\nConsruction du repère x, y...", end='')
        s(xDec, yDec)       # Se place à l'origine du repère [0;0]
        t.down()      # Pose le stylo
        s(0, y)       # Trace l'axe des ordonnées y
        t.left(90)    # Pour tracer la flèche dans le bon sens
        ecrire("NOTE", -13, 2, 10)  # Notation de l'axe y
        fleche()    # ajout d'une fleche sur le bout de l'axe y
        s(0, -y)    # Retour à l'origine
        t.down()    # Pose le stylo
        s(x, 0)     # Trace l'axe des abscisses x
        ecrire("TEMPS", 6, -7, 10)   # Notation de l'axe x
        t.right(90)   # Pour tracer la flèche dans le bon sens
        fleche()      # ajout d'une fleche sur le bout de l'axe x
        s(-x, 0)      # Retour à l'origine
        # Construction lignes dégrdées
        print("OK !\nConstruction de l'échelle en ordonnée...", end='')
        t.width(4)    # affine l'épaisseur du stylo
        s(miniDec, 0)     # Se décale un peu vers la droite
        for i in range(20):     # Trace 20 lignes en partant de 0
            t.color(colorRepere)     # Règle la couleur 
            if i % 2 == 0:      # Si i est pas divisible par 2
                if i < 10:       # Si i n'a pas encore atteint la dizaine
                    ecrire(str(i), -17, -7, 10)  # Ecrit l'échelle (rapproché de l'axe y)
                else:   # Si la division de i par 2 possède un reste
                    ecrire(str(i), -24, -7, 10)  # Ecrit l'échelle (éloigné de l'axe y)
            t.up()  # Lève le stylo
            s(0, (y-dec)/20)     # Monte de quelques ordonnées sur l'axe y
            t.color(colorDegrader[i])   # Règle la couleur à la couleur hexadécimal du rang i de <degrader>
            t.down()    # Pose le stylo
            s(x-dec-miniDec, 0) # Trace la ligne
            t.up()  # Lève le stylo
            s(-(x-dec-miniDec), 0)  # Reviens sur l'axe des ordonnées
        t.color(colorRepere)     # Règle la couleur 
        ecrire('20', -23, -7, 10) # Ecrit l'échelle : 20
        t.up()  # Lève le stylo
        s(-miniDec, 0)    # Se recolle àl'axe y
        s(0, -(y-dec))  # Se place sur l'origine
        # Construction échelle temps + Initialisation graphique
        if len(noteGraph) > 30:     # Si le nombre de note est trop grand
            noteGraph = noteGraph[-30:]     # Garder uniquement les 30 dernières notes
        xStep = (x-dec)/(len(noteGraph)-1)  # Règle l'additionneur des absisses 
        yStep = (y-dec)/20  # Règle le multiplicateur des ordonnées
        print("OK !\nConstruction de l'échelle en abscisse...", end='')
        if len(tempsGraph) > 30:     # Si le nombre de note est trop grand
            tempsGraph = tempsGraph[-30:]     # Garder uniquement les 30 dernières dates
        t.up()  # Lève le stylo
        for i in range(len(tempsGraph)):    # Ecrire le nombre de date ou heure dans la lsite <tempsGraph>
            # Si il y a trop de valeur
            # Alterner dans les y (une fois sur 2 aller un peu plus bas lors de l'écriture)
            if len(tempsGraph) > 15 and i % 2:          # Si la division par 2 donen un reste (pour i = 1, 3, 5,...)
                ecrire(tempsGraph[i], -14, -35, 10)         # Ecrire la date ou heure en allant plus en dessous de l'axe des absisses
            else:
                ecrire(tempsGraph[i], -14, -20, 10)     # Ecrire la date ou heure en allant au plus proche de l'axe des absisses
            s(xStep, 0)     # Avance de quelques x 
        # Initialisation graphique
        t.color(colorCourbe)  # Règle la couleur
        s(-(xStep*len(tempsGraph)), 0)      # Retourne à l'origine [0;0]
        s(0, (noteGraph[0]*(y-dec)/20))     # Monte en y en fonction de la grandeur de la 1ere note de <noteGraph>
        t.down()    # Pose le stylo
        point()     # Trace un point
        t.width(4)  # Règle l'épaisseur u stylo à 4
        t.speed('slowest') # Change la vitesse à lent
        print("OK !\nConstruction de la courbe...", end='')
        # Trace le graphique
        for i in range(1, len(noteGraph)):  # Pour i allant de 0 à la dernière note de <noteGraph>
            t.goto(t.xcor() + xStep, noteGraph[i]*yStep+yDec)  # Avance de xStep et se place sur les ordonnées en fonction de la note
            point()     # Trace un point
        print("OK !\n")
        t.speed(0)  # Vitesse au maximum
        t.up()      # Relève le stylo
        t.color(colorMoyenne)   # Change la couleur
        t.goto(-150, 248)       # Se déplace à un point précis
        ecrire(("MOYENNE = " + str(moyenne) + "/20"), 0, 0, 20)     # Ecrit la moyenne du grpahique de note
    input('Appuiez sur entrée pour revenir au menu...')
    #print("Ne fermez pas la fenêtre turtle.py merci :)")
    if len(noteGraph) > 1:
        t.bye()     # Ferme la fenêtre 
    
# Définie la procédure save() avec les paramètres <list1>, <list2>, <list3>, <list4>, <list5> <list6> et <var>
def save(list1, list2, list3, list4, list5, list6, var):
    # Cette procédure est déstiné à sauvegarder toutes les valeurs de variables ou listes dans des fichiers textes
    def arrondie(float):
        # Cette fonction arrondie() sert à renvoyer un arrondie d'un float à une décimale uniquement
        # Dans la ligne suivante :
        # 1.Multiplie le paramètre <float> par 10
        # 2.Convertie le produit <float> en <int> 
        # 3.Convertie la variable <int> en <str>
        # 4.Récupère le dernier caractère de la variable <str> (il correspond donc à la décimale)
        # 5.Convertie ce caractère <str> en <int>
        # 6.Affecte la valeur obtenue à <int> <dec> pour décimale
        dec = int(str(int(float*10))[-1])   # Récupère LA décimale du paramètre <flaot> dans un entier <int> <dec>
        if dec < 5:     # Si la décimale du paramètre est strictement inférieur à 5
            return int(float)   # L'arrondie correspond à son entier inférieur
        else:           # Si la décimale du paramètre est suérieur ou égale à 5
            return int(float)+1 # L'arrondie correspond à son entier supérieur
    # Premier enregistrement des listes dans le fichier mot.txt
    # Ouverture du fichier "mot.txt" en lecture  
    # avec l'encodage Universal Character Set Transformation Format - 8 bits (=Utf-8)
    f = open("mot.txt", 'r', encoding='Utf-8')
    saveFirst = []  # Enregeistre les thèmes avant celui recherché
    find = '['+langue[2]+'] ['+langue[0]+'='+langue[1]+']\n' # Définie la ligne dans le fichier mot.txt à trouver 
    sortir = False  # Variable <bool> pour sortir de la boucle 
    for l in f:     # Lecture de tout le fichier texte
        if l == find:   # Si la ligne <l> est égale à la ligne recherché
            saveFirst.append(l)     # Enregistre la ligne theme + langue car elle ne change pas
            sortir = True   # Une fois tout les mots précédents le thèmes actuelle sauvegardés, on peut sortir de la boucle 
        if sortir == True:  # Il faut d'abord avoir trouvé le thème qui à été choisit avant de quitter
            if l == '\n':  # Il faut d'abord passé le thème qu'on va re écrire avec les listes !
                break   # Sortir de la boucle for 
        else:   # Si on n'a pas encore trouver la ligne recherchée
            saveFirst.append(l)     # Enregistre la ligne dans la liste <saveFirst>
    saveRest = f.readlines()    # Sauvegarder tout le reste du fichier texte à partir de la fin du thème recherché dans la liste <saveRest>
    f.close()   # Fermer le fichier mot.txt
    f = open("mot.txt", 'w', encoding='Utf-8')  # Ouverture du fichier mot.txt en écriture (écrase le fichier éxistant) avec l'encodage 'Utf-8
    for ligne in saveFirst:     # Ajout de la 1er sauvegarde non utilisée dans le programme
        f.write(ligne)      # Ecriture ligne par ligne ( car f.write(saveFirst) retourne une erreur, car write() ne peux que écrire du <str> pas une liste)
    # Ecriture de toutes les paires de mots avec leurs points de difficultés 
    # ligne par ligne : mot=saTradution.(pointDeDifficultés)
    for i in range(len(list1)):    #Pour i allant de 0 au nombre de mot total dans <list1> 
        f.write(list1[i] + '=' + list2[i] + '.('+str(arrondie((list3[i]+1)/10)) + ')\n')    # Enregistrement en écriture des 3 listes
    f.write('\n')   # Ecriture d'une ligne vide
    for ligne in saveRest:  # Ajout de la 2eme sauvegarde 
        f.write(ligne)  # Ecriture ligne par ligne
    f.close()   # Fermeture du fichier mot.txt
    bestIndex = 0       # Initialise <int> <bestIndex> pour sauvegarder l'index de la meilleur note de <list6>
    for i in range(len(list6[0])):  # Analyse tout les éléments de la liste de rang 0 du tableau <list6>
        if list6[0][i] > list6[0][bestIndex]:    # Si la note i de la liste du rang 0 du tableau <list6> est plus grand que l'index <bestIndex> de <list6>
            bestIndex = i   # Affecte à <bestIndex> i de la boucle for
    if len(list6[0]) > 0 and list6[0][bestIndex] > 0:     # Si la meilleur note est plus grande que 0/20
        now = datetime.now()    # now est une class contenant la date et l'heure actuelle de l'ordinateur
        list5[0].append(list6[0][bestIndex])     # Ajoute au tableau <list5> ma meilleur note
        list5[1].append("Le "+now.strftime('%d/%m/%y') + " à "+ note[1][bestIndex] + '\n')      # Ajoute au tableau <list5> al date de cette meilleure note
    moyenne = 0         # Initialise la variable <int> <moyenne> à 0
    if len(list5[0]) > 0:   # Si il y a au moins une note
        for i in list5[0]:  # Calcule la somme des notes
            moyenne += i    # Incrémente 1 à <i>
        moyenne = round(moyenne/len(list5[0]))      # Calcule la moyenne
    f = open(('score\SCORE ('+list4[2]+').txt'), 'w', encoding='Utf-8')    # Ouverture du fichier score.txt en écriture avec l'encodage 'Utf-8'
    f.write("###############\nBASE NOTE = "+str(var)+'\nMOYENNE = '+str(moyenne)+'/'+str(var)+'\n###############\n\n')      # Ecriture avec encadré de la nouvelle base
    for i in range(len(list5[0])):   # Pour i allant de 0 au nombre de note du fichier texte
        f.write(list5[1][i]+"La meilleure note était : "+str(list5[0][i])+'/'+str(base)+'\n\n')  # Ecriture du groupe de note (date, note, saut de ligne)
    f.close     # Fermeture du fichier score.txt

# Définie la fonction init() pour 'initialisation'
def init():
    # Cette fonction renvoie toutes les variables et listes du programme principale
    ################
    # FICHIER MOT  
    f = open("mot.txt", 'r', encoding='Utf-8')      # Ouverture en lecture du fichier mot.txt avec l'encodage 'Utf-8'
    fichier = f.readlines()     # Enregistre tout le fichier sous forme de liste dans <fichier>
    f.close()       # Ferme proprement le fichier mot.txt
    theme = []      # Initialise le tableau <theme> 
    for l in fichier:   # Lit chaque index de <fichier>
        if l != '\n':       # Si la valeur l de <fichier> n'est pas un saut de ligne '\n'
            if l[0] == '[':     # Si la première valeur de <l> est égale à '[' donc l'entête d'un thème et sa langue
                theme.append([])    # Ajoute une nouvelle liste à <theme>
                read = l.split(' ')     # Sépare la chaine de caractère de la valeur l de <fichier> par l'espace 
                temp = read[1].split('=')    # Sépare par '=' la chaine de caractère comportant les 2 langues, dans une liste <temp> 
                theme[-1].append(read[0][1:-1])    # Ajoute le theme dans le premier index de la dernière liste créé dans la liste <theme>
                theme[-1].append(temp[0][1:])      # Ajoute la langue1 dans la dernière liste créé dans la liste <theme>
                theme[-1].append(temp[1][:-2])     # Ajoute la langue2 dans la dernière liste créé dans la liste <theme>
            else:   # Ajoute tous les mots du theme
                l1, l = l.split('=')    # Affecte à <l1> la chaine de caractère de <l> jusq'au caractère '=' le reste de la liste est stocké dans <l>
                l2, l = l.split('.')    # Affecte à <l2> la chaine de caractère de <l> jusq'au caractère '.' le reste de la liste est stocké dans <l>
                l3, l = l.split('\n')   # Affecte à <l2> la chaine de caractère de <l> jusq'au caractère '\n' le reste de la liste est stocké dans <l>
                theme[-1].append(l1)    # Ajouter au dernier index de la liste <theme> le mot dans la langue1
                theme[-1].append(l2)    # Ajouter au dernier index de la liste <theme> la traduction dans la langue2
                theme[-1].append(l3)    # Ajouter au dernier index de la liste <theme> les points de difficultés du mot <l3>
    print("\nQuel thème voulez vous choisir ? :")
    for i in range(len(theme)):     # Affiche tout les thèmes disponibles
        # Chaque theme correspond à l'index 0 des listes dans la liste <theme>
        # On affiche aussi le nombre de mot dans chauqe theme :
        # Comme un 'mot' corresond au (mot) + (sa tradution) + (son point faible) il faut diviser le nombre total de valeur par 3
        # Avant cela ne pas oublier de soustraire 3 car on ne compte pas les 3 première valeurs correspondanttes au (theme) + (langue1) + (langue2)
        print(i+1, '. <', theme[i][0], '> [', theme[i][1],'=', theme[i][2],'] (', int((len(theme[i])-3)/3), 'mots)', sep='')
    lim = len(theme)+1  # la variable <lim> sert aussi bien à numéroter le mode 'créer' qu'à faire en sorte que le <choix> est dans l'intervale des choix discponibles
    print(lim, '. Créer un nouveau thème', sep='')  # Affcihe la dernière option après le nombre de thème
    choix = 100     # Pour rentrer dans la boucle while
    while choix > lim:   # Tant que le choix n'est pas conforme
        choix = int(input("\nVotre choix : "))  # Saisie la valaeur <choix> convertie en <int>
        if choix > lim:  # Si le numéro choisit n'est pas dans la liste proposée
            print("Impossible !")   # Affiche une erreur avant de recommencé 
    if choix == lim:    # Si le choix est égale au dernier qui est 'ajouter un thème'
        newTheme = input("Quel est le nom de votre nouveau thème ? :")     # Saisir le nouveau thème
        print("En 2 lettres, entrez la langue du thème")    # Demande d'entré la première langue
        l1 = input("(Ex : 'fr', 'de', 'en') : ").upper()     # la fonction .upper() retourne la chaine de caractère avec des majuscules
        print("En 2 lettres, entrez la langue de sa traduction")   # La 2eme langue pour la traduction
        l2 = input("(Ex : 'de', 'en', 'fr') : ").upper()    # la fonction .upper() retourne la chaine de caractère avec des majuscules
        f = open("mot.txt", 'a', encoding='Utf-8')      # Ouverture en écriture (ajout) du fichier mot.txt avec l'encodage 'Utf-8'
        f.write("["+ newTheme+ "] ["+ l1+ '='+ l2+ "]\n\n")   # Enregistre directement le nouveau thème dans le fichier mot.txt...
        theme.append([newTheme, l1, l2])    # ... Et comme la lecture de ce fichier à déjà été effectuée ajouter à <theme> le nouveau thème avec ses langues associées
    i = choix - 1   # Affecte à <i> la valeur de <choix> - 1 car une liste commence par l'index 0
    list1 = []      # Initialisation de la liste <list1> pour "mot"
    list2 = []      # Initialisation de la liste <list2> pour "traduction"
    list3 = []      # Initialisation de la liste <list3> pour "point faible"
    list4 = [theme[i][1],theme[i][2], theme[i][0]]  # Initialisation de la liste <list4>  pour "langue + theme"
    # Chaque 'mot' du theme choisit est regroupé en 3 valeurs
        # 1.Mot
        # 2.Traduction
        # 3.Point faibles
        # Ainsi pour analyser toutes les valeur en une boucle
        # On divise par 3 la longeur de la liste <theme[i]> 
        # Puis ensuite avec une fonction affine (j*3+k) on peut se déplacer dans le 'groupe' de 'mot'
    for j in range(1, int(len(theme[i])/3)):
        list1.append(theme[i][j*3])     # Premier index du groupe de 'mot'
        list2.append(theme[i][j*3+1])   # Deuxième index du groupe de 'mot'
        list3.append(theme[i][j*3+2])   # Troisième index du groupe de 'mot'
    # Enlève les parenthèses de chaque index i de <list3> et multiplie chaque valeur par 10 après les avoir converties en <int>
    list3 = [int(i[1:len(i)-1])*10 for i in list3]
    if not len(list3):  # Si le nombre de valeur dans <list3> ne renvoie PAS de valeur ce'ts à dire 0
        # Il faut absolument ajouter des mots de ce thème, sinon des erreurs de divisions se produiront dans test(), controle(),...
        # car comme il n'y a aucun mot, les procédures vont passer la boucle for (pour i allande de 0 à 0), puis afficher la note /base,
        # pour se faire il faut diviser par le nombre <n> de mot avant de multiplier par la <base>. 
        # Or ce <n> est égale à 0 et une division par 0 est impossible !
        input("\n/!\\ N'oubliez pas avant tout d'ajouter\ndes mots de ce thème dans les paramètres /!\\")  
    ###################
    # FICHIER SCORE
    try:
        f = open(('score\SCORE ('+list4[2]+').txt'), 'r', encoding='Utf-8')     # Ouverture en mode lectue avec l'encodage 'Utf-8' du fichier score.txt
    except:     # Si le fichier n'éxiste pas, en créé un nouveau
        f = open(('score\SCORE ('+list4[2]+').txt'), 'w', encoding='Utf-8')
        f.write("###############\nBASE NOTE = 20\nMOYENNE = 0/20\n###############\n\n")      # Ecriture avec encadré de la nouvelle base
        f.close()   # Fermeture du fichier pour le re ouvrir en...
        f = open(('score\SCORE ('+list4[2]+').txt'), 'r', encoding='Utf-8')     # Ouverture en mode lectue avec l'encodage 'Utf-8' du fichier score.txt
    base = ''   # Initialise la variable <str> <base> à rien
    f.readline()  # Avance d'une ligne dans le fichier texte
    read = f.readline()     # Lecture de la deuxième ligne du fichier
    for i in range(12, len(read)):  # Pour i allant du premier caractère de la valeur de la base jusq'à son dernier caractère
        base += read[i]     # Ajoute à base par concaténation le caractère i de <read>
    for i in range(3):
        f.readline()
    save = f.readlines()   # Enregistre tout le reste des lignes non lu dans la liste <save>
    f.close()   # Ferme le fichier
    list5 = [[], []]   # Initialisation de la liste <list5> pour enregistrer les date et heures de chaque scores enregistrés 
    # Chaque note est regroupé en 3 lignes
    # 1.Date de la note
    # 2.Note sur base
    # 3.Saut de ligne
    # Ainsi pour analyser toutes les notes en une boucle
    # On divise par 3 la longeur de la liste <save> 
    # Puis ensuite avec une fonction affine (i*3+k) on peut se déplacer dans le 'groupe' de la note
    for i in range(int(len(save)/3)):    # Pour i allant de la première note à la dernière
        read = ''   # Initialisation de <read> à une chaine de caractère vide
        for j in range(26, len(save[i*3+1])):   # Pour i allant du premier caractère de la note au dernier
            read += save[i*3+1][j]  # Concatenation de <temp> 
        # Affectation à <list5> la variable de <temp> séparée par le caractère '/'
        temp = read.split('/')    # Séparation de <temp> par le caractère '/' avec la fonction .split()
        list5[0].append(int(temp[0]))   # Ajoute à la liste <list5> la note de la ligne i du fichier 
        list5[1].append(save[i*3])  # Ajout de la date de la note dans la liste <list5>
    f.close     # Ferme le fichier settings.txt
    return list1, list2, list3, list4, list5, [[], []], int(base)      # Renvoie toutes les tableaux, listes, variables et valeurs demandé par l'appelle de la fonction init()

# PROGRAMME PRINCIPALE
from random import randint      # Importation de la fontion randint() du module random
from datetime import datetime   # Importation de la focntion datetime du module datetime
import turtle as t      # Importation du module turtle, on l'appelle avec t.fonction()
# Affiche un messsage de bienvenue
print("Bienvenue dans <LE Boss En Langue> !")
# Initialise toutes les listes et variables avec la fonction init()
motFR, motET, pointF, langue, noteSave, note, base  = init()
play = True  # Initialisation de la variable <bool> play à True pour pouvoir rentrer dans la boucle while
# Tant que play n'est pas pas vide
# On peut aussi écrire <play != 0>
# Mais cette condition est moins performante car elle oblige l'ordinateur à effectuer 2 opérations
# (comparer play à une autre donnée : 0, puis évaluer si le résultat est True ou False)
while play:
    # Affichage du menu principale
    print("\n####### MENU ########")
    print("## 1. Apprendre    ##")
    print("## 2. Reviser      ##")
    print("## 3. Test         ##")
    print("## 4. Contrôle     ##")
    print("## 5. Point faible ##")
    print("## 6. Pendu        ##")
    print("## 7. Paramètre    ##")
    print("## 8. Graphique    ##")
    print("## 9. Quitter      ##")
    print("#####################")
    # saisir le choix dans la variable <str> choix
    choix = input("Lancer le mode : ")
    print()         # saute une ligne
    # compare le choix à 8 conditions différentes en <str> (pour empêcher une erreur si un caractère est entré)
    if choix == '1':
        # Appel de la procédure apprendre() avec comme arguments motFR et motET
        apprendre(motFR, motET)
    elif choix == '2':
        # Appel de la procédure reviser() avec comme arguments motFR, motET et langue
        reviser(motFR, motET, langue)
    elif choix == '3':
        # Appel de la procédure test() avec comme arguments motFR, motET et langue
        test(motFR, motET, langue)
    elif choix == '4':
        # Appel de la procédure controle() avec comme arguments motFR, motET et pointF
        controle(motFR, motET, pointF)
    elif choix == '5':
        # Appel de la procédure hard() avec comme arguments motFR, motET, pointF et langue
        hard(motFR, motET, pointF, langue)
    elif choix == '6':
        # Appel de la procédure pendu() avec comme arguments motFR, motET et langue
        pendu(motFR, motET, langue)
    elif choix == '7':
        # Appel de la procédure parametre() avec comme arguments motFR, motET, pointF et langue
        parametre(motFR, motET, pointF, langue, note, noteSave)
    elif choix == '8':
        # Appel de la procédure graphique() avec comme arguments langue, noteSave, note et base
        graphique(langue, note, noteSave, base)
    elif choix == '9':
        play = False    # Affecte à play l'état False pour sortir de la boucle
    else:    # Si aucune des conditions ci dessus n'a été respectées alors
        # Informe que le choix saisie est invalide
        print("Choix inconnu, erreur...")
# Afficher "A bientôt" afin d'inciter le joueur à revenir
print("A bientôt !")
# Appel de la fonction save() avec comme arguments toutes les variables et listes
save(motFR, motET, pointF, langue, noteSave, note, base)
