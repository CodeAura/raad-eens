import random
import time

time.sleep(0.5)
print("     Welkom bij getal raden      ")
print("---------------------------------")
print("  Noem een getal tussen de 1000  ")
print("---------------------------------")
time.sleep(2)
print(
    ""
)
guess = -1
ronde = 1
score = 0
while ronde <= 20:
    print('Ronde' + str(ronde))
    getal = random.randint(1,1000)
    kans = 1
    while getal != guess:
        guess = int(input(str(kans) + ': '))
        
        if guess < getal:
            print('Getal zit Hoger')
            if(getal - guess) <= 20:
                print('Je bent heel warm!')
            elif(getal - guess) <= 50:
                print('Je bent warm')
        elif guess > getal:
            print('Getal zit Lager')
            if(guess - getal) <= 20:
                print('Je ben heel erg warm!')
            elif(guess - getal <= 50):
                print('Je bent warm')
        else:
            print('Geraden! ')
            score = score + 1
        kans = kans + 1
        if kans > 10:
            break
    print('Het getal was: ' + str(getal))
    if ronde >= 20:
        break
    print('Score: ' + str(score))
    antwoord =input("wil je nog een keer raden? ja/nee ")
    if not (antwoord == 'ja' or antwoord == 'Ja'):
        break
    ronde = ronde + 1
print('End')
print('Je eindscore is: ' + str(score))