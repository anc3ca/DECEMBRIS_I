#Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.

x = int(input("Ievadiet skaitli: "))
if x%2 == 0:
    print(f"Skaitlis {x} ir pāra skaitlis.")
else:
    print(f"Skaitlis {x} ir nepāra skaitlis.")