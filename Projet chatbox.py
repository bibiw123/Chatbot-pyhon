import time
from playsound import playsound
from PIL import Image


les_animaux = [
    [0, "chat ๐บ"],
    [0, "chien ๐ถ"],
    [0, "cochon d'inde ๐น"],
    [0, "poisson rouge ๐"],
]

# zoobot dit bonjour
user_name = input("Hello!! \nComment tu t'appelles ?:\nTape ici:>>>>")
time.sleep(2)
print(">>>>>>>>>>>>")
print("Salut " + user_name.upper() + "! \nMoi c'est zoobot.")
print(">>>>>>>>>>>>")
time.sleep(2)

print('')
print('                                   โโทโ         โโทโ')
print('                                  โโทโทโทโทโทโทโทโทโทโทโทโทโทโทโทโ')
print('                                  โ   (ยฐ)    (ยฐ)  โ')
print('                                  โ       m       โ')
print('                                  โ      ___      โ')
print('                                   \     โฐโฏ      /')
print('                                    \___________/')
print('                                        โ   โข')
print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
print('โโโโโโโโโโโโโโโ Veux-tu connaรฎtre quel est ton animal de compagnie idรฉal ?   โ')
print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
time.sleep(3)

def  question_0():
    question = input("oui/non:\nTape ici:>>>> ")
    if (question.lower()) == "oui":
        time.sleep(2)
        print(">>>>>>>>>>>>>>>>>")
        print("Alors c'est parti! ๐")
        print("")
        time.sleep(2)
    elif (question.lower()) == "non":
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("T'es sรปr.e ? Peut รชtre ร  la prochaine... ๐")
        question_0()

    else:
        print(">>>>>>>>>>>>")
        print("On recommence!")
        time.sleep(2)
        question_0()

question_0()
time.sleep(2)


# on commence le questionnaire

def question_1():
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('โโโโโโโโโโโโโโโ Combien de temps peux-tu dedier ร  ton animal?                โ')
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    q_1 = input('a: peu \nb: moyen \nc: beaucoup:\nTape ici:>>>>')
    if (q_1.lower()) == "a" or (q_1.lower()) == "peu":
        les_animaux[0][0] += 1
        les_animaux[2][0] += 1
        les_animaux[3][0] += 2
    elif (q_1.lower()) == "b" or (q_1.lower()) == "moyen":
        les_animaux[0][0] += 2
        les_animaux[2][0] += 1
    elif (q_1.lower()) == "c" or (q_1.lower()) == "beacoup":
        les_animaux[1][0] += 2
        les_animaux[0][0] += 1
    else:
        print("J'ai pas compris ta rรฉponse...\n")
        time.sleep(1)
        question_1()


question_1()
time.sleep(2)
print('***********')
print("Ok, super! ๐")
print('***********')
print("")
time.sleep(2)


def question_2():
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('โโโโโโโโโโโโโโโ Aimes-tu le contact?                โ')
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    q_2 = input("a: peu \nb: moyen \nc: beaucoup\nTape ici ta rรฉponse:>>>>")
    if (q_2.lower()) == "a" or (q_2.lower()) =="peu":
        les_animaux[2][0] += 1
        les_animaux[3][0] += 2
    elif (q_2.lower()) == "b" or (q_2.lower()) == "moyen":
        les_animaux[0][0] += 2
    elif (q_2.lower()) == "c" or (q_2.lower()) == "beaucoup":
        les_animaux[1][0] += 2
        les_animaux[0][0] += 1
    else:
        print("Ok, mais... soyons plus prรฉcis:\n")
        time.sleep(1)
        question_2()


question_2()
time.sleep(2)
print('*************')
print("Trรจs bien ๐!!!")
print('*************')
print("")
time.sleep(2)


def question_3():
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('โโโโโโโโโโโโโโโ Est-ce spacieux chez toi ?          โ')
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    q_3 = input("a: oui\nb: non\nc: pas trop\nTape ici:>>>>")
    if (q_3.lower()) == "oui" or (q_3.lower()) =="a":
        les_animaux[1][0] += 2
        les_animaux[0][0] += 1
    elif (q_3.lower()) == "non" or (q_3.lower()) =="b":
        les_animaux[3][0] += 2
        les_animaux[0][0] += 1
    elif (q_3.lower()) == "pas trop" or (q_3.lower()) =="c":
        les_animaux[2][0] += 1
        les_animaux[0][0] += 2
        les_animaux[3][0] += 1
    else:
        print("Heu... c'est pas trรจs claire\n")
        print('')
        time.sleep(1)
        question_3()


question_3()
time.sleep(2)
print('*************')
print("D'accord ๐")
print('*************')
print("")
time.sleep(2)


