import pygame
import pyttsx3
import random
import speech_recognition as speech

engine = pyttsx3.init()
pygame.init()



alexa = {
    "olympics":["img", "The olympics is an international sporting event which has been currently postponed to 2021 due to the covid - 19 outbreak. One of the best participants so far has been Micheal Phelphs who competes in swimming and has won 23 gold medals."],

    "premier": ["img","The Premier League is a football tournament over England with the defending champions for the past 2 years being Manchester City"],

    "running":["img", "Usain Bolt is the current world record holder for the 100 metres and the 200 metres sprint. His record for 100 metres being 9.58 seconds and his record for the 200 metres being 19.19 seconds. He has earned a total of 9 gold medals in the olympics"],

    "ipl": ["img","The Indian Premier League is a cricket tournament held all across India. The current defending champions are Mumbai Indians under the coachmanship of Mahela Jayawardene. This year's IPL has been postponed due to the covid-19 outbreak"],

    "games": ["img","The Asian Games is a multisport event held for Asian countries every 4 years. The next Asian Games will be held in 2022 in Hangzhou, Zhejiang, China ."],

    "long": ["img","The long jump is a track and field event in which athletes combine speed, strength and agility in an attempt to leap as far as possible from a take off point. The world record being set by Mike Powell which is 8.95 metres."],

    "wimbledon": ["img","The Wimbledon is one of the most prestigious tennis tournaments in the world. It has been held at the All England Club in Wimbledon, London, since 1877 and is played on outdoor grass courts. The defending champion for the men's singles being Novak Djokovic. This year's tournament has been cancelled due to the covid - 19 outbreak."],

    "cycling": ["img","Cycling is a recreational activity which has tournaments mostly in Europe. The largest being UCI World Tour and Tour de France."],

    "formula": ["img","Formula One  is the highest class of single-seater auto racing held since 1950. The defending champion being Lewis Hamilton from Mercedes Benz."],

    "hockey": ["img","The Hockey World Cup is an international field hockey competition organised by the International Hockey Federation (FIH). The current defending champions being Belgium although Pakistan has won the most amount of times."],

    "coronavirus" : ["img","The first case of the Corona virus emerged in Wuhan, China in december 2019.As for ninth april 2020 . There are 88,538 deaths out of 14,96,055 cases , US being the worst affected by it."],

    "ebola" : ["", "Ebola originated in Congo.It started in February 2014, Liberia being the worst effected by it.This virus has caused 11,325 deaths."],

    "swine" : ["", "Started in Veracruz, Mexico on April 2009 was the swine flu.It caused 18,036 deaths worldwide."],

    "aids" :["","AIDS was first indentified in Congo in 1976. This disease has caused 36 million deaths since 1981."],

    "spanish" : ["", "As the name suggests, this disease originated in Spain in 1918.The worst affected place being Western Samoa. This flu caused 5 crore deaths"],

    "plague" : ["" , "The plague of justinion thought to have killed half of Europes population.It started in 541AD .Its death toll is 25million"],

    "flu" : ["", "Flu originated in Asia,it started in 1968. Its death toll  is 1 milion.It killed 15% of Hong Kongs population at that time."],

    "asian" : ["", "Asian flu originated in China.It started in 1956.Its death toll being 2 million.The worst affected being USA ."],

    "cholera" : ["","This  pandemic orignated in India, it started in 1852.Its death toll is 1 million.John Snow found the cure for this virus in 1860"],

    "black" : ["" , "The black death originated in China in 1347. Over 50 million people were killed, wiping over 60% of Europes population.This disease came to a stop in 1353. This was amongst the most dangerous pandemics history has ever faced."],

    "jallianwala" : ["img" , "Jallianwala Bagh Massacre, Jallianwala also spelled Jallianwalla, also called Massacre of Amritsar, incident on April 13, 1919."],

    "arrival" : ["", "Arrival of the British and the establishment of British East India Company was the outcome of the Portuguese traders who earn enormous profit by selling their merchandise in India. "],

    "rajput" : ["img" , "The principal Rajput states of Mewar (Udaipur) Marwar (Jodhpur) and Amber (Jaipur) were alienated from the Mughal Empire due to the religious and administrative policies of Aurangzeb."],

    "rule" : ["", "Murshid Quli Khan was appointed as the Diwan of Bengal by Aurangzeb. Governor Murshid Quil Khan (1717-1727 A.D.) transferred the capital from Dacca to Murshidabad."],

    "shivaji" : ["img", "The Maratha Empire or the Maratha Confederacy is located in the south west of present-day India. They ruled from 1674 to 1818 and extended their territories. "],

    "sikhs" : ["" , "The Sikhs had not been able to found a state during the reign of Aurangzeb, though they had been organised into a fighting group by the tenth and the last guru-Guru Gobind Singh. After his death the Sikhs found a capable leader in Banda Bahadur (A.D.1708-1716). He organised a large number of Sikhs and captured Sirhind."],

    "astronomy" : ["img", "Astronomy is the study of celestial objects such as stars,planets etc and phenonema that originate outside the Earth's atmosphere"],

    "copernicus" : ["img" , "Nicolaus Copernicus proposed a Heliocentric system"],

    "galileo" : ["" , "Galileo Galilei resurfaced heliocentrism, and discovered four of Jupiter's moons: Io , Europa, Ganymede and Callisto."],

    "heliocentrism" : ["" ,"  The idea that the Sun is at the centre and not the Earth."],

    "andromeda" : ["", "The Andromeda Galaxy, also known as Messier 31, is a barred spiral galaxy approximately 2.5 million lightyears from Earth and the nearest major galaxy to the MilkyWay."],

    "variable" : ["" , "Any stars whose brightness fluctuates as seen from Earth are variable stars"],

    "halley's" : ["" , "Halley's comet can be seen around once every 74 years. First discovered by Edmond Halley."],

    "nebula" : ["" , "A nebula is cloud of gas and dust in space. It forms new stars."],

    "constellations" : ["" , "A constellation is an area in the celestial sphere in which a group of stars forms an imaginary outline or pattern. First noted by Babylonians."],

    "supermoon" : ["" ,  "A point in time in which the moon is closer to the Earth.  The moon appears larger than usual."]}
