# PYTHON 1 - dars: Asosiy tushunchalar

# Izoh qo'shish usullari:
# 1. '#' belgisi bilan - Yagona qatorli izoh
# 2. ''' ''' yoki """ """ - Ko'p qatorli izoh

# Matn chiqarish
print("Hello, world!")
print('Python dasturlash tili')
print("""Bu 1-qator
Salom, dunyo!""")

# Son chiqarish
print(12345)
print(3.14)

# "Escape" belgilar
print("O'zbekiston poytaxti \"Toshkent\"")  # Qo'shtirnoq ishlatish
print('O\'zbekiston poytaxti "Toshkent"')  # Bitta tirnoq bilan

# \n- Yangi qatordan yozish
print("Salom,\ndunyo!")

# \t - Tab (bo'sh joy qo'shish)
print("Salom\tsalom")

# Qo'shimcha maxsus belgilar
print("Salom\rDunyo")  # \r - Qator boshiga qaytaradi
print("Salom\b!")  # \b - Bir belgi o‘chiriladi

# Unicode belgilar
print("\u2764")  # Yurak belgisi
print("\U0001F600")  # Emoji (kulgu)

# Hexadecimal belgilar
print("\x41")  # 'A' harfi
print("\xa9")  # Copyright belgisi

# O'zgaruvchilar bilan ishlash
ism = "Anvar"  # Matn (string)
son = 123  # Butun son (integer)
print(ism)
print(type(ism))  # O'zgaruvchi turini aniqlash

# Stringdan son olish
qiymat = int("8")
print(type(qiymat))  # Natija: <class 'int'>

# Bir qatorga bir nechta o'zgaruvchi berish
x, y, z = 4, 9, "3"
javob = 27 // int(z)  # Stringni butun songa o'tkazish
print(javob)
print(type(javob))

x=y=z= "Olma"
print(x)
print(y)
print(z)


# Global va lokal o'zgaruvchilar
x = "shirin"  # Global o'zgaruvchi
def funksiya():
    x = "foydali"  # Lokal o'zgaruvchi
    print("Olma " + x)
funksiya()
print("Olma " + x)  # Global o'zgaruvchi saqlanib qoladi

# Global kalit so'zi bilan ishlash
def funksiya2():
    global x
    x = "shirin"
    print("Olma " + x)
funksiya2()
print("Olma " + x)

# Ma'lumot turlari
butun_son = 652
matn_korinishida = str(butun_son)  # Butun sonni matnga o'tkazish
print(type(matn_korinishida))

# Input orqali foydalanuvchidan ma'lumot olish
ism = input("Ismingizni kiriting: ")
print("Salom, " + ism + "!")

# Foydalanuvchidan son olish
son = float(input("Sonni kiriting: "))
xisobla = son + 3
print("Natija:", xisobla)

# f-string
mamlakat = "O'zbekiston"
print(f"{mamlakat} Markaziy Osiyoda joylashgan.")
print(f"Toshkent {mamlakat} davlatida joylashgan.")



# str = matn (string)
# int = butun sonlar (intager)
# float = kasr sonlar (float)

