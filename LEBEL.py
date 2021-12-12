####################################################################
# Copyright (C) 2019-2019 BADER Alexandre <alexandrebader3@gmail.com>
#
# This file is part of LEBEL.
#
# LEBEL can not be copied and/or distributed without the express
# permission of Alexandre
####################################################################

# Ce programme est la v4.0 du projet LEBEL
# Cette version est la 10eme et dernière de ce mini projet
# Débuté le 07/11/2019 fini le 14/11/19
# Par Alexandre BADER

# Définie la procédure apprendre() avec les paramètres <mot1> et  <mot2>
def apprendre(mot1, mot2):
    # Cette procédure permet d'apprendre
    # tout les mots en les affichants un par un
    print("Bienvenue dans le mode APPRENDRE")
    print("Une fois le mot mémorisé\nAppuyez sur entrée :)\n")
    for i in range(len(mot1)):    # Pour <i> allant de 0 au nombre de mot dans <mot1>
        # Affiche le mot d'index <i> de <mot1> ainsi que sa traduction de <mot2>
        # <sep> permet de modifier le caractère entre les chaines de caractères et les variables (defaut =' ')
        # <end> permet de modifier le caractère de fin de la procédure print() (defaut ='\n')
        print(i+1,'. ',mot1[i],' = ',mot2[i],sep='',end=' ')    
        input()    # Attend que l'utilisateur ai retenue les 2 mots
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin de l'apprentissage\nAppuiez sur entrée pour revenir au menu...")

# Définie la procédure reviser() avec les paramètres <mot1>, <mot2> et <langue>
def reviser(mot1, mot2, langue):
    # Cette procédure permet de réviser ses mots
    # avec un simple affichage du mot dans la langue choisie
    # Lorsque l'utilisateur à trouvé la traduction dans sa tête
    # il peut vérifier si cette dernière est juste en affichant la traduction correcte
    print("Bienvenue dans le mode REVISER\n")    # Affiche un petit message de bienvenue
    # Demande à l'utilisateur de choisir en quelle langue afficher les mots
    print("Vous voulez réviser en ",langue[0],'(1)/',langue[1],"(2) : ",sep='',end='')
    langue = input()    # Saisir la langue voulu par '1' ou '2'
    # <mot1> et <mot2> sont des adresses des listes misent en arguments lors de l'appelle de cette procédure
    # Afin de ne pas modifier les listes de mot <global> dans le programme principal
    # une "copie" des valeurs des 2 listes (par adresse) est effectuée
    # sur leurs intervalles complets [:] = [0:len(list)]
    # Ainsi si un mot de la liste est supprimé la liste mise en 
    # argument ne sera pas affectée (voir note de README.txt)
    m1, m2 = mot1[:], mot2[:]    # Copie des listes <str><mot1> et <str><mot2> dans <str><m1> et <str><m2>
    N = len(m1)    # Affecte à <int><N> la longeur de la liste <m1>
    for i in range(N):    # Pour <i> allant de 0 a <N>
         # Affecter à <int><r> un nombre aléatoire compris entre 0 et
         # len(m1)-1 pour ne pas dépasser l'index maximal des listes
        r = randint(0,len(m1)-1)
        if langue == '1':    # Si la langue désirée est la première
            # Affecter à <str><mot> le mot d'index <r> de <m1>(mot1) 
            # et à <str><trad> sa traduction qui est l'index <r> de <m2>(mot2)
            mot, trad = m1[r], m2[r]
        else:    # Si la langue choisit est la deuxième
            # Affecter à <str><mot> le mot d'index <r> de <m2>(mot2)
            # et à <str><trad> sa traduction qui est l'index <r> de <m1>(mot1)
            mot, trad = m2[r], m1[r]
        # Demande la traduction de la variable <mot>
        print(i+1,'/',N," La traduction de <",mot,"> est...",sep='', end='')
        input()      # Attend que l'utilisateur trouve la traduction dans sa tête
        print('>',trad,end='')  # Affiche la bonne traduction
        input()      # Attend que l'utilisateur appuie sur entrée pour passer au mot suivant
        del m1[r]    # Supprime le mot <m1> d'index <r> pour ne pas qu'il soit réutilisé
        del m2[r]    # Supprime le mot <m2> d'index <r> pour ne pas qu'il soit réutilisé
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin de la revision\nAppuiez sur entrée pour revenir au menu...")

# Définie la fonction test() avec les paramètres <mot1>, <mot2> et <langue>
def test(mot1, mot2, langue):
    # Cette procédure permet de tester ses connaissaces
    # sans que la note n'est d'impacte sur le fichier score.txt ou la variable <pointF>
    # Le test est semblable à reviser() à la différence que la traduction doit être écrite
    # Puis une condition vérifie si cette réponse correspond à la tradcution
    # Si, ce n'est pas le cas afficher directement la bonne réponse
    global base    # Informe à Python que la variable base peut être utiliser partout dans le programme
    m1, m2 = mot1[:], mot2[:]     # Copie des listes <mot1> et <mot2> dans <str><m1> et <str><m2>
    N = len(m1)  # Initialisation de <int><N> à la longeur de <m1>
    p = 0          # Initialisation de <int><p> pour 'point' à 0
    print("Bienvenue dans le mode TEST\n")    # Affiche un petit message de bienvenue
    # Demande à l'utilisateur de choisir en quelle langue afficher les mots
    print("Vous voulez réviser en ",langue[0],'(1)/',langue[1],"(2) : ",sep='',end='')
    langue = input()    # Saisir la langue voulu
    for i in range(N):    # Pour i allant de 0 à <N>
        r = randint(0, len(m1)-1)    # Affecte à <int><r> un entier aléatoire entre 0 et N-1
        if langue == '1':    # Si la langue désirée est la première 
            # Affecter à <str><mot> le mot d'index <r> de <m1>
            # et à <str><trad> sa traduction qui est l'index <r> de <m2>
            mot, juste = m1[r], m2[r]
        else:
            # Affecter à <str><mot> le mot d'index <r> de <m2>
            # et à <str><trad> sa traduction qui est l'index <r> de <m1>
            mot, juste = m2[r], m1[r]
        # Demande la tradcution de <mot>
        print(i+1,'/',N," Donne moi la traduction de <",mot,'> : ',sep='',end='')
        reponse = input()     # Enregistre la réponse dans la variable <str><reponse>
        if reponse == juste:  # Si la réponse est identique à la bonne traduction
            print(">BRAVO !") # Féliciter le joueur
            p += 1    # Incrémenter 1 à la variable <p>
        else:
            print("> FAUX, la réponse était <",juste,'>',sep='')    # Affiche la bonne traduction
        # Supprime l'index <r> des listes <m1> et <m2> pour ne pas que la fonction randint() ressorte le même index
        del m1[r]       # Supprime l'index <r> de la liste <m1>
        del m2[r]       # Supprime l'index <r> de la liste <m2>
    # Affiche la note sur le nombre total de mots et une autre note sur <base>
    print("\nFin du test ", p, "/", N, ' (', round(p/N*base), '/', base, ')', sep='')
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("Appuiez sur entrée pour revenir au menu...")

