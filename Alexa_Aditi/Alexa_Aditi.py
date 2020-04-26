import pygame
import pyttsx3

import speech_recognition as speech

engine = pyttsx3.init()
pygame.init()



alexa = {
    "olympics": "The olympics is an international sporting event which has been currently postponed to 2021 due to the covid - 19 outbreak. One of the best participants so far has been Micheal Phelphs who competes in swimming and has won 23 gold medals.",

    "premier": "The Premier League is a football tournament over England with the defending champions for the past 2 years being Manchester City",

    "running": "Usain Bolt is the current world record holder for the 100 metres and the 200 metres sprint. His record for 100 metres being 9.58 seconds and his record for the 200 metres being 19.19 seconds. He has earned a total of 9 gold medals in the olympics",

    "ipl": "The Indian Premier League is a cricket tournament held all across India. The current defending champions are Mumbai Indians under the coachmanship of Mahela Jayawardene. This year's IPL has been postponed due to the covid-19 outbreak",

    "asian": "The Asian Games is a multisport event held for Asian countries every 4 years. The next Asian Games will be held in 2022 in Hangzhou, Zhejiang, China .",

    "long": "The long jump is a track and field event in which athletes combine speed, strength and agility in an attempt to leap as far as possible from a take off point. The world record being set by Mike Powell which is 8.95 metres.",

    "wimbledon": "The Wimbledon is one of the most prestigious tennis tournaments in the world. It has been held at the All England Club in Wimbledon, London, since 1877 and is played on outdoor grass courts. The defending champion for the men's singles being Novak Djokovic. This year's tournament has been cancelled due to the covid - 19 outbreak.",

    "cycling": "Cycling is a recreational activity which has tournaments mostly in Europe. The largest being UCI World Tour and Tour de France.",

    "formula": "Formula One  is the highest class of single-seater auto racing held since 1950. The defending champion being Lewis Hamilton from Mercedes Benz.",

    "hockey": "The Hockey World Cup is an international field hockey competition organised by the International Hockey Federation (FIH). The current defending champions being Belgium although Pakistan has won the most amount of times."}


def display(bg):
    width = 900
    height = 575
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Alexa')
    if bg == 1:
        img = pygame.image.load("screen1.png").convert_alpha()

    elif bg == 2:
        img = pygame.image.load("screen.png").convert_alpha()

    elif bg == 3:
        img = pygame.image.load("screen2.png").convert_alpha()


    screen.blit(img, (0, 0))






def start_listening():

        listen = True

        r = speech.Recognizer()
        display(3)
        pygame.display.update()
        with speech.Microphone() as source:

            r.adjust_for_ambient_noise(source)



            print("Speak:")
            display(3)
            pygame.display.update()



            audio = r.listen(source)


        command = r.recognize_google(audio).lower()

        print("You said" + command)
        words = command.split()
        length = len(words)
        dict = list(alexa)
        if listen == True:
            for i in range(length):
                for j in range(10):
                    if words[i] == dict[j]:

                        keyword = words[i]

                        return keyword

                        listen = False





def image(keyword):

    image = pygame.image.load(keyword + ".png").convert_alpha()
    screen.blit(image, (175, 175))




ask = False
running = True

while running:
    display(1)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:

            ask = True


        if event.key == pygame.K_x:
            ask = False
            running = False



    if ask == True:




        keyword = start_listening()

        display(2)



        image(keyword)

        pygame.display.update()

        engine.say(alexa[keyword])
        engine.runAndWait()

        ask = False
