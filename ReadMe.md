# EAFC AutoPurchaser
This package contains python scripts for automatically purchasing players on EAFC24 using PyAutoGUI. 

## PyAutoGUI disclaimer
PyAutoGUI will perform actual actions on your computer screen. 
If the screen regions end up being incorrect, the program is capable of clicking on unintended contents. 

## How to use this package
1. The calibrate script contains logic to automatically configure the click locations to be used. This should
execute on the "Search the Transfer Market" page on the webapp. Simply run this script while on the correct web UI 
one time to prepare the purchasing script.
2. Set the max buy now price in the purchase.py script via MAX_TOTAL_SEARCHES. EAFC increments the min price
at a few different intervals depending on the value. 
3. Begin the purchase.py script

## Credits
An original script using PyAutoGui was created by @zachangha. This served as the inspiration for this package
and he created the calibrate.py class.