# Définie la procédure controle() avec les paramètres <mot1>, <mot2> <faible> et <add>
def controle(mot1, mot2, note, faible, add):
    # Cette procédure est la plus avancée dans l'apprentissage des mots
    # Chaque bonne et mauvaise réponse a un impacte sur la liste <pointF>(faible)
    # Les fautes de chaques mots sont enregistrées dans une liste pour la fin du contrôle 
    global base     # Déclaration de <base> en global, sa modification sera donc enregistrée en dehors de la procédure
    N = len(mot1)   # Initialisation de la variable <int><N> à la longueur de <mot1>
    print("Bienvenue dans le mode CONTROLE\n")    # Affiche un petit message de bienvenue
    m1, m2 = mot1[:], mot2[:]     # Copie des listes <mot1> et <mot2> dans les nouvelles listes <str><m1> et <str><m2>
    p = 0  # Nomre de point <int><p> pour chaque réponse juste
    # La liste <corrige> contiendra les corrections des traductions non correctes
    corrige = []    # Initialisation de la list <str><corrige>
    for i in range(N):    # Pour <i> allant de 0 à <N>
        r = randint(0, len(m1)-1)    # Choisi un rang <r> entre 0 et la longeur de <m1>-1
        if randint(0, 1):    # La probabilité de traduire un mot en langue1 est de 50%
            # Affecte les mots du rang <r> des listes <m1> et <m2> dans les variables, de types string, <mot> et <juste>
            mot, juste = m1[r], m2[r]
            corrige.append(mot)    # Ajoute à la liste <corrige> le mot à traduire <mot>
             # Affecte à la variable <int><index> l'index <i> du mot <juste> de la liste <mot2>
             # grâce la fonction .index() qui retourne l'index de la valeur recherchée dans la liste demandée
            index = mot2.index(juste)
        else:    # La probabilité de traduire un mot en langue2 est de 50%
            # Affecte les mots du rang <r> des listes <m2> et <m1> dans les variables, de types string, <mot> et <juste>
            mot, juste = m2[r], m1[r]
            corrige.append(mot)    # Ajoute à la liste <corrige> le mot à traduire <mot>
            index = mot1.index(juste)    # Affecte à la variable <int><index> l'index <i> du mot <juste> de la liste <mot1>
        # Affiche le mot à traduire <mot> en précisant combien il en reste en affichant sur <N> la variable local <i>
        print(i+1,'/',N,' <',mot,sep='',end='> : ')
        reponse = input()   # Saisir la tradution dans la variable <str><reponse>
        if reponse == juste:    # Si la réponse correspond bien à la bonne tradution
            # Script pour gérer les point faibles du mot actuelle
            if faible[index] > 0:    # Si le mot actuelle est une difficulté
                # Enlever à l'index <index> de la liste <faible> n points de difficultés
                # de l'index [1][1] du tableau <add> pour avoir eu juste
                faible[index] += add[1]   # Incrémentaion à l'index <index> de la liste <faible>
                if faible[index] < 0:    # Si la nouvelle valeur de l'index <index> de la liste <faible> est négative
                    faible[index] = 0    # Remettre la valeur de cette index à 0
            p += 1  # Incrémente 1 point à la variable <p> pour la note
            del corrige[-1] # Supprime le dernier élément de <corrige> car le mot demandé a bien été traduit
        else:    # Sinon (si la traduction saisie est fausse)
            faible[index] += add[0]  # Ajouter à lindex de la liste <faible> n points de difficultés
            corrige.append(juste)       # Ajoute le mot juste à la liste <corrige>
            if reponse:    # Si la traduction saisie contient au moins 1 caractère (!=vide)
                corrige.append(reponse)    # Ajouter à la lsite <corrige> la réponse fausse saisie <reponse>
            else:    # Sinon (si la réponse est vide)
                corrige.append('<vide>')    # Informe que la réponse était vide
        # Supprime l'index <r> des listes <m1> et <m2> pour ne pas que la fonction randint() ressorte le même index
        del m1[r]   # Supprime l'index <r> de la liste <m1>
        del m2[r]   # Supprime l'index <r> de la liste <et>
    score = round(p/N*base)    # Convertie le score sur la base définie
    print("\nFin du contrôle ",score,'/',base,sep='')    # Affiche le score sur la <base> (ex: 10/20)
    if p != N:    # Si il y a eu au moins 1 faute
        reponse = input("Voulez voir le corrigé ? (Y/n) : ")    # Demande d'affichage du corriger
        if reponse in ['Y', 'y']:    # Si l'utilisateur valide la demande par 'y' ou 'Y'
            for i in range(N-p):     # Pour i allant de 0 à N-p (= nombre de fautes)
                # Affiche 1.le mot suivi de 2.sa tradution et 3.la mauvaise tradution répondue
                # Pour afficher ces 3 éléments de la liste <corriger>
                # L'index <i> de la boucle for est multiplié par 3 
                # puis il y est additionné par l'entier (1 ou 2) pour acccéder à l'élément voulu
                print(i+1,'/',N-p," La traduction de <",corrige[i*3],"> est <",corrige[i*3+1],"> (≠",corrige[i*3+2],")",sep='',end='')
                input()    # Attendre que l'utilisateur prenne connaissance de son erreur
            print()    # Saute une ligne
    # Enregistre le score dans la liste <note>
    note[0].append(score)    # <note> étant un tableau par adresse, sa nouvelle valeur sera conservée à la sortie de la procédure
    now = datetime.now()     # now est une class qui contient la date et le temps de l'ordinateur 
    note[1].append(now.strftime('%H:%M'))    # .strftime() va rechercher les valeurs demandées par '%' (ex: '%H'= heure actuelle)
    if p == N or reponse in ['Y', 'y']:    # Si il n'y a pas de corrigé ou à l'inverse si le corrigé à bien été lu...
        # Pour ne pas avoir un retour trop brusque sur le menu
        input("Appuiez sur entrée pour revenir au menu...")

# Définie la procédure hard() avec les paramètres <mot1>, <mot2>, <point> et <langue>
def hard(mot1, mot2, faible, langue):
    # Cette procédure est la plus complexe du fait de la difficulté à gérer les difficultés des mots individuellement
    # Après une analyse et triage de tous les points de difficultés de la liste <faible>
    # Un sous menu est lancé semblable au menu principale 
    # à la différenc prêt que les mots mis en arguments correspondent uniquement aux mots à point faible
    # Ici les points de difficultés ne peuvent être modifiés
    # Il faut se rendre dans le menu principale et lancer un controle() pour réduire ses points faibles  
    N = len(faible)    # Initialistion de la variable <int><N> aux nombres de mots contenues dans la liste <faible>
    print("Bienvenue dans le mode POINT FAIBLE\n")    # Affiche un petit message de bienvenue
    # Initialisation du tableau <top> 
    # La première liste du tableau correspond à la copie de la liste <faible> contenant les points faibles de chaque mot
    # La deuxième liste du tableau contient une suite arithmétique de raison 1 
    # Cette suite sert à garder lié l'index du mot <--> ses point faibles
    # Car le tableau va être trié dans l'ordre décroissant des points faibles de la 1ere liste
    top = [faible[:], [i for i in range(N)]]    # Initialisation du tableau <int><top>
    # La 2eme liste est égale à <i>. Or <i> correspond à la variable de la boucle pour <i> allant de 0 à <N>
    # Donc la 2eme liste comprendra tout les entiers positifs de 0 à <N>
    trier = True    # Initialisation de la variable <bool><trier> à l'état <True> pour entrer dans la boucle while
    while trier:    # Tant que <trier> n'est pas égale à rien (!=0)
        trier = False   # Conjecturer que la liste 1 du tableau <top> est bien trier dans l'ordre décroissant des points faibles
        for i in range(N-1):      # Pour <i> allant de 0 à N-1
            if top[0][i] < top[0][i+1]:     # Si la valeur la plus grande dans l'intervalle [i;i+1] est à droite de la liste
                trier = True    # Affecter à <trier> l'état True pour continuer à trier
                for j in range(2):    # Répéter 2 fois
                    # Inverser les valeurs <i> et <i>+1 de la 1ere et 2eme (j) liste du tableau <top>
                    top[j][i], top[j][i+1] = top[j][i+1], top[j][i] 
    # Vérifie si la première liste de <top> contient que des 0
    # Si le nombre, par la fonction .count(), de 0 contenu dans la liste d'index 0
    # du tableau <top> est le même que la longueur de cette même liste
    # cela signifie que top[0] ne comporte que des 0 c.a.d. aucune difficulté
    if top[0].count(0) == N:
        print("Félicitation ! Vous n'avez aucune difficultée :)")  # Il n'y a aucun mot qui pose difficulté
        input("\nAppuyez sur entrée pour revenir au menu...")      # Pour ne pas avoir un retour trop brusque sur le menu
    else:    # top[0] comporte au moins 1 difficulté
        print("Ce mode analyse vos points faibles\nEt vous permet de vous concentrez sur vos difficultés")
        # Le nombre total de mots difficiles <n> correspond à N moins le nombre de 0, qui sont des mots non difficiles
        n = N - top[0].count(0)
        if n > 1:   # Si il y a plus d'un mot difficile
            print("Tu as", n, "difficultées sur", N, "mots")  # Afficher la proportion de difficulté <n> sur le nombre total <N> de mot
        if n > round(N/2):    # Si la proportion des mots mot à difficultés est supérieur que tout les mots divisé par 2
            temp = n
            n = 0    # Reset <n> à 0
            pc = int(input("\nQuelle quantitée en % voulez vous trvailler ? : ")) # Convertie la saisie en <int>
            # Produit en croix pour obtenir la quantité <n> de mot à travailler en fonction du % voulu du total <N> 
            n = int(pc*temp/100)
            if n < 1:    # Si le produit en croix donne 0
                n = 1    # Forcer le nombre de mot à travailler à être supérieur à 0
            elif n > N:  # Si le produit en croix est supérieur au maximum <N>
                n = N    # Forcer <n> à ne pas dépsser le maximum <N>
        # Ces 2 lignes suivantes sont très compressées et donc optimisées
        # Prenons l'exemple de <motHard1>
        # La liste est initialisée depuis la liste <mot1> qui contient TOUT les mots en français
        # Or nous ne voulons que les mots à travailler donc difficiles
        # Pour se faire seul les mots de <mot1> dont leurs index correspondent 
        # aux valeurs de la 2eme liste du tableau <top> sont utilisés
        # Afin d'accéder à tout les index voulu, la boucle for est appellée
        # pour affecter chaque mot de <mot1> d'index (valeur du 2eme tableau) <i> dans la liste <motHard1>
        motHard1 = [mot1[top[1][i]] for i in range(n)]    # Initialisation de <str><motHard1> en local
        motHard2 = [mot2[top[1][i]] for i in range(n)]    # Initialisation de <str><motHard2> en local
        play = True     # Initialisation de la la variable <bool><play> à l'état True pour entrer dans la boucle while
        while play:     # Tant que play != 0
            if n == 1:  # Si il n'y a qu'un seul mot à travailler
                print("\nTa plus grande difficulté est : ")
            else:    # sinon (si il y a plus d'un mot à travailler)
                print("\nTes mots les plus difficiles sont dans l'ordre décroissant : ")
            # Afficher les mots difficiles avec leurs points de difficultés, précédament trié dans l'ordre décroissant 
            for i in range(n):    # Pour <i> allant de 0 à <n> 
                # Affciher l'index <i> de <motHard1> avec ses points faibles <top[0]>
                print('<',motHard1[i],'>(',top[0][i]/10,')',sep='',end='  ')
            # Afficher le sous menu de la procédure hard()
            # Son fonctionnement est le même que le menu principal
            print("\n\nQue veux tu faire pour t'améliorer ? ")
            print("1. Apprendre")
            print("2. Reviser")
            print("3. Test")
            print("4. Quitter(Menu)")
            choix = input("Lancer le mode :")    # Saisir le choix voulu dans <str><choix>
            print()    # Saute une ligne
            if choix == '1':
                # Appel de la procédure apprendre() avec comme arguments <motHard1> et <motHard2>
                # Et non <mot1> car on veut travailler que sur les mot à difficultés 
                apprendre(motHard1, motHard2) 
            elif choix == '2':          
                # Appel de la procédure reviser() avec comme arguments <motHard1>, <motHard2> et <langue>
                reviser(motHard1, motHard2, langue)
            elif choix == '3':
                # Appel de la procédure test() avec comme arguments <motHard1>, <motHard2> et <langue>
                test(motHard1, motHard2, langue)
            elif choix == '4':
                play = False    # Sortir de la boucle while
            else:
                # Si Aucune des conditions ne correpondent aux choix
                print("Choix inconnu, erreur...")

