website="http://www.google.com"
course="pyhton kursu:baştan sona pyhton programlama rehberiniz."
print("course str kaç karakter bulunuyor")
print(len(course))
print("website içindeki www olan kismi aliniz")
remove=website[7:10]
print(remove)
print("website icinden com aliniz")
remo=website[-3:]
print(remo)
print("course stringini tersten yaz.")
ters=course[::-1]
print(ters)
name,surname,age,job='bora',"yilmaz",32,"enginee"
print(f"benim adim {name} {surname}.yasim {age} ve meslegim {job}.")
print("hello world ifadesindeki w yi W ile degistir.")
s="hello world"
s=s[0:6]+'W'+s[-4:]
print(s)
print("abc ifadesini yan yana 3 defa yazdırın")
x='abc '*3
print(x)