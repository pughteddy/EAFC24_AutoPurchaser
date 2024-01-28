import pyautogui
import time
import keyboard
import win32api, win32con
import json
import random

coordinates = []

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.randrange(100, 999, 1) / 100000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def load_coordinates():
    with open("search_the_transfer_market_coordinates.json", "r") as json_file:
        global coordinates
        coordinates = json.load(json_file)


def search():
    click(coordinates[0][0], coordinates[0][1])  # Search
    time.sleep(random.randrange(154, 227, 1) / 100)


def attempt_purchase():
    pyautogui.locateOnScreen('images/buy/BuyNow.PNG', confidence=0.80)
    print("Found results, attempting a purchase")
    click(coordinates[1][0], coordinates[1][1])  # Buy Now
    time.sleep(random.randrange(75, 111, 1) / 100)
    click(coordinates[2][0], coordinates[2][1])  # Ok
    time.sleep(random.randrange(300, 319, 1) / 100)
    click(coordinates[3][0], coordinates[3][1])  # Send to TL
    time.sleep(random.randrange(100, 127, 1) / 100)


def reset():
    click(coordinates[4][0], coordinates[4][1])  # Back
    time.sleep(random.randrange(80, 127, 1) / 100)
    click(coordinates[5][0], coordinates[5][1])  # Increase min Bid
    time.sleep(random.randrange(70, 280, 1) / 100)


if __name__ == "__main__":
    print("Loading coordinates...")
    load_coordinates()
    time.sleep(3)

    totalSearches = 0
    totalPurchases = 0
    MAX_TOTAL_SEARCHES = 40

    print("Beginning search...")
    while not keyboard.is_pressed('q') and totalSearches < MAX_TOTAL_SEARCHES:
        search()
        try:
            attempt_purchase()
            totalPurchases += 1
        except pyautogui.ImageNotFoundException as e:
            print("Did not find any results")
        reset()
        totalSearches += 1
        print("Total Searches: %s Total Purchases: %s" % (totalSearches, totalPurchases))


    if keyboard.is_pressed('q'):
        print("Ending script. Final results.. Total Searches: %s Total Purchase: %s" % (totalSearches, totalPurchases))
