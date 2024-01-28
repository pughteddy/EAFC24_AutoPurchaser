import pyautogui
import time
import json
from purchase import click


def init():
    print("Starting calibration.")

    search_button_location = pyautogui.locateOnScreen('images/Search.PNG')
    location_x, location_y = pyautogui.center(search_button_location)
    search_button = [location_x, location_y]
    click(search_button[0], search_button[1])
    time.sleep(3)

    buy_now_button_location = pyautogui.locateAllOnScreen('images/BuyNow.PNG', confidence=0.80)
    buy_now_button_location = max(buy_now_button_location, key=lambda loc: loc[-1])
    location_x, location_y = pyautogui.center(buy_now_button_location)
    buy_now_button = [location_x, location_y]
    click(buy_now_button[0], buy_now_button[1])
    time.sleep(3)

    ok_button_location = pyautogui.locateAllOnScreen('images/Ok.PNG', confidence=0.80)
    ok_button_location = max(ok_button_location, key=lambda loc: loc[-1])
    location_x, location_y = pyautogui.center(ok_button_location)
    ok_button = [location_x, location_y]
    click(ok_button[0], ok_button[1])
    time.sleep(3)

    tL_button_location = pyautogui.locateAllOnScreen('images/SendToTL.PNG', confidence=0.80)
    tL_button_location = max(tL_button_location, key=lambda loc: loc[-1])
    location_x, location_y = pyautogui.center(tL_button_location)
    tl_button = [location_x, location_y]
    click(tl_button[0], tl_button[1])
    time.sleep(2)

    back_button_location = pyautogui.locateAllOnScreen('images/Back.PNG', confidence=0.80)
    back_button_location = max(back_button_location, key=lambda loc: loc[-1])
    location_x, location_y = pyautogui.center(back_button_location)
    back_button = [location_x, location_y]
    click(back_button[0], back_button[1])
    time.sleep(2)

    increase_button_location = pyautogui.locateAllOnScreen('images/Increase.PNG', confidence=0.80)
    increase_button_location = max(increase_button_location, key=lambda loc: loc[-1])
    location_x, location_y = pyautogui.center(increase_button_location)
    increase_button = [location_x, location_y]
    click(increase_button[0], increase_button[1])
    time.sleep(1)

    decrease_button_location = pyautogui.locateAllOnScreen('images/Decrease.PNG', confidence=0.95)
    decrease_button_location = max(decrease_button_location, key=lambda loc: loc[-1])
    location_x, location_y = pyautogui.center(decrease_button_location)
    decrease_button = [location_x, location_y]
    click(decrease_button[0], decrease_button[1])

    updateCoordinates = [search_button, buy_now_button, ok_button, tl_button, back_button, increase_button, decrease_button]
    
    for coord in updateCoordinates:
        coord[0] = int(coord[0])
        coord[1] = int(coord[1])

    with open("search_the_transfer_market_coordinates.json", "w") as json_file:
        json.dump(updateCoordinates, json_file)

    print("Calibration is done.")


time.sleep(3)
init()
