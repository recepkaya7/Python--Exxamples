message=" hello world.My name is Recep"
#message=message.upper()        # upper butun krarkterleri buyuk yazar
#message=message.lower()        #lower butun karakterleri kucuk yazar
#message=message.title()        #baş harfler buyuk
#message=message.capitalize()   #sadece ilk karakter buyuk digerleri kucuk
message=message.strip()         # ilk karakteri siler
#message=message.split()        #bosluk ile kelimeleri ayırır
#index=message.find('is')       #is varsa eger kaçıncı i ise o döner
#print(index)
message=message.replace('Recep','Recep Kaya') # yer degistirir

print(message) 