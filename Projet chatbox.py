import time
from playsound import playsound
from PIL import Image


les_animaux = [
    [0, "chat 😺"],
    [0, "chien 🐶"],
    [0, "cochon d'inde 🐹"],
    [0, "poisson rouge 🐟"],
]

# zoobot dit bonjour
user_name = input("Hello!! \nComment tu t'appelles ?:\nTape ici:>>>>")
time.sleep(2)
print(">>>>>>>>>>>>")
print("Salut " + user_name.upper() + "! \nMoi c'est zoobot.")
print(">>>>>>>>>>>>")
time.sleep(2)

print('')
print('                                   ┏┷┓         ┏┷┓')
print('                                  ┏┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┓')
print('                                  ┃   (°)    (°)  ┃')
print('                                  ┃       m       ┃')
print('                                  ┃      ___      ┃')
print('                                   \     ╰╯      /')
print('                                    \___________/')
print('                                        ╟   ╢')
print('              ╔══════════════════════════════════════════════════════════════╗')
print('══════════════║ Veux-tu connaître quel est ton animal de compagnie idéal ?   ║')
print('              ╚══════════════════════════════════════════════════════════════╝')
time.sleep(3)

def  question_0():
    question = input("oui/non:\nTape ici:>>>> ")
    if (question.lower()) == "oui":
        time.sleep(2)
        print(">>>>>>>>>>>>>>>>>")
        print("Alors c'est parti! 🚀")
        print("")
        time.sleep(2)
    elif (question.lower()) == "non":
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("T'es sûr.e ? Peut être à la prochaine... 👋")
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
    print('              ╔══════════════════════════════════════════════════════════════╗')
    print('══════════════║ Combien de temps peux-tu dedier à ton animal?                ║')
    print('              ╚══════════════════════════════════════════════════════════════╝')
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
        print("J'ai pas compris ta réponse...\n")
        time.sleep(1)
        question_1()


question_1()
time.sleep(2)
print('***********')
print("Ok, super! 👍")
print('***********')
print("")
time.sleep(2)


def question_2():
    print('              ╔═════════════════════════════════════╗')
    print('══════════════║ Aimes-tu le contact?                ║')
    print('              ╚═════════════════════════════════════╝')
    q_2 = input("a: peu \nb: moyen \nc: beaucoup\nTape ici ta réponse:>>>>")
    if (q_2.lower()) == "a" or (q_2.lower()) =="peu":
        les_animaux[2][0] += 1
        les_animaux[3][0] += 2
    elif (q_2.lower()) == "b" or (q_2.lower()) == "moyen":
        les_animaux[0][0] += 2
    elif (q_2.lower()) == "c" or (q_2.lower()) == "beaucoup":
        les_animaux[1][0] += 2
        les_animaux[0][0] += 1
    else:
        print("Ok, mais... soyons plus précis:\n")
        time.sleep(1)
        question_2()


question_2()
time.sleep(2)
print('*************')
print("Très bien 😉!!!")
print('*************')
print("")
time.sleep(2)


def question_3():
    print('              ╔═════════════════════════════════════╗')
    print('══════════════║ Est-ce spacieux chez toi ?          ║')
    print('              ╚═════════════════════════════════════╝')
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
        print("Heu... c'est pas très claire\n")
        print('')
        time.sleep(1)
        question_3()


question_3()
time.sleep(2)
print('*************')
print("D'accord 😄")
print('*************')
print("")
time.sleep(2)


def question_4():
    print('              ╔═════════════════════════════════════╗')
    print('              ║Un dimanche, tu préfères:            ║')
    print('══════════════║a: Faire un footing                  ║')
    print('              ║b: Te promener dans un parc          ║')
    print('              ║c: Rester au chaud avec un bouquin ? ║')
    print('              ╚═════════════════════════════════════╝')
    print('')
    q_4 = input("Tape ici ta réponse:>>>>")
    if (q_4.lower()) == "a" or (q_4.lower()) == "Faire un footing":
        les_animaux[1][0] += 2
    elif (q_4.lower()) == "b" or (q_4.lower()) == "me promener dans un parc" or (q_4.lower()) == "se promener dans un parc":
        les_animaux[0][0] += 1
        les_animaux[2][0] += 1
    elif (q_4.lower()) == "c" or (q_4.lower()) == "rester au chaud avec un bouquin":
        les_animaux[0][0] += 2
        les_animaux[3][0] += 1
    else:
        print("J'ai pas bien compris ta réponse\n")
        print('')
        time.sleep(2)
        question_4()


question_4()
time.sleep(2)
print('*************')
print("Ok, alors la suite 🚀!")
print('*************')
print("")
time.sleep(2)


def question_5():
    print('              ╔═════════════════════════════════════╗')
    print('══════════════║ As tu des enfants?                  ║')
    print('              ╚═════════════════════════════════════╝')
    q_5 = input("oui/non:\nTape ici:>>>>")
    if (q_5.lower()) == "oui":
        les_animaux[1][0] += 2
        les_animaux[2][0] += 2
    elif (q_5.lower()) == "non":
        les_animaux[0][0] += 2
        les_animaux[3][0] += 2
    else:
        print("Je suis pas sûr si j'ai bien compris ta réponse.\n")
        print('')
        time.sleep(1)
        question_5()


question_5()
time.sleep(2)
print('*************')
print("Génial, on continue ✨!!")
print('*************')
print("")
time.sleep(2)


def question_6():
    print('              ╔═════════════════════════════════════╗')
    print('              ║Tu es plutôt :                       ║')
    print('══════════════║a: AC/DC                             ║')
    print('              ║b: LADY GAGA                         ║')
    print('              ║c: CHOPIN                            ║')
    print('              ╚═════════════════════════════════════╝')
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
        print("Desolé, j'ai pas compris ta réponse.\n")
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

print("C’est fini " + user_name.upper() + ", voici le résultat: 🎉!!")
time.sleep(3)
les_animaux.sort(reverse=True)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('              ╔════════════════════════════════════════════════════════════════════════╗')
print("══════════════  Ton animal compatible c'est le: " + les_animaux[0][1].upper() + '!!     ')
print('              ╚════════════════════════════════════════════════════════════════════════╝')
print("")
# emoticon ou dessin animal ou félicitation
time.sleep(3)
print("Voici tes autres posibilités, en ordre descendant:")
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
    print('              ╔══════════════════💡═════════════════╗')
    print('              ║Ok... Aurais-tu préferé...❓:        ║')
    print('              ║1: licorne 🦄                        ║')
    print('══════════════║2: pikachu 🐭                        ║')
    print('              ║3: vélociraptor 🦎                   ║')
    print('              ║4: dragon 🐉                         ║')
    print('              ╚══════════════════💡═════════════════╝')
    print('')
    my_pet = input("Tape ici ta réponse:>>>>")
    if my_pet == "1" or (my_pet.lower()) == "licorne":
        playsound("licorne.wav")
        print("Au revoir !")
    elif my_pet == "2" or (my_pet.lower()) == "pikachu" or (my_pet.lower()) == "picachu":
        playsound("pikachu.wav")
        print("Au revoir !")
    elif my_pet == "3" or (my_pet.lower()) == "vélociraptor" or (my_pet.lower()) == "velociraptor":
        playsound("dragon.wav")
        print("Au revoir !")
    elif my_pet == "4" or (my_pet.lower()) == "dragon":
        playsound("dragon.wav")
        print("Au revoir !")
    else:
        print("Peut être un robot alors! 🤖")
        print("A la prochaine !")


imageLue = Image.open('comic.jpg')
imageLue.show()
time.sleep(1)