# Définie la procédure pendu() avec les paramètres <mot1>, <mot2> et <langue>
def pendu(mot1, mot2, langue):
    # Le jeu du pendu à été créer
    # pour se détendre entre deux séance de test() ou controle()
    # Il permet aussi de reviser l'écriture d'un mot
    # Le principe de jeux est simple
    # Après avoir choisi la langue du mot à trouver
    # Afficher le mot en cachant ses lettres par des '_' (sauf la première)
    # A chaque bonne lettre trouvée, remplacer '_' par la bonne lettre
    # A chaque mauvaise lettre, enlever un point de vie et afficher la potence
    def espace(mot):    # Définie la fonction espace() avec le paramètre <mot>
        # Retourne la chaine de caractère <mot> avec des espaces entre chaque caractère
        motE = ''    # Initialise la variable <str><motE> à une chaine de caractère vide
        for i in mot:    # Pour <i> allant de 0 à longueur du paramètre <mot>
            motE += i + ' '    # Ajouter par concaténation à <motE> la lettre <i> du <mot> et un espace(=' ')
        return motE    # retourner la variable <motE> 
    def verifie(lettre):    # Définie la fonction verifie() avec le paramètre <char><lettre>
        # Cette fonction vérifie si la lettre proposer est dans la variable <str><mot>
        # Si c'est le cas retourner False
        # Si la lettre proposer n'est pas dans la variable <str> mot retourner True
        # Vérifie dans un premier temps
        # 1.Si la lettre est valide pour être comparer avec <mot>
        # 2.Si la longueur est différente de 1 et différente de 'exit'
        if len(lettre) != 1 and lettre != 'exit':
            print('Erreur...')    # Afficher "Erreur"
            return 0    # Sortir de la fonction en retournant 0
        # Vérifie dans un second temps si la lettre n'a pas déjà été utilisée
        if lettre in utilise:    # Si la liste <utilise> contient la lettre
            print('Vous avez déjà utilisé cette lettre...')
            return 0    # Sortir de la fonction en retournant 0
        perdu = True    # Conjecture que la lettre n'est pas dans mot
        # Si la lettre est valide, vérifier si elle appartient à <mot>
        for i in range(len(trouve)):    # Pour i allant de 0 à la longueur de la liste <trouve>
            # Si la lettre correspond à l'index <i> du mot à trouver <mot>
            if lettre.upper() == mot[i].upper():
                trouve[i] = mot[i]   # Affecter au rang i de <trouve> la lettre <mot[i]>
                perdu = 0            # Sortir de la foncction en retournant False
            # Sinon si le mot <mot> contient des accents (é, è,...) de <strE>
            # et que la <lettre> est 'e'
            # alors si l'index <i> du mot à trouver <mot> contient un des accents de la liste <strE>
            elif accent == True and lettre == 'e' and (mot[i] in strE) == True:
                # Affecter au rang <i> de <trouve> la lettre d'index <i> du mot à trouver
                trouve[i] = mot[i]
                perdu = 0   # Affecter à perdu False
        return perdu    # retourner la variable <bool><perdu>

    def affiche(vie, affiche):    # Définie la fonction affiche() avec les paramètres <vie> et <affiche>
        # Cette profcédure affiche un "dessin" d'une potence dans le terminal avec des '#'
        # Définie la fonction ligne() avec les paramètres <ligne>, <mini> et <maxi>
        def ligne(ligne, mini, maxi):
            # Cette procédure affecte l'intervale [mini;maxi] de la liste d'index <ligne> du tableau <potence> des '#'
            while mini < maxi:    # Répéter jusqu'à que la variable <mini> soit égale à <maxi>
                # Affecter au rang <mini> de l'index <ligne> du tableau <potence> le caractère '#'
                potence[ligne][mini] = '#'
                mini += 1    # Incrémente 1 à la variable <int> <mini>

        # Définie la fonction colonne() avec les paramètres <colonne>, <mini> et <maxi>
        def colonne(colonne, mini, maxi):
            # Cette procédure affecte l'intervale [mini;maxi] de la liste d'index <ligne> du tableau <potence> des '#'
            while mini < maxi:    # Répéter jusqu'à que la variable <mini> soit égale à <maxi>
                # Affecter au rang <mini> de l'index <colonne> du tableau <potence> le caractère '#'
                potence[mini][colonne] = '#'
                mini += 1    # Incrémente 1 à la variable <mini>
        # En fonction des vies restantes ajouter les différentes parties (poutre(verticales, horizontales), corde,...) de la potence
        if vie == 7:
            # 1ère poutre horizontal
            ligne(7, 0, 9)  # Apelle de la fonction ligne() avec 7, 0, 9 en arguments
        elif vie == 6:
            # 2eme poutre appartenant et perpendiculaire à la première
            colonne(3, 2, 7)  # Apelle de la fonction colonne() avec 3, 2, 7 en arguments
        elif vie == 5:
            # 3eme poutre parallèle à la première, passant par le segment de la 2eme poutre et perpendiculaire à cette dernière
            ligne(1, 3, 13)  # Apelle de la fonction ligne() avec 1, 3, 13 en arguments
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
            colonne(12, 4, 7)    # Apelle de la fonction colonne() avec 12, 4, 7 en arguments
        elif vie == 0:
            # Bras du corps
            ligne(4, 10, 15)    # Apelle de la fonction ligne() avec 4, 10, 15 en arguments
        # Si le parmamètre <bool> <affiche> est vrai alors afficher la potence
        if affiche == True:
            # Double boucle pour afficher le tableau à 2 dimenssions
            for i in range(8):
                for j in range(17):    # Boucle pour <j> car <i> est déjà utilisé
                    print(potence[i][j],end='')
                print()    # Revenir à la ligne après chaque affichage d'une ligne

    def gagner(vie):    # Définie la fonction gagner() avec le paramètre <vie>
        # Cette fonction permet de vérifier si toutes les lettres ont été trouvées
        # Si c'est le cas la fonction renvoie -1 pour sortir de la boucle
        # et ne pas passer par la condition <if vie == 0>
        # Si il reste des lettres introuvées la fonction renvoie la même vie reçu en paramètre
        for i in trouve:   # Pour <i> allant de la lettre d'index 0 du mot <trouve> à sa dernière
            if i == '_':    # Si la lettre <i> est égale à une lettre pas encore trouvée '_'
                return vie   # Renvoyer la vie actuelle
        return -1   # Si la boucle s'est fini (sans return) alors renvoyer -1

    # Programme principal
    vie = 8    # Initialise la variable <int><vie> à 8
    # Conjecture que le mot n'a pas d'accent (é, è, ê,...)
    # Avec l'initialisation de la variable <bool><accent>
    accent = False
    utilise = []    # Initialise la liste <str><utilise> pour les mots utilisés
    potence = []    # Initialise le tableau (liste à 2 dimmensions) <str><potence> pour afficher la potence et le pendu
    print("Bienvenue dans le jeux du PENDU\nTapez 'exit' pour abandonner\n")    # Petit message de bienvenue
    # Demande dans quelle langue le mot à trouver doit être deviné
    # Avec les index 0 et 1 du paramètre <langue>
    print("Vous voulez jouer en ",langue[0],'(1)/',langue[1],"(2) : ",sep='',end='')
    langue = input()    # Enregistre la réponse dans la variable <str><langue>
    if langue == '1':   # Si la langue choisie est la première
        # Affecter à <mot> un mot aléatoire entre tous les mots de la liste <mot1>
        mot = mot1[randint(0, len(mot1)-1)]
    else:    # Sinon
        # Affecter à <mot> un mot aléatoire de la liste <mot2>
        mot = mot2[randint(0, len(mot2)-1)]
    # Ce script enlève l'article du mot
    if ' ' in mot[:4]:    # Si les 3 permières caractères de <mot> contiennent un espace
        i = mot[:4].index(" ")    # Enregistre l'index de <mot> où se trouve le caractère ' '
        mot = mot[i+1:]    # Affecte à <mot> le mot sans l'article
    # Initialiser la liste <strE> correspondant à tous les accents possible de la lettre 'e'
    strE = ['é', 'è', 'ê', 'ë']
    # Liste <char> des caractère indésirables qu'on veut montrer dans la liste <trouve>
    strSpecial = [' ', "'", '-', '&']
    # Initialisation du mot à trouver <str><trouve> par une liste contenant 
    # des caracrtères underscore = '_' fois la longueur du mot à trouver <mot>
    trouve = ['_']*len(mot)
    # Analyse du mot <mot> afin de trouver si :
    # 1.Il comporte des 'e' avec accent <strE>
    # 2.Il comporte des caractères spéciaux (comme un tiret ou une apostrophe)
    #      qui devront être directements visibles dans le mot caché <trouve>
    #      Car ce n'est pas un lettre à trouver !
    for i in range(len(mot)): # Pour <i> allant de 0 à la longueur de <mot>
        if mot[i] in strE:    # Si la lettre i de <mot> appartient à la liste <strE>
            accent = True      # Affecter à accent l'état True
        else:    # Sinon, si la lettre <i> contient autre chose que <strE>
            for j in range(len(strSpecial)):   # Compare la lettre avec toutes les <char> de <strSpecial>
                # Si le <i>eme caractère de <mot> est égale à la valeur d'index <i> de <strSpecial>
                if mot[i] == strSpecial[j]:
                    # Remplacer la valeur <i> de <trouve> par le même
                    # caractère <i> de <mot> (ou strSpecial[i] c'est la même chose)
                    trouve[i] = mot[i]
    # Initialisation du tableau 17x8 <potence> pour afficher graphiquement la potence et le pendu
    for i in range(8):    # Pour <i> allant de 0 à 8
        # Ajouter à la liste <potence>, une liste vide de 17 espaces ' '
        potence.append([' ']*17)
    # Afficher la première lettre du mot <mot> dans la liste <trouve>
    trouve[0] = mot[0]
    ##################################
    # Boucle principale du jeu pendu()
    # Tant qu'il reste de la <vie> ou que le mot est trouvé (<vie>=-1)
    while vie > 0:
        # Afficher le mot à trouver <trouve> avec la fonction espace()
        print(espace(trouve))
        # Demande de saisie d'une lettre dans la variable <char><lettre>
        lettre = input("Entrez une lettre : ")
        # Vérifie si la <lettre> appartient au <mot> avec l'appelle de la fonction verifie()
        # L'appelle de cette fonction se fait avec l'argument <lettre>
        # La fonction retourne soit True pour "la lettre est dans <mot>"
        # La fonction retourne False pour "la lettre n'est pas dans <mot>"
        if verifie(lettre):    # Si la fonction retourne False
            vie -= 1    # Retirer une vie à la variable <vie>
            utilise.append(lettre)    # Ajoute la lettre saisie dans la liste <utilise>
        if lettre == 'exit':    # Si la variable <lettre> contient la demande 'exit'
            # Passer une par une les vies jusq'à 0
            # Tout en appelant la procédure affiche() sans aficher la potence 
            # Pour affciher par la suite la potence en entier
            for i in range(vie):    # Pour i allant de 0 à <vie>
                affiche(vie, False)   # Appelle de la procédure affiche() avec comme arguments <vie> et 0
                vie -= 1              # Enlever 1 vie à la variable <vie>
        affiche(vie, True)   # Afficher la potence grâce à l'argument True de la procédure affiche()
        vie = gagner(vie)    # Envoie en argument <vie> à la fonction gagner() qui revoie la nouvelle valeur de <vie>
    if vie == 0:    # Si <vie> est nulle alors le mot n'a pas été trouver par manque de vie
        print('\nPERDU\nLe mot était <',mot,'>',sep='')    # Afficher la bonne réponse
    else:    # Sinon si <vie> = -1 cela signifie que le mot à été trouvé
        print(espace(mot))          # Affiche le mot <mot> avec la fonction espace()
        print('\nFELICITATION !')   # Affiche la récompense de l'utilisateur
    # Pour ne pas avoir un retour trop brusque sur le menu
    input("\nFin du jeu pendu\nAppuiez sur entrée pour revenir au menu...")

