import pyautogui
import time


for i in range(100):
    time.sleep(7)
    # Peso/PC - double click
    pyautogui.click(724, 410, clicks=2,duration=1)
    # copiar
    pyautogui.hotkey("ctrlleft", "c")
    # Atributo - single click
    pyautogui.click(861, 170, clicks=2,duration=1)
    # Scroll - quatro clicks
    pyautogui.click(1153, 707, clicks=4)
    # Peso Frete gr - double click
    pyautogui.click(1075, 697, clicks=2,duration=1)
    # colar
    pyautogui.hotkey("ctrlleft", "v")
    pyautogui.typewrite("*1000")
    pyautogui.hotkey("enter")
    # Identificação Auxiliar - single click
    pyautogui.click(670, 167, clicks=1)
    # Referência - double click
    pyautogui.click(857, 236, clicks=2,duration=1)
    # copiar
    pyautogui.hotkey("ctrlleft", "c")
    # Atributo - single click
    pyautogui.click(861, 170, clicks=1)
    # Modelo - double click
    pyautogui.click(707, 459, clicks=2,duration=1)
    # colar
    pyautogui.hotkey("ctrlleft", "v")
    pyautogui.hotkey("alt", "v")
    pyautogui.hotkey("enter")
    # sair
    pyautogui.press('esc')
    pyautogui.press('s')
    # seta para baixo
    pyautogui.press('down')
    # F2
    pyautogui.press('f2')  

print("terminei")
print("terminei")