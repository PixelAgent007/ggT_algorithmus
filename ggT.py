from time import sleep

print("""
            _____             
  __ _  __ |_   _|_ __  _   _ 
 / _` |/ _` || | | '_ \| | | |
| (_| | (_| || |_| |_) | |_| |
 \__, |\__, ||_(_) .__/ \__, |
 |___/ |___/     |_|    |___/ 

""")
print("""
Copyright (C) 2021  Oskar Manhart
This program comes with ABSOLUTELY NO WARRANTY; for details type `cat LICENSE`.
This is free software, and you are welcome to redistribute it
under certain conditions; type `cat LICENSE` for details.
""")
print("Berechne den größten gemeinsamen Teiler zweier Zahlen.")
sleep(5)

a = int(input("A: "))
b = int(input("B: "))
temp1 = a
temp2 = b

while not temp1 == 0 or not temp2 == 0:
    if temp1 > temp2:
        temp1 = temp1 - temp2
    elif temp2 > temp1:
        temp2 = temp2 - temp1
    elif temp1 == temp2:
        print(f"ggT von {a} und {b}: {temp1}")
        break