# Définie la procédure parametre() avec les paramètres <mot1>, <mot2>, <faible> <langue> <note> <noteSave> et <settings>
def parametre(mot1, mot2, faible, langue, note, noteSave, settings):
    # Cette procédure permet 3 actions:
    # 1. Ajouter des mots, afin de na pas à avoir le faire depuis un éditeur texte en dehors du progrmame
    # 2. Reset les point faibles, si par exemple une autre personne veut apprendre les mots
    # 3. Changer la base de note, si une note sur 10 ne vous convient pas vous pouvez la changer sur n'importe quelle autre base dans l'intervale [1; +infini[
    #    Pour ne pas a avoir à changer la base à chaque redémarrage du programme, cette valeur est sauvegardée dans le fichier score.txt
    global base   # Définie la variable <base> comme global car elle va être modifiée
    def setBase(list1, list2, base):
        # Cette fonction change la base de la note pour les procédures test() et controle() ainsi que l'enregistrement du meilleur score
        # de la partie dans le fichier SCORE(<theme>).txt Or si la base change la note du meilleur score change aussi !
        # Il faut donc reconvertir avec les produits en croix la note pour qu'elle corresponde avec la nouvelle base (ex : 5/10 -> 10/20)
        print("La base actuelle est de <note/", base, ">", sep='')    # Affiche la base actuelle avec la variable global <base>
        newBase = 0    # Pour rentrer dans la boucle while
        while newBase <= 0:    # Tant que la nouvelle base ne corresponde pas aux critères de validités
            newBase = int(input("Entrez votre nouvelle base : "))    # Saisir la nouvelle base dans <int><newBase>
            if newBase <= 0:    # Si la base est négative ou nulle
                print("La base doit être positive !")
        for i in range(len(list1[0])):    # Pour <i> allant de 0 au nombre de note compris dans la liste d'index 0 du tablau <list1>
            list1[0][i] = round(list1[0][i] / base * newBase)    # Convertir la note de <list1> en fonction de la nouvelle base
        for i in range(len(list2[0])):    # Pour <i> allant de 0 au nombre de note compris dans la liste d'index 0 du tablau <list2>
            list2[0][i] = round(list2[0][i] / base * newBase)     # Convertir la note de <list2> en fonction de la nouvelle base
        return newBase    #retourne la variable local <newBase>
    def reset(list):
        # Ce reset est déconsillé d'être effectué car il ne sera plus possible de connaître ses plus grosses difficultées
        # C'est pourquoi une demande de confirmation est demandée pour continuer
        if input("Cette commande est irréverssible ! Poursuivre ? (Y/n) : ") in  ['Y', 'y']:    # Si l'avertissement est accepté 
            # Affecter à tout les index de <list> la valeur 0
            for i in range(len(list)): # Pour i allant de 0 au nombre de valeur de <list>
                list[i] = 0    # Affecter à l'index i de <faible> la valeur 0
    def add(list1, list2, list3, list4):
        # Pour ajouter des mots, 3 listes doivent être affectées : <list1> et <list2>
        # Il n'y pas plus à faire, et ces mots seront bien enregistrés dans le fichier mot.txt lors de la fermeture du programme
        print("Pour ajouter des mots suivez les instructions !")
        ajout = True    # Initialise la variable <bool><ajout> à True pour entrer dans la boucle while
        while ajout:    # Tant que ajout != 0
            print("Entrez le mot en", list3[0], ': ', end='')    # Demande le premier mot dans la langue de l'élément 0 de <list3>
            # Ajoute le mot saisie par input() dans la liste <list1> qui est un paramètre par adresse de <mot1>
            # Donc cette liste mise en argument lors de l'appelle de la procédure add() sera bien affectée
            list1.append(input())    # Ajoute le mot <input()> dans <list1>
            print("Entrez sa traduction en", list3[1], ': ', end='')    # Demande la traduction du mot dans la langue de l'index 1 de <langue>
            list2.append(input())   # Ajoute la traduction saisie dans <list2>
            list4.append(0)     # Ajoute 0 dans la liste <list4> (pour 0 point de difficulté pour la nouvelle paire de mot)
            if not input("Encore un autre ? (Y/n) : ") in ['Y','y']:  # Si la réponse ne correspond pas au 'Y, y' de Yes, quitter la boucle
                ajout = False   # Affecter à <ajout> la valeur 0 pour quitter la boucle while
    def setGraph(list):
        # Cette procédure permet de modifier le mode des dimensions du repère de la procédure graphique() 
        mode = ['automatiques', 'manuels']    # Affecte à <str><mode> les deux paramtères possibles
        print("Les dimensions du grpahique sont <", mode[list[0][0]],">", sep='')    # Affiche le mode actuelle 
        print("Vous pouvez :\n1. Ne rien faire")    # Propose les choix disponibles
        print("2. Changer le mode")
        if list[0][0]:  # Si la valeur d'index 0 de la liste du rang 0 du tableau <list> est égale à 1 (diff de 0) 
            print("3. Ajuster les dimensions")      # Cela signifie que le mode maunel est vrai (True)
        choix = input("Votre choix : ")    # On peut donc choisir manuelement les dimensions
        if choix == '2':    # Si on veut changer de mode
            # Switch entre True ou False
            if list[0][0]:    # Cette condition switch dans le True
                list[0][0] = False    # Il faut donc mettre le mode manuel à False
            else:    # Le mode manuel est False
                list[0][0] = True   # Donc on l'inverse en True
            print("\nLes dimensions ont bien été modifiées en <",mode[list[0][0]], ">!",sep="")    # Confirme les changements
        # Si le mode manuel est activé et qu'on veut modifier les valeur des axe x et y
        if list[0][0] == True and choix == '3':
            axe = ['x', 'y']    # Affecter à <str><axe> les noms des 2 axes du repère
            for i in range(2):     # Répétition x2
                # Demande la nouvelle valeur de l'axe <axe[i]> en affichant la valeur actuelle
                print("Definir axe ",axe[i]," (",list[0][i+1],") : ",sep='',end='')
                list[0][i+1] = int(input())    # Affecte au tableau <list> la nouvelle valeur <str> convertie en <int>
    print("Bienvenue dans le menu PARAMETRE !")
    play = True     # Initialise la variable <bool> <play> à True pour entrer dans la boucle while
    while play:     # Tant que play != 0
        # Affiche le sous menu
        print("\nQue souhaitez vous faire ?")
        print("1. Ajouter des mots")
        print("2. Reset points faibles")
        print("3. Changer base note")
        print("4. Dimensions graphique")
        print("5. Quitter(menu)")
        # Saisir le choix 1, 2, 3 ou 4
        choix = input("Executer le paramètre : ")
        print()  # Saute une ligne
        if choix == '1':     # Si le choix est égale à '1'
            add(mot1, mot2, langue, faible)    # Appelle de la procédure add() sans argument
        elif choix == '2':   # Si le choix est veut dire "Reset les pointF"
            reset(faible)    # Appelle de la procédure reset() sans argument
        elif choix == '3':   # Si le choix est centré sur la modification de la base pour les notes
            base = setBase(note, noteSave, base)    # Appelle de la fonction setBase() qui retourne la nouvelle base
        elif choix == '4':       # Si le choix est traduit par l'envie de touchez au option graphique
            setGraph(settings)   # Appelle de la procédure reset() sans argument
        elif choix == '5':       # Si le choix signifie 'Sortir du sous menu pour retourner au menu principal'
            play = False         # Affecter à <play> la valeur 0 pour quitter la boucle while
        else:    # Si aucune des condition ne correspondent au choix
            print("Choix inconnu, erreur...")   # Informer que le choix n'existe pas
        # Pour ne pas avoir un retour trop brusque sur le menu
        # Mais uniqement si l'utilisateur sort d'une procédure
        if choix in ['1', '2', '3', '4']:  # Si la variable <char><choix> appartient à la liste des choix correspondants à une procédure  
            input("\nLa commande s'est terminée avec succès !\nAppuiez sur entrée pour revenir au menu...")   # Bloque le programme jusq'à une action de l'utilisateur

