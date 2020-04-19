#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:05:01 2020

@author: Aditi
"""

import pyttsx3
from PIL import Image
engine = pyttsx3.init()

while True :
    alexa = {"olympics": "The olympics is an international sporting event which has been currently postponed to 2021 due to the coronavirus pandemic. One of the best participants so far has been Micheal Phelphs who competes in swimming and has won 23 gold medals.",
         
         
         "premier league": "The Premier League is a football tournament over England with the defending champions for the past 2 years being Manchester City",
         
         "running" : "Usain Bolt is the current world record holder for the 100 metres and the 200 metres sprint. His record for 100 meteres being 9.58 seconds and his record for the 200 metres being 19.19 seconds. He has earned a total of 9 gold medals in the olympics",
        
         "ipl" : "The Indian Premier League is a cricket tournament held all across India. The current defending champions are Mumbai Indians under the coachmanship of Mahela Jayawardene. This year's IPL has been postponed due to the coronavirus pandemic",
         
         "asian games" : "The Asian Games is a multisport event held for Asian countries every 4 years. The next Asian Games will be held in 2022 in Hangzhou, Zhejiang, China .",
         
         "long jump" : "The long jump is a track and field event in which athletes combine speed, strength and agility in an attempt to leap as far as possible from a take off point. The world record being set by Mike Powell which is 8.95 metres.",
         
         "wimbledon" : "The Wimbledon is one of the most prestigious tennis tournaments in the world. It has been held at the All England Club in Wimbledon, London, since 1877 and is played on outdoor grass courts. The defending champion for the men's singles being Novak Djokovic. This year's tournament has been cancelled due to the coronavirus outbreak.",
         
         "cycling" : "Cycling is a recreational activitiy which has tournaments mostly in Europe. The largest being UCI World Tour and Tour de France.",
         
         "formula 1" : "Formula One  is the highest class of single-seater auto racing held since 1950. The defending champion being Lewis Hamilton from Mercedes Benz.",
         
         "men's hockey world cup" : "The Hockey World Cup is an international field hockey competition organised by the International Hockey Federation (FIH). The current defending champions being Belgium although Pakistan has won the most amount of times."}


    keyword = input("Enter the keyword : ").lower()

    print(alexa[keyword])
    image = Image.open(keyword + '.png')
    image.show()
    engine.say(alexa[keyword])
    engine.runAndWait()


