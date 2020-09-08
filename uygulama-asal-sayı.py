x=int (input("bir sayı giriniz: "))
asallar=[]
control=0
for y in range(2,x+1):
    for z in range(2,y):
        if(y==2):
            asallar.append(y)
        elif(y%z==0):
            control+=1
    if(control==0):
        asallar.append(y)
    control=0    
print(asallar)