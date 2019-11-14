from random import randint
nom = input("Thème : ")
base = 20
moyenne = 10
list5 = [[],[]]
mois = 10
jour = 15
heure = 0
tempJ = 0
tempH = 0
n = int(input("Combien de note ? : "))
for i in range(n):
    print("note ", i+1,' : ',sep='', end='')
    note = input()
    if jour == tempJ:
        heure += randint(1, 4)
    else:
        heure = randint(8, 13)
    list5[0].append(note)
    list5[1].append("Le "+str(jour)+'/'+str(mois)+"/19 à "+str(heure)+":"+str(randint(10, 59))+'\n')
    tempJ = jour
    tempH = heure
    jour += randint(0, 1)
    if jour > 31:
        jour = 1
        mois = 11

f = open(('..\score\SCORE ('+nom+').txt'), 'w', encoding='Utf-8')    # Ouverture du fichier score.txt en écriture avec l'encodage 'Utf-8'
f.write("###############\nBASE NOTE = "+str(base)+'\nMOYENNE = '+str(moyenne)+'/'+str(base)+'\n###############\n\n')      # Ecriture avec encadré de la nouvelle base
for i in range(len(list5[0])):   # Pour i allant de 0 au nombre de note du fichier texte
    f.write(list5[1][i]+"La meilleure note était : "+str(list5[0][i])+'/'+str(base)+'\n\n')  # Ecriture du groupe de note (date, note, saut de ligne)