# Définie la procédure save() avec les paramètres <note>, <noteSave> <mode> et <base>
def graphique(note, noteSave, manuel, base):
    # Cette procédure, grâce au module 'turtle.py' affiche un graphique sur un repère x, y 
    # Les ordonnées représentent la note sur 20 en fonction du temps (absisses) qui précisons, n'est pas à l'échelle 
    # On peut afficher 2 catégories de note différentes :
    #   - Les dernières notes actuelles du tableau <note> 
    #     C'est à dire les notes produites par controle(), depuis l'ouverture du programme
    #   - Toutes les meilleures notes du fichier SCORE(<theme>).txt
    # Avant de débuté le graphique il faut avoir convertie les notes sur une base de 20
    def s(x, y):
        # Afin de ne pas écrire à chaque fois la même longue procédure
        t.goto(t.xcor()+x, t.ycor()+y)    # Ajoute à x et y la valeur en plus ou en moins voulu 
    def fleche():
        # Trace une flèche au bout du repère
        t.right(135)   # Tourne à droite de 135 degrés
        t.down()       # Pose le stylo
        t.forward(9)   # Avance de 9
        t.up()         # Lève le stylo
        t.backward(9)  # Recule de 9
        t.left(270)    # Tourne à gauche de 270 degrés
        t.down()       # Pose le stylo
        t.forward(9)   # Avance de 9
        t.up()         # Lève le stylo
        t.backward(9)  # Recule de 9
        t.right(135)   # Tourne de 135 degrés
    def ecrire(str, x, y, taille, sens):
        # Ecrit la chaine de caractère voulu en se déplacant de <x> ou <y> avec une <taille> de police
        # Ainsi que le <sens> pour l'argument <align> de la fonction t.write() qui permet de choisir 
        # Si le texte doit être collé à gauche, à droite, ou au centre de la pointe du stylo
        t.up()  # Lève le stylo
        s(x, y) # Se déplace de <x> et <y>
        # Ecrit la chaine de caractère <str> avec la police 'Arial' en taille <taille>
        t.write(str, align=sens, font=("Arial", taille, "normal"))
        s(-x, -y)   # Revient sur les coordonnées précédentes 
    def point(color1, color2):
        #Trace un gros point en <color1> à chque valeur d'une note
        t.width(9)       # Règle l'épaisseur du stylo à 9
        t.color(color1)  # Règle la couleur du stylo à <color1>
        s(0, 0)          # Fait semblant davancer pour que le stylo "trace"
        t.width(4)       # Remet l'épaisseur su stylo à 4
        t.color(color2)  # Remet la couleur du stylo à <color2>

    # Programme principale 
    print("Bienvenue dans le mode GRAPHIQUE")
    print("\nVous voulez afficher : ")
    print("1. Vos dernières notes de cette séance")
    print("2. Vos meilleures notes du fichier score.txt")
    choix = input("Votre choix : ")
    total = 0   # Initialise la variable <int><total> pour le calcule de la moyenne
    if choix == '1':    # Si l'utilisateur veux voir ses notes actuelles
        noteGraph = note[0][:]     # Copie la liste <note> dans <noteGraph> SANS ADRESSE !
        tempsGraph = note[1][:]    # Affecte à <tempsGraph> toutes les heures aux quelles controle() à été appelée
        for i in note[0]:   # Calcule le total des note de la liste <note>
            total += i      # Incrémente l'index <i> de <note[0]> à <total>
        n = len(note[0])    # Initialise <n> au nombre de note dans <note[0]>
    else:   # Si l'utilisateur veut voir ses notes à partir du fichier
        noteGraph = noteSave[0][:]     # Copie la liste <noteSave> dans <noteGraph> SANS ADRESSE !
        tempsGraph = []            # Initialsiation de la liste <tempsGraph>
        for i in noteSave[1]:      # Analyse de toutes les notes de <noteSave>
            temp = i.split('/')    # Sépare la chaine de caractère <i> 
            tempsGraph.append(temp[0][3:]+'/'+temp[1])    # Affecte à <tempsGraph> toutes la date jour/mois de la variable <temp>
        for i in noteSave[0]:    # Calcule le total des note de la liste <noteSave>
            total += i    # Incrémente l'index <i> de <noteSave[0]> à <total>
        n = len(noteSave[0])   # Initialise <n> au nombre de note dans <noteSave[0]>
    if len(noteGraph) < 2:     # Si la quantité de note empêche la création d'un graphique
        print("\nIl n'y a pas assez de notes...\n")
    else:   # Si il y a assez de notes
        moyenne = round((total/base*20)/n) # Calcule la moyenne et affecter le résultat à <moyenne>
        if base != 20:    # Si la <base> est déjà à 20 il est inutile de convertir les notes avec une base 20...
            for i in range(len(noteGraph)):    # Affecte à chaque index de <noteGraph>...
                noteGraph[i] = round(noteGraph[i]/base*20)    # ...la note convertie sur une base de 20
        print("\nOuverture de la fenêtre turtle.py...", end='')
        try:    # Essaye
            # Si la fenêtre s'est déjà fermé, une erreur se produit lors de la re-ouverture
            # Mais si on execute une deuxième fois la commande, alors le module fonctionne à nouveau
            t.reset()   # Permet d'éxecuter 2x la commande t.rexet()
        except:    # Si une erreur se prosuit lors de l'ouverture de la fenêtre
            print("ERREUR !\n2eme tentative d'ouverture...", end='')
        t.reset()   # Remet tout les réglage à 0 et ouvre une fenêtre si ce n'est pas le cas
        t.bgcolor("black")    #Règle la couleur de l'arrière plan à noir
        t.speed(0)  # Règle la vitesse de déplacement à 0 (max)
        t.width(5)  # Règle l'épasseur du stylo à 5
        t.ht()      # Cache le stylo
        t.up()      # Relève le stylo
        # Si le mode manuel est vrai (True) alors affecter à <x> et <y> les valeurs enregistré dans <manuel>
        if manuel[0] == True:  
            x = manuel[1]    # Dimenssion global X à aprtir de <manuel>
            y = manuel[2]    # Dimenssion global Y à partir de <manuel>
        else:   # Si le mode manuel est faux, donc automatique
            t.color("white")    # Règle la couleur du stylo à blanc
            # Demande de bouger la fenêtre 
            ecrire("Ajustez la taille de la fenêtre", 0, 0, 20, 'center')
            ecrire("Ensuite appuez sur [entrée] dans le terminal", 0, -30, 20, 'center')
            print("OK!\nDéfinissez la taille du grapgique...", end='')
            input()    # Attend que l'utilisateur ai fini ses réglages
            # t.window_height() est une fonction qui retourne la hauteur de la fenêtre turtle.py
            #  t.window_width() est une fonction qui retourne la largeur de la fenêtre turtle.py
            x = t.window_width()/1.4     # Dimenssion global X à partir de la dimension x de la fenêtre
            y = t.window_height()/1.2     # Dimenssion global Y à partir de la dimension y de la fenêtre
            # 6qzFdbGS
            t.clear()    # Efface juste le texte 
        xDec = -(round(x/2)+40)   # Recule dans les négatif de x par rapport à x=0
        yDec = -(round(y/2))      # Descente dans les négatif de y par rapport à y=0
        decAxeX = round(x/18)     # Décalage entre le bout du repère et le bout de l'axe x
        decAxeY = round(y/18)     # Décalage entre le bout du repère et le bout de l'axe y
        miniDec = 4               # Pour ne pas que le dégradé touche l'axe y
        tLim = round((x-decAxeX)/19)        # Limite pour l'axe des x sinon les valeurs <temps> s'imprime les une sur les autres
        tailleMoy = round((x-decAxeX)/20)   # Taille de police de la moyenne des notes 
        tailleAxeY = round(y/55)+5          # Définie la taille des unités en ordonnées (notes)
        tailleNoteAxe = round((y+x)/100)+5  # Définie la taille des unités des axes (note et temps)
        colorRepere = '#4261CA'     # Bleu clair
        colorCourbe = '#9D2fF5'     # Violet 
        colorPoint = '#D287D6'      # Violet clair
        colorMoyenne = '#F34141'    # Rouge clair
        # Initialisation de la liste <str><colorDegrader> comportant un dégarder du rauge --> vert en #hexadécimal
        # Chaque index correspond à une couleur décomposer en RGB
        # Par exemple #FD 0D 01   = hexadécimal
        #             253 13  1   = base de 10 
        #              R  G   B   = couleur
        # La couleur R=red=rouge étant dominante on obtient du rouge
        colorDegrader = ['#FD0D01', '#FB2803', '#F94205', '#F85F06', '#F67708', '#F48F0A', '#F2A90C', '#F0BF0E', '#EFD50F', '#EDED11', '#D6EB13', '#BEE915', '#A5E816', '#90E618', '#78E41A', '#64E21C', '#52E01E', '#3CDF1F', '#2ADD21', '#23DB2C']
        # Affiche axe x et y
        print("OK !\nConsruction du repère x, y...", end='')
        t.color(colorRepere) # Règle la couleur du stylo à bleu
        s(xDec, yDec) # Se place à l'origine du repère [0;0]
        t.down()      # Pose le stylo
        s(0, y)       # Trace l'axe des ordonnées y
        t.left(90)    # Pour tracer la flèche dans le bon sens
        ecrire("NOTE", 5, 2, tailleNoteAxe, 'center')  # Notation de l'axe y
        fleche()    # ajout d'une fleche sur le bout de l'axe y
        s(0, -y)    # Retour à l'origine
        t.down()    # Pose le stylo
        s(x, 0)     # Trace l'axe des abscisses x
        ecrire("TEMPS", 4, -10, tailleNoteAxe, 'left')   # Notation de l'axe x
        t.right(90)   # Pour tracer la flèche dans le bon sens
        fleche()      # ajout d'une fleche sur le bout de l'axe x
        s(-x, 0)      # Retour à l'origine
        # Construction lignes dégrdées
        print("OK !\nConstruction de l'échelle en ordonnée...", end='')
        t.width(4)      # Affine l'épaisseur du stylo
        s(miniDec, 0)   # Se décale un peu vers la droite
        for i in range(20):     # Trace 20 lignes en partant de y=0
            t.color(colorRepere)     # Règle la couleur 
            if i % 2 == 0:      # Si <i> n'est pas divisible par 2
                ecrire(str(i), -10, -7, tailleAxeY, 'right')    # Ecrit l'échelle (rapproché de l'axe y)
            t.up()    # Lève le stylo
            s(0, (y-decAxeY)/20)        # Monte de quelques ordonnées sur l'axe y
            t.color(colorDegrader[i])   # Règle la couleur à la couleur hexadécimal du rang i de <degrader>
            t.down()  # Pose le stylo
            s(x-decAxeX-miniDec, 0)     # Trace la ligne
            t.up()  # Lève le stylo
            s(-(x-decAxeX-miniDec), 0)  # Reviens sur l'axe des ordonnées
        t.color(colorRepere)     # Règle la couleur 
        ecrire('20', -10, -7, tailleAxeY, 'right')  # Ecrit la dernière unité de temps 
        t.up()  # Lève le stylo
        s(-miniDec, 0)   # Se re-colle à l'axe y
        s(0, -(y-decAxeY))  # Se place sur l'origine
        # Construction échelle temps + Initialisation graphique
        if len(noteGraph) > tLim:     # Si le nombre de note est trop grand
            noteGraph = noteGraph[-tLim:]       # Garder uniquement les <tLim> dernières notes
            tempsGraph = tempsGraph[-tLim:]     # Garder uniquement les <tLim> dernières dates
        xStep = (x-decAxeX)/(len(noteGraph)-1)  # Règle la raison <xStep> des absisses
        yStep = (y-decAxeY)/20  # Règle le multiplicateur des ordonnées
        print("OK !\nConstruction de l'échelle en abscisse...", end='')
        t.up()  # Lève le stylo
        for i in range(len(tempsGraph)):    # Ecrire le nombre de date ou heure dans la liste <tempsGraph>
            # La condition suivante augmente, plus l'axe x et grand (numérateur) et diminue si il y a beaucoup de note (dénominateur)
            # Ainsi si le qutient est inférieur à 35 cela signifie que l'axe x est trop petit pour afficher toutes les notes
            # Ou qu'il y a trop de notes pour tous les afficher
            # Le <i> % 2 permet d'alterner dans les y (une fois sur 2 aller un peu plus bas lors de l'écriture)
            if round((x-decAxeX)/len(tempsGraph)) < 35 and i % 2:    # Si la division par 2 donne un reste (pour i = 1, 3, 5,...)
                ecrire(tempsGraph[i], 5, -35, 10, 'center')      # Ecrire la date ou heure en allant plus en dessous de l'axe des absisses
            else:
                ecrire(tempsGraph[i], 5, -20, 10, 'center')      # Ecrire la date ou heure en allant au plus proche de l'axe des absisses
            s(xStep, 0)     # Avance de quelques x 
        # Initialisation graphique
        t.color(colorCourbe)  # Règle la couleur
        s(-(xStep*len(tempsGraph)), 0)      # Retourne à l'origine [0;0]
        s(0, (noteGraph[0]*(y-decAxeY)/20))     # Monte en y en fonction de la grandeur de la 1ere note de <noteGraph>
        t.down()    # Pose le stylo
        point(colorPoint, colorCourbe)     # Trace un point
        t.width(4)  # Règle l'épaisseur u stylo à 4
        t.speed(round(len(noteGraph)/10)+1) # Change la vitesse à lent
        print("OK !\nConstruction de la courbe...", end='')
        # Trace le graphique
        for i in range(1, len(noteGraph)):  # Pour i allant de 0 à la dernière note de <noteGraph>
            t.goto(t.xcor() + xStep, noteGraph[i]*yStep+yDec)  # Avance de xStep et se place sur les ordonnées en fonction de la note
            point(colorPoint, colorCourbe)     # Trace un point
        print("OK !\n") # Dernier check 
        t.speed(0)  # Vitesse au maximum
        t.up()      # Relève le stylo
        t.color(colorMoyenne)    # Change la couleur
        t.goto((x-decAxeX)/2+xDec, yDec+y)    # Se déplace en haut, au milieu du grpahique pour afficher la moyenne
        ecrire(("MOYENNE = " + str(moyenne) + "/20"), 0, -(round(decAxeY/2)), tailleMoy, 'center')   # Ecrit la moyenne du grpahique de note
    input('Le graphique a bien été affiché\nAppuiez sur entrée pour revenir au menu...')
    #print("Ne fermez pas la fenêtre turtle.py merci :)")
    if len(noteGraph) > 1:  # Si la fenêtre à été ouverte
        t.bye()     # Ferme la fenêtre 
    
