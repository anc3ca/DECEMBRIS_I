#Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.

skaitlis = int(input("Ievadi skaitli: "))


def faktorials(skaitlis):
    rezultats = 1

    for x in range(1, skaitlis+1):
        rezultats *= x

    return rezultats



if skaitlis <0:
    print("Ievadītais skaitlis nav naturāls skaitlis")
else:
    print(f"Ievadītā skaitļa {skaitlis} faktoriāls ir {faktorials(skaitlis)}")