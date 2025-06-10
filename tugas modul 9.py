import os
import time
from termcolor import cprint
os.system('cls')
icon = """
+-------+
|BLOKKU |
+-------+
"""
cprint(icon, 'yellow',"on_red", attrs=['bold'])
for char in "BLOKKU":
    cprint(char, 'cyan', end='')
    time.sleep(0.3)
print()
for i in range(10):
    dots = '.' * (i % 5)
    cprint(f"Memuat aplikasi BLOKKU{dots}", 'yellow', attrs=['bold'])
    time.sleep(0.5)
    os.system('cls')
    cprint(icon, 'yellow',"on_red",attrs=['bold'])
    for char in "BLOKKU":
        cprint(char, 'cyan', end='')
    print()
cprint("\nAplikasi BLOKKKU berhasil dibuka 💙", 'blue', attrs=['bold', 'underline'])
