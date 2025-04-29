# samod subhasha
# 29/04/25

import datetime
import time
import pygame

def setAlarm(alarmTime):
    print(f"Alarm set for {alarmTime}")
    musicFile = "alarmclock\ma_meilleure_ennemie.mp3"
    
    isRunning = True
    
    while isRunning:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)
        
        
        if alarmTime == currentTime:
            print("Wake up")
            
            pygame.mixer.init()
            pygame.mixer.music.load(musicFile)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            isRunning = False
        time.sleep(1)
            

if __name__ == "__main__":
    alarmTime = input("Enter the alarm time HH:MM:SS - ")
    setAlarm(alarmTime)