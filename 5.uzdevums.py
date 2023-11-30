#Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)

from datetime import datetime
currentTime = datetime.datetime.now()
currentTime.hour


if currentTime.hour < 12:
    print("Labrīt!")

elif 12 <= currentTime.hour < 18:
  print("Labdien!")

else:
  print("Labvakar!") 