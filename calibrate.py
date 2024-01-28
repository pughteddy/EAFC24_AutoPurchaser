import pyautogui
import time
import json
from purchase import click

def init():
    print("Starting calibration.")
    print(pyautogui.size())

    SearchButtonLocation = pyautogui.locateOnScreen('images/buy/Search.PNG')
    LocationX, LocationY = pyautogui.center(SearchButtonLocation)
    SearchButton = [LocationX, LocationY]
    click(SearchButton[0], SearchButton[1])
    time.sleep(2)

    buyNowButtonLocation = pyautogui.locateAllOnScreen('images/buy/BuyNow.PNG', confidence=0.80)
    buyNowButtonLocation = max(buyNowButtonLocation, key=lambda loc: loc[-1])
    LocationX, LocationY = pyautogui.center(buyNowButtonLocation)
    BuyNowButton = [LocationX, LocationY]
    click(BuyNowButton[0], BuyNowButton[1])
    time.sleep(2)

    OkButtonLocation = pyautogui.locateAllOnScreen('images/buy/Ok.PNG', confidence=0.80)
    OkButtonLocation = max(OkButtonLocation, key=lambda loc: loc[-1])
    LocationX, LocationY = pyautogui.center(OkButtonLocation)
    OkButton = [LocationX, LocationY]
    click(OkButton[0], OkButton[1])
    time.sleep(3)

    try:
        TLButtonLocation = pyautogui.locateAllOnScreen('images/buy/SendToTL.PNG', confidence=0.80)
        if not TLButtonLocation:
            raise pyautogui.ImageNotFoundException(f"Can't find Transfer List Button")
        TLButtonLocation = max(TLButtonLocation, key=lambda loc: loc[-1])
        LocationX, LocationY = pyautogui.center(TLButtonLocation)
        TLButton = [LocationX, LocationY]
        click(TLButton[0], TLButton[1])
        time.sleep(1)
    except pyautogui.ImageNotFoundException as e:
        print(f"Can't find Transfer List Button")

    BackButtonLocation = pyautogui.locateAllOnScreen('images/buy/Back.PNG', confidence=0.80)
    BackButtonLocation = max(BackButtonLocation, key=lambda loc: loc[-1])
    LocationX, LocationY = pyautogui.center(BackButtonLocation)
    BackButton = [LocationX, LocationY]
    click(BackButton[0], BackButton[1])
    time.sleep(1)

    IncreaseButtonLocation = pyautogui.locateAllOnScreen('images/buy/Increase.PNG', confidence=0.80)
    IncreaseButtonLocation = max(IncreaseButtonLocation, key=lambda loc: loc[-1])
    LocationX, LocationY = pyautogui.center(IncreaseButtonLocation)
    IncreaseButton = [LocationX, LocationY]
    click(IncreaseButton[0], IncreaseButton[1])

    DecreaseButtonLocation = pyautogui.locateAllOnScreen('images/buy/Decrease.PNG', confidence=0.95)
    DecreaseButtonLocation = max(DecreaseButtonLocation, key=lambda loc: loc[-1])
    LocationX, LocationY = pyautogui.center(DecreaseButtonLocation)
    DecreaseButton = [LocationX, LocationY]
    click(DecreaseButton[0], DecreaseButton[1])

    updateCoordinates = [SearchButton, BuyNowButton, OkButton, TLButton, BackButton, IncreaseButton, DecreaseButton]
    
    for coord in updateCoordinates:
        coord[0] = int(coord[0])
        coord[1] = int(coord[1])

    with open("search_the_transfer_market_coordinates.json", "w") as json_file:
        json.dump(updateCoordinates, json_file)

    print("Calibration is done.")



time.sleep(3)
init()