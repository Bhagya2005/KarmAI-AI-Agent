import pyautogui
import keyboard
import time
from PIL import Image
import base64
from io import BytesIO

class Mousepy:
    def __init__(self):
        pass
    
    def mouse_left_click(self):
        pyautogui.leftClick()
        return "Mouse Left Clicked"
    
    def mouse_right_click(self):
        pyautogui.rightClick()
        return "Mouse Right Clicked"

    def mouse_position(self):
        x, y = pyautogui.position()
        pixel_color = pyautogui.screenshot(imageFilename='temp.png').getpixel((x, y))
        return x,y,pixel_color
    

# For confidentiality reasons, some lines of code have been removed from this project. 
# If you are interested in running the complete version, please contact me at bhagya20052904@gmail.com, and 
# I will provide the full code. The project will function properly with the complete code. 


    def capture_screenshot_with_cursor(self,*args,**kwargs):
        screenshot = pyautogui.screenshot()
        x, y = pyautogui.position()
        cursor = Image.open('Tools\cursor.png').convert("RGBA")
        cursor = cursor.resize((50,71))
        r, g, b, a = cursor.split()
        red_cursor = Image.merge("RGBA", (r.point(lambda p: 255), g.point(lambda p: 0), b.point(lambda p: 0), a))
        screenshot.paste(red_cursor, (x+1, y+1), red_cursor)
        screenshot.save('temp.png')
        buffered = BytesIO()
        screenshot.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str

if __name__ == "__main__":
    mouse = Mousepy()
    print(mouse.move_mouse_to(177,63))