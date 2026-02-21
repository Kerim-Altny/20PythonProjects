import pyautogui
import time
from PIL import ImageGrab

HITBOX = (195, 765, 245, 830)

def is_obstacle_in_front():
    image = ImageGrab.grab(bbox=HITBOX)

    for x in range(image.width):
        for y in range(image.height):
            color = image.getpixel((x, y))
            if color[0] < 100:
                return True

    return False


def start_bot():
    print("🤖 Dino Bot activates in 3 seconds! Keep the game on screen...")
    time.sleep(3)


    pyautogui.press('space')
    print("🚀 Bot started! (Press Ctrl+C to stop)")

    try:
        while True:
            if is_obstacle_in_front():
                pyautogui.press('space')

                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n🛑 Bot Stopped.")


if __name__ == "__main__":
    start_bot()