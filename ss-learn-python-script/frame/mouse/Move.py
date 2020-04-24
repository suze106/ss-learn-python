import pyautogui;

def click(ac):
    pyautogui.click(ac,ac)

if __name__ == '__main__':
    i = 1
    while i<=3:
        i+=1
        click(i*100)