def question_4():
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('              โUn dimanche, tu prรฉfรจres:            โ')
    print('โโโโโโโโโโโโโโโa: Faire un footing                  โ')
    print('              โb: Te promener dans un parc          โ')
    print('              โc: Rester au chaud avec un bouquin ? โ')
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('')
    q_4 = input("Tape ici ta rรฉponse:>>>>")
    if (q_4.lower()) == "a" or (q_4.lower()) == "Faire un footing":
        les_animaux[1][0] += 2
    elif (q_4.lower()) == "b" or (q_4.lower()) == "me promener dans un parc" or (q_4.lower()) == "se promener dans un parc":
        les_animaux[0][0] += 1
        les_animaux[2][0] += 1
    elif (q_4.lower()) == "c" or (q_4.lower()) == "rester au chaud avec un bouquin":
        les_animaux[0][0] += 2
        les_animaux[3][0] += 1
    else:
        print("J'ai pas bien compris ta rรฉponse\n")
        print('')
        time.sleep(2)
        question_4()


question_4()
time.sleep(2)
print('*************')
print("Ok, alors la suite ๐!")
print('*************')
print("")
time.sleep(2)


def question_5():
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('โโโโโโโโโโโโโโโ As tu des enfants?                  โ')
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    q_5 = input("oui/non:\nTape ici:>>>>")
    if (q_5.lower()) == "oui":
        les_animaux[1][0] += 2
        les_animaux[2][0] += 2
    elif (q_5.lower()) == "non":
        les_animaux[0][0] += 2
        les_animaux[3][0] += 2
    else:
        print("Je suis pas sรปr si j'ai bien compris ta rรฉponse.\n")
        print('')
        time.sleep(1)
        question_5()


question_5()
time.sleep(2)
print('*************')
print("Gรฉnial, on continue โจ!!")
print('*************')
print("")
time.sleep(2)


def question_6():
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    print('              โTu es plutรดt :                       โ')
    print('โโโโโโโโโโโโโโโa: AC/DC                             โ')
    print('              โb: LADY GAGA                         โ')
    print('              โc: CHOPIN                            โ')
    print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
    q_6 = input("Tape ici:>>>>")
    if (q_6.lower()) == "a" or (q_6.lower()) == "ac/dc":
        les_animaux[1][0] += 2
    elif (q_6.lower()) == "b" or (q_6.lower()) == "lady gaga":
        les_animaux[0][0] += 0
        les_animaux[2][0] += 1
    elif (q_6.lower()) == "c" or (q_6.lower()) == "chopin":
        les_animaux[0][0] += 2
        les_animaux[3][0] += 2
    else:
        print("Desolรฉ, j'ai pas compris ta rรฉponse.\n")
        print('')
        time.sleep(1)
        question_6()


question_6()
time.sleep(2)
print('********')
print("Super!")
print('********')
print("")
time.sleep(2)

print("Cโest fini " + user_name.upper() + ", voici le rรฉsultat: ๐!!")
time.sleep(3)
les_animaux.sort(reverse=True)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
print("โโโโโโโโโโโโโโ  Ton animal compatible c'est le: " + les_animaux[0][1].upper() + '!!     ')
print('              โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ')
print("")
# emoticon ou dessin animal ou fรฉlicitation
time.sleep(3)
print("Voici tes autres posibilitรฉs, en ordre descendant:")
time.sleep(2)
print(les_animaux[0][0], les_animaux[0][1])
print(les_animaux[1][0], les_animaux[1][1])
print(les_animaux[2][0], les_animaux[2][1])
print(les_animaux[3][0], les_animaux[3][1])
print('********************************')
time.sleep(3)
question_final = input("Es tu satisfait de ton animal ? \noui / non:\nTape ici:")
if (question_final.lower()) == "oui":
    time.sleep(2)
    print("Super, bon courage avec ton nouveau compagnon!!")

else:
    print('              โโโโโโโโโโโโโโโโโโโ๐กโโโโโโโโโโโโโโโโโโ')
    print('              โOk... Aurais-tu prรฉferรฉ...โ:        โ')
    print('              โ1: licorne ๐ฆ                        โ')
    print('โโโโโโโโโโโโโโโ2: pikachu ๐ญ                        โ')
    print('              โ3: vรฉlociraptor ๐ฆ                   โ')
    print('              โ4: dragon ๐                         โ')
    print('              โโโโโโโโโโโโโโโโโโโ๐กโโโโโโโโโโโโโโโโโโ')
    print('')
    my_pet = input("Tape ici ta rรฉponse:>>>>")
    if my_pet == "1" or (my_pet.lower()) == "licorne":
        playsound("licorne.wav")
        print("Au revoir !")
    elif my_pet == "2" or (my_pet.lower()) == "pikachu" or (my_pet.lower()) == "picachu":
        playsound("pikachu.wav")
        print("Au revoir !")
    elif my_pet == "3" or (my_pet.lower()) == "vรฉlociraptor" or (my_pet.lower()) == "velociraptor":
        playsound("dragon.wav")
        print("Au revoir !")
    elif my_pet == "4" or (my_pet.lower()) == "dragon":
        playsound("dragon.wav")
        print("Au revoir !")
    else:
        print("Peut รชtre un robot alors! ๐ค")
        print("A la prochaine !")


imageLue = Image.open('comic.jpg')
imageLue.show()
time.sleep(1)
