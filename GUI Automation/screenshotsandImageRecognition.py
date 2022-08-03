'''
Screenshots and Image Recognition in pyAutoGUI
'''
import pyautogui, os

# print(os.getcwd())

pyautogui.screenshot('E:\\Python Udemy\\Automate boting stuff with Python programming course\\GUI Automation')

#Image recognition - the image has to be THE SAME!!!!
# pyautogui.locateOnScreen('E:\\Python Udemy\\Automate boting stuff with Python programming course\\GUI Automation\\Capture.JPG')

pyautogui.locateCenterOnScreen('E:\\Python Udemy\\Automate boting stuff with Python programming course\\GUI Automation\\Capture.JPG')