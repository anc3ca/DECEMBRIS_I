#Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

skaitlis = int(input("Ievadiet skaitli: "))
sum = 0

for x in range (1, skaitlis+1):
    sum += x
print(f"Skaitot no viens līdz {skaitlis}, iegūst summu {sum}.")
