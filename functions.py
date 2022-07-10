import pyautogui as main
import pyperclip as pc
from points import empresa
import time

#wait time
main.PAUSE = 1.5
#coordenadas
POSITION_PORCENT =  634,101
PORCENT_VALUE = "45"

#Inicio
def inicio():
	main.hotkey("winleft", "d")
	main.hotkey("winright", "q")
	time.sleep(4)
	empresa()
	time.sleep(5)
	main.press('enter', presses=1)
	time.sleep(4)

#preparing size pdf
def precopy():
    puntero(POSITION_PORCENT)
    main.write(PORCENT_VALUE)
    main.press('enter', presses=1) 

#Clicks
def puntero(pos, click=1):
    main.moveTo(pos)
    main.click(clicks=click)

#data extractor for pyautogui
def function_copy(a):	
	pc.copy(a)
	main.hotkey('ctrl', 'v')  

   