# Définie la procédure save() avec les paramètres <mot1>, <mot2>, <faible>, <langue>, <noteSave> <note> <settings> et <base>
def save(mot1, mot2, faible, langue, noteSave, note, settings, base):
    # Cette procédure est déstiné à sauvegarder toutes les valeurs de variables, listes, et tableaux dans des fichiers textes
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
    f = open("fichier/mot.txt", 'r', encoding='Utf-8')
    saveFirst = []  # Enregeistre les thèmes avant celui recherché
    trouve = '['+langue[2]+'] ['+langue[0]+'='+langue[1]+']\n' # Définie la ligne dans le fichier mot.txt à trouver 
    sortir = False  # Variable <bool><sortir> pour sortir de la boucle 
    for l in f:     # Lecture de tout le fichier texte
        if l == trouve:   # Si la ligne <l> est égale à la ligne recherché
            saveFirst.append(l)     # Enregistre la ligne thème + langue car elle ne change pas
            sortir = True   # Une fois tout les mots précédents le thèmes actuelle sauvegardés, on peut sortir de la boucle 
        if sortir == True:  # Il faut d'abord avoir trouvé le thème qui à été choisit avant de quitter
            if l == '\n':   # Il faut d'abord passé le thème qu'on va re écrire avec les listes !
                break   # Sortir de la boucle for 
        else:   # Si on n'a pas encore trouver la ligne recherchée
            saveFirst.append(l)    # Enregistre la ligne dans la liste <saveFirst>
    saveRest = f.readlines()    # Sauvegarder tout le reste du fichier texte à partir de la fin du thème recherché dans la liste <saveRest>
    f.close()   # Fermer le fichier mot.txt
    # Ouverture dans le dossier fichier, le fichier mot.txt en écriture (écrase le fichier éxistant) avec l'encodage 'Utf-8'
    f = open("fichier/mot.txt", 'w', encoding='Utf-8')
    for ligne in saveFirst:     # Ajout de la 1er sauvegarde non utilisée dans le programme
        # Ecriture ligne par ligne (car f.write(saveFirst) retourne une erreur
        # car write() ne peux que écrire du <str> pas une <list>)
        f.write(ligne)
    # Ecriture de toutes les paires de mots avec leurs points de difficultés 
    # ligne par ligne : mot=saTradution.(pointsDeDifficultés)
    for i in range(len(mot1)):    #Pour i allant de 0 au nombre de mot total dans <mot1> 
        f.write(mot1[i] + '=' + mot2[i] + '.('+str(arrondie((faible[i]+1)/10)) + ')\n')    # Enregistrement en écriture des 3 listes
    f.write('\n')   # Ecriture d'une ligne vide
    for ligne in saveRest:  # Ajout de la 2eme sauvegarde 
        f.write(ligne)  # Ecriture ligne par ligne
    f.close()   # Fermeture du fichier mot.txt
    bestIndex = 0    # Initialise <int> <bestIndex> pour sauvegarder l'index de la meilleur note de <note>
    for i in range(len(note[0])):    # Analyse tout les éléments de la liste de rang 0 du tableau <note>
        # Si la note <i> de la liste du rang 0 du tableau <note> est plus grand que l'index <bestIndex> de <note>
        if note[0][i] > note[0][bestIndex]:
            bestIndex = i   # Affecte à <bestIndex> le rang <i> de la boucle for
    if len(note[0]) > 0 and note[0][bestIndex] > 0:    # Si la meilleur note est plus grande que 0/20
        now = datetime.now()    # now est une class contenant la date et l'heure actuelle de l'ordinateur
        noteSave[0].append(note[0][bestIndex])     # Ajoute au tableau <noteSave> la meilleure note
         # Ajoute au tableau <noteSave> la date de cette meilleure note
        noteSave[1].append("Le "+now.strftime('%d/%m/%y') + " à "+ note[1][bestIndex] + '\n')
    moyenne = 0    # Initialise la variable <int><moyenne> à 0
    if len(noteSave[0]) > 0:   # Si il y a au moins une note
        for i in noteSave[0]:  # Calcule la somme des notes
            moyenne += i       # Incrémente 1 à <i>
        moyenne = round(moyenne/len(noteSave[0]))    # Calcule la moyenne
    # Ouverture du fichier SCORE(<thème>).txt dans le dossier fichier en écriture avec l'encodage 'Utf-8'
    f = open(('score\SCORE ('+langue[2]+').txt'), 'w', encoding='Utf-8')
    # Ecriture avec encadré de la nouvelle base
    f.write("###############\nBASE NOTE = "+str(base)+'\nMOYENNE = '+str(moyenne)+'/'+str(base)+'\n###############\n\n')
    for i in range(len(noteSave[0])):   # Pour i allant de 0 au nombre de note du fichier texte
        # Ecriture du groupe de note (date + note + saut_de_ligne)
        f.write(noteSave[1][i]+"La meilleure note était : "+str(noteSave[0][i])+'/'+str(base)+'\n\n')
    f.close    # Fermeture du fichier SCORE(<thème>).txt
    # Enregistre avec un <write> les nouveau paramètres
    # Ouverture de settings.txt dans le dossier fichier fichier en écriture
    f = open("fichier/settings.txt", 'w', encoding='Utf-8')
    if settings[0][0]:    # Si le mode manuel est True (vrai)
        etat = 'True'     # Affecte ) <str><etat> 'True'
    else:   # Sinon (si le mode manuel est faux)
        etat = "False"    # Enregistre dans <etat> la chaine de caractère 'False'
    # Ecriture depuis le début du fichier settings.txt avec les nouvelles valeurs
    f.write("####GRAPHIQUE####\n"+"manuel="+etat+"\nx="+str(settings[0][1])+"\ny="+str(settings[0][2]))
    f.write("\n\n####POINT####\nfaute=+"+str(settings[1][0])+"\njuste="+str(settings[1][1]))

