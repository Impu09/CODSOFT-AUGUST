import random

uppr_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = uppr_letters.lower()
spec_chars = """~!@#$%^&*()_+"'-=}{[]:;?><,./"""
digits = "0123456789"

allChar = ""

upper, lower, nums, symbols = True, True, True, True

if upper: allChar += uppr_letters
if lower: allChar += lower_letters
if nums: allChar += digits
if symbols: allChar += spec_chars

Length = int(input("Enter The Legth Of Password: "))

pswd = "".join(random.sample(allChar, Length))
print(pswd)