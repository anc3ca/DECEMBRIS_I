#Izveidojiet Python programmu, kas izmanto while ciklu, lai atrastu pirmo skaitli, kura kvadrāts ir lielāks par 1000.

x = 1
while x**2 <= 1000:
    x += 1

print(f"Pirmais skaitlis, kura kvadrāts ir lielāks par 1000, ir {x}")