# Définie la fonction init() pour 'initialisation'
def init():
    # Cette fonction renvoie toutes les variables et listes du programme principale
    ################
    # FICHIER MOT  
    f = open("fichier/mot.txt", 'r', encoding='Utf-8')      # Ouverture en lecture du fichier mot.txt avec l'encodage 'Utf-8'
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
    print("\nQuel thème voulez vous choisir ?")
    for i in range(len(theme)):     # Affiche tout les thèmes disponibles
        # Chaque theme correspond à l'index 0 des listes dans la liste <theme>
        # On affiche aussi le nombre de mot dans chauqe theme :
        # Comme un 'mot' corresond au (mot) + (sa tradution) + (son point faible) il faut diviser le nombre total de valeur par 3
        # Avant cela ne pas oublier de soustraire 3 car on ne compte pas les 3 première valeurs correspondanttes au (theme) + (langue1) + (langue2)
        print(i+1,'. <',theme[i][0],'> [',theme[i][1],'=',theme[i][2],'] (',int((len(theme[i])-3)/3),'mots)',sep='')
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
        f = open("fichier/mot.txt", 'a', encoding='Utf-8')      # Ouverture en écriture (ajout) du fichier mot.txt avec l'encodage 'Utf-8'
        f.write("["+ newTheme+ "] ["+ l1+ '='+ l2+ "]\n\n")   # Enregistre directement le nouveau thème dans le fichier mot.txt...
        theme.append([newTheme, l1, l2])    # ... Et comme la lecture de ce fichier à déjà été effectuée ajouter à <theme> le nouveau thème avec ses langues associées
    else:    # Si le choix est dans les thèmes
        print("Vous avez choisi le thème <",theme[choix-1][0],'>', sep='')    # Afficher le thème choisi
    i = choix - 1   # Affecte à <i> la valeur de <choix> - 1 car une liste commence par l'index 0
    mot1 = []       # Initialisation de la liste <mot1> pour "mot"
    mot2 = []       # Initialisation de la liste <mot2> pour "traduction"
    faible = []     # Initialisation de la liste <faible> pour "point faible"
    # Chaque 'mot' du theme choisit est regroupé en 3 valeurs
        # 1.Mot
        # 2.Traduction
        # 3.Point faibles
        # Ainsi pour analyser toutes les valeur en une boucle
        # On divise par 3 la longeur de la liste <theme[i]> 
        # Puis ensuite avec une fonction affine (j*3+k) on peut se déplacer dans le 'groupe' de 'mot'
    for j in range(1, int(len(theme[i])/3)):
        mot1.append(theme[i][j*3])     # Premier index du groupe de 'mot'
        mot2.append(theme[i][j*3+1])   # Deuxième index du groupe de 'mot'
        faible.append(theme[i][j*3+2])   # Troisième index du groupe de 'mot'
    # Enlève les parenthèses de chaque index i de <faible> et multiplie chaque valeur par 10 après les avoir converties en <int>
    faible = [int(i[1:len(i)-1])*10 for i in faible]
    if not len(faible):  # Si le nombre de valeur dans <faible> ne renvoie PAS de valeur ce'ts à dire 0
        # Il faut absolument ajouter des mots de ce thème, sinon des erreurs de divisions se produiront dans test(), controle(),...
        # car comme il n'y a aucun mot, les procédures vont passer la boucle for (pour i allande de 0 à 0), puis afficher la note /base,
        # pour se faire il faut diviser par le nombre <n> de mot avant de multiplier par la <base>. 
        # Or ce <n> est égale à 0 et une division par 0 est impossible !
        input("\n/!\\ N'oubliez pas avant tout d'ajouter\ndes mots de ce thème dans les paramètres /!\\")  
    ###################
    # FICHIER SCORE
    langue = [theme[i][1],theme[i][2], theme[i][0]]  # Initialisation de la liste <langue>  pour "langue + theme"
    try:
        f = open(('score\SCORE ('+langue[2]+').txt'), 'r', encoding='Utf-8')     # Ouverture en mode lecture avec l'encodage 'Utf-8' du fichier score.txt
    except:     # Si le fichier n'éxiste pas, en créé un nouveau
        f = open(('score\SCORE ('+langue[2]+').txt'), 'w', encoding='Utf-8')
        f.write("###############\nBASE NOTE = 20\nMOYENNE = 0/20\n###############\n\n")      # Ecriture avec encadré de la nouvelle base
        f.close()   # Fermeture du fichier pour le re ouvrir en...
        f = open(('score\SCORE ('+langue[2]+').txt'), 'r', encoding='Utf-8')     # Ouverture en mode lecture avec l'encodage 'Utf-8' du fichier score.txt
    base = ''   # Initialise la variable <str> <base> à rien
    f.readline()  # Avance d'une ligne dans le fichier texte
    read = f.readline()     # Lecture de la deuxième ligne du fichier
    for i in range(12, len(read)):  # Pour i allant du premier caractère de la valeur de la base jusq'à son dernier caractère
        base += read[i]     # Ajoute à base par concaténation le caractère i de <read>
    for i in range(3):
        f.readline()
    save = f.readlines()   # Enregistre tout le reste des lignes non lu dans la liste <save>
    f.close()   # Ferme le fichier
    noteSave = [[], []]   # Initialisation de la liste <noteSave> pour enregistrer les date et heures de chaque scores enregistrés 
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
        # Affectation à <noteSave> la variable de <temp> séparée par le caractère '/'
        temp = read.split('/')    # Séparation de <temp> par le caractère '/' avec la fonction .split()
        noteSave[0].append(int(temp[0]))   # Ajoute à la liste <noteSave> la note de la ligne i du fichier 
        noteSave[1].append(save[i*3])  # Ajout de la date de la note dans la liste <noteSave>
    ######################
    # FICHIER SETTINGS
    f = open('fichier/settings.txt', 'r', encoding='Utf-8')     # Ouverture en mode lecture avec l'encodage 'Utf-8' du fichier settings.txt
    read = f.readlines()    # Enregistre le fichier dans la liste <read>
    f.close()          # Ferme le fichier settings.txt
    note = [[], []]    # Initialise la liste <note> pour les paramètres
    etat = read[1][7:-1]    # Affecte à <str><etat> la valeur de la 2eme ligne 
    if etat == 'True':      # Si la chaine de caractère de <etat> est égale à 'True' 
        note[0].append(True)    # Les dimmenssions du repère correspondes au fichier settings.txt
    else:   # Le mode manuel est faux 'False'
        note[0].append(False)             # Les dimmensions sont en fonction de la taille de la fenêtre
    note[0].append(int(read[2][2:-1]))    # Ajoute un nouvelle index avec la dimmension x pour le graphique
    note[0].append(int(read[3][2:-1]))    # 4:-1 correpsond au dimmension y du graphique
    note[1].append(int(read[6][6:-1]))    # Ajoute un nouvelle index avec l'incrément du point de faiblesse si mauvaise réponse
    note[1].append(int(read[7][6:]))      # 6: correspond à l'incrément du point de faiblesse si bonne réponse
    return mot1, mot2, faible, langue, noteSave, [[], []], note, int(base)      # Renvoie toutes les tableaux, listes, variables et valeurs demandé par l'appelle de la fonction init()

