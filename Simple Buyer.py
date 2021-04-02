import pyautogui
import pygame
import time
pygame.mixer.init()

time.sleep(5)
while True:
    ATC = pyautogui.locateCenterOnScreen('AddToCart.png')
    
    if (ATC == None):
        print(ATC)
    if (ATC != None):
        pyautogui.click(ATC.x, ATC.y)
        print("Added To Cart")
        pygame.mixer.music.load("Finished.wav")
        pygame.mixer.music.play(loops=0)
        break
        
    