int = 0
num = 0
def display(bg):

    width = 900
    height = 575
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Alexa')
    if bg == 1:

        img = pygame.image.load("screen" + str(num) + ".png").convert_alpha()

    elif bg == 2:
        img = pygame.image.load("display" + str(num)  +".png").convert_alpha()

    elif bg == 3:
        img = pygame.image.load( str(num) + ".png").convert_alpha()


    screen.blit(img, (0, 0))


def quiz():
    i = 0
    width = 900
    height = 575
    white = (255,255,255)
    questions = ["What is the largest moon of Juptier?",
                 "What is the highest waterfall?" ,
                 "How many lines of longitude are there?" ,
                 "Which country is the most socially protected country?",
                 "Which country has the most export?" ]
    answers = ["a" , "a" , "c" , "c" , "a"]
    options = [["Ganymede" , "Europa" ,"Callisto"],["Angel Falls" , "Nigara Falls" , "Iguazu Falls"],["181", "360", "180"],
            ["Venenzuela" , "Brazil", "Austria"], ["China","United States of America" , "Japan" ]]


    recieved = False
    next = True

    score = 0
    while next :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                pygame.quit()
                quit()

        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Alexa')
        img = pygame.image.load("quiz.png").convert_alpha()
        screen.blit(img,(0,0))
        font = pygame.font.Font('Comfortaa.ttf', 30)
        if i < 5 :
            if recieved == True:

                if answer == answers[i]:
                    score = score + 1
                    print(score)
                i = i + 1
                if i < 5:
                    text = font.render(questions[i], True, white)
                    text_width = text.get_width()
                    screen.blit(text, (width / 2 - text_width / 2, 100))
                    option_a = font.render(options[i][0], True, white)
                    option_b = font.render(options[i][1], True, white)
                    option_c = font.render(options[i][2], True, white)

                    screen.blit(option_a, (250, 205))
                    screen.blit(option_b, (250, 305))
                    screen.blit(option_c, (250, 405))

                recieved = False
            if i == 0 :

                text = font.render(questions[0], True, white)
                text_width = text.get_width()
                screen.blit(text, (width / 2 - text_width / 2, 100))
                option_a = font.render(options[0][0], True, white)
                option_b = font.render(options[0][1], True, white)
                option_c = font.render(options[0][2], True, white)

                screen.blit(option_a, (250, 205))
                screen.blit(option_b, (250, 305))
                screen.blit(option_c, (250, 405))

        #for i in range (0,5):


            mouse = pygame.mouse.get_pos()
            if 155 < mouse[0] < 216 and 390 < mouse[1] < 453:
                option3 = pygame.image.load("C1.png").convert_alpha()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        answer = "c"
                        print(answer)
                        recieved = True
            else :
                option3 = pygame.image.load("C.png").convert_alpha()

            screen.blit(option3, (100, 350))

            if 155 < mouse[0] < 216 and 293 < mouse[1] < 353:
                option2 = pygame.image.load("B1.png").convert_alpha()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        answer = "b"
                        print(answer)
                        recieved = True
            else :
                option2 = pygame.image.load("B.png").convert_alpha()


            screen.blit(option2, (100, 250))
            if 155 < mouse[0] < 216 and 194 < mouse[1] < 254:
                option1 = pygame.image.load("A1.png").convert_alpha()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        answer = "a"
                        print(answer)
                        recieved = True
            else :
                option1 = pygame.image.load("A.png").convert_alpha()


            screen.blit(option1, (100, 150))




            screen.blit(text, (width / 2 - text_width / 2, 100))
            screen.blit(option_a, (250, 205))
            screen.blit(option_b, (250, 305))
            screen.blit(option_c, (250, 405))
            pygame.display.update()

        if i == 5:
            font = pygame.font.Font('Comfortaa.ttf', 100)
            screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption('Alexa')
            img = pygame.image.load("quiz1.png").convert_alpha()
            screen.blit(img, (0, 0))


            text = font.render("Your score", True, white)
            text_width = text.get_width()
            screen.blit(text, (width / 2 - text_width / 2, 100))
            text2 = font.render(str(score) + "/5", True, white)
            text2_width = text2.get_width()
            screen.blit(text2, (width / 2 - text2_width / 2, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        next = False





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

                for j in range(36):

                    if words[i] == dict[j]:
                        keyword = words[i]
                        if words[i] == "asian" :
                            if words[i + 1] == "games" :
                                keyword = "games"




                        return keyword

                        listen = False





def image(keyword):

    image = pygame.image.load(keyword + ".png").convert_alpha()
    screen.blit(image, (175, 175))



int = True
ask = False
running = True

while running:
    for event in pygame.event.get():



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:

                ask = True


            if event.key == pygame.K_x:
                ask = False
                running = False

            if event.key == pygame.K_q:
                quiz()

        if event.type == pygame.QUIT:
            print(event)


            quit()





    if int == True :
        print("True")
        num = random.randint(6, 8)

        int = False
    display(1)
    pygame.display.update()




    if ask == True:




        keyword = start_listening()

        display(2)


        if alexa[keyword][0] ==  "img":

            image(keyword)

        pygame.display.update()

        engine.say(alexa[keyword][1])
        engine.runAndWait()
        int = True
        print(1)
        ask = False