# PROGRAMME PRINCIPALE
from random import randint      # Importation de la fontion randint() du module random
from datetime import datetime   # Importation de la focntion datetime du module datetime
import turtle as t      # Importation du module turtle, on l'appelle avec t.fonction()
# Affiche un messsage de bienvenue
print("Bienvenue dans <LE Boss En Langue> !")
# Initialise toutes les listes et variables avec la fonction init()
motG1, motG2, pointF, langue, noteSave, note, settings, base  = init()
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
    # saisir le choix dans la variable <str><choix>
    choix = input("Lancer le mode : ")
    print()    # saute une ligne
    # compare le choix à 8 conditions différentes en <str> (pour empêcher une erreur si un caractère est entré)
    if choix == '1':
        # Appel de la procédure apprendre() avec comme arguments motG1 et motG2
        apprendre(motG1, motG2)
    elif choix == '2':
        # Appel de la procédure reviser() avec comme arguments motG1, motG2 et langue
        reviser(motG1, motG2, langue)
    elif choix == '3':
        # Appel de la procédure test() avec comme arguments motG1, motG2 et langue
        test(motG1, motG2, langue)
    elif choix == '4':
        # Appel de la procédure controle() avec comme arguments motG1, motG2, note, pointF et settings[1]
        controle(motG1, motG2, note, pointF, settings[1])
    elif choix == '5':
        # Appel de la procédure hard() avec comme arguments motG1, motG2, pointF et langue
        hard(motG1, motG2, pointF, langue)
    elif choix == '6':
        # Appel de la procédure pendu() avec comme arguments motG1, motG2 et langue
        pendu(motG1, motG2, langue)
    elif choix == '7':
        # Appel de la procédure parametre() avec comme arguments motG1, motG2, pointF, langue, note, et noteSave
        parametre(motG1, motG2, pointF, langue, note, noteSave, settings)
    elif choix == '8':
        # Appel de la procédure graphique() avec comme arguments langue, noteSave, note, settings[0], et base
        graphique(note, noteSave, settings[0], base)
    elif choix == '9':
        play = False    # Affecte à play l'état False pour sortir de la boucle
    else:    # Si aucune des conditions ci dessus n'a été respectées alors
        # Informe que le choix saisie est invalide
        print("Choix inconnu, erreur...")
# Afficher "A bientôt" afin d'inciter le joueur à revenir
print("A bientôt !")
# Appel de la fonction save() avec comme arguments toutes les variables et listes
save(motG1, motG2, pointF, langue, noteSave, note, settings, base)
