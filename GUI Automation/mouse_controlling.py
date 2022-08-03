import pyautogui

print(pyautogui.size())     #resolution

width , height = pyautogui.size()

pyautogui.position()        #giving the position of the cursor

# pyautogui.moveTo(10,10) #changing the position of the mouse

# pyautogui.moveTo(10,10, duration = 3.5)

# pyautogui.moveRel(200,0)    #moving 200 px to the right

pyautogui.click(393,21)