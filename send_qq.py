import pyautogui
import time


def get_qq_pos():
    image_path = '.\\qq_img\\s.png'
    try:
        position = pyautogui.locateOnScreen(image_path)
        if position:
            x, y, width, height = position
            return x + width / 2, y + height / 2
        else:
            return -1
    except pyautogui.ImageNotFoundException:
        return -1


def get_qq_pos_2():
    image_path = '.\\qq_img\\f.png'
    try:
        position = pyautogui.locateOnScreen(image_path)
        if position:
            x, y, width, height = position
            return x + width / 2, y + height / 2
        else:
            return -1
    except pyautogui.ImageNotFoundException:
        return -1


def qq_choise_group(group):
    x, y = get_qq_pos()
    pyautogui.click(x, y)
    pyautogui.typewrite(group, interval=0.001)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')




def qq_send_message(message):
    x, y = get_qq_pos_2()
    x, y = x + 40, y + 40
    pyautogui.click(x, y)
    time.sleep(0.1)
    pyautogui.click(x, y)

    import pyperclip

    # 修改剪切板的文本内容
    pyperclip.copy("[以下信息由机器人发送]\n"+message)

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('enter')

