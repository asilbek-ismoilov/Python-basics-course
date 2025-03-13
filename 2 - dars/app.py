# PYTHON 2 - dars

# Foydalanuvchi ma'lumotlarini saqlash va formatlash
ism, kurs, meva, yosh = "Alfred", "Python", "Olma", 15
# F-string yordamida matnni oson formatlash
matn = f"Salom {ism}, Siz {kurs} kursida o'qiysizmi? Yosh: {yosh}"
print(matn)

foydalanuvchi_ism = input("Ismingizni kiriting: ")
print(f"Xush kelibsiz, {foydalanuvchi_ism}!")

# Arifmetik operatorlar
x, y, z = 7, 6, 23
hisobla = (x + z) / z  # Qo'shish va bo'lish
print(f"Hisob natijasi: {hisobla}")

ayirma = x - y  # Ayirish
print(f"Ayirma: {ayirma}")

kopaytma = x * y  # Ko'paytirish
print(f"Ko'paytirish: {kopaytma}")

bolish = z / y         # Bo'lish (natija float bo'ladi)
print(f"Bo'lish: {bolish}")

butun_bolinma = z // y  # Butun bo'linma
print(f"Butun bo'linma: {butun_bolinma}")

qoldiq = z % y  # Qoldiq olish
print(f"Qoldiq: {qoldiq}")

ildiz = x ** 2  # Darajaga ko'tarish
print(f"Ildiz: {ildiz}")

# O'zlashtirish operatorlari
son = 10
son += 5  # son = son + 5
print(f"Yangi son: {son}")

son -= 3  # son = son - 3
print(f"Kamaytirildi: {son}")

son *= 2  # son = son * 2
print(f"Ko'paytirildi: {son}")

son /= 4  # son = son / 4
print(f"Bo'lindi: {son}")

# Ma'lumot turlari
son_1 = 56.0
son_2 = 48
print(f"son_2 turi: {type(son_2)}")
print(f"son_1 turi: {type(son_1)}")

hisobla = 55 + 32.0
print(f"Yangi hisob: {hisobla}, turi: {type(hisobla)}")

javob = 98 // 3
print(f"Butun bo'linma natijasi: {javob}")

# Satrlarga ishlov berish
matn = "Bugun issiq havo bo'ladi.\nTaxmin"
print(matn)

matn = "Kurslar har kuni" + " ertalab soat 8:00"
print(matn)

# String metodlari
# upper() - Barcha harflarni katta qiladi
# lower() - Barcha harflarni kichik qiladi
# title() - Har bir so'z bosh harfini katta qiladi
# capitalize() - Faqat birinchi harfni katta qiladi

matn = "python darslari"
print(f"upper(): {matn.upper()}")       # Hammasi katta harf
print(f"lower(): {matn.lower()}")       # Hammasi kichik harf
print(f"title(): {matn.title()}")       # Har bir so'z bosh harfi katta
print(f"capitalize(): {matn.capitalize()}")  # Faqat birinchi harf katta

kitob = input("Kitob nomini kiriting: ").capitalize()
print(kitob)

yosh, ism, familiyasi, yil = 15, "Ezoza", "Mamarasulova", 2009
print(ism.upper())

# Katta sonlarni o'qish uchun _ bilan ajratish
sonlar = 900_800_600_000
print(f"Katta son: {sonlar}")

# Sonlarni f-string bilan formatlash
pul = 25000
print(f"Pul miqdori: {pul:,} so'm")  # , bilan ajratish

# Bo'sh joylarni tozalash metodlari
# strip() - Bosh va oxiridagi bo'sh joylarni olib tashlaydi
# rstrip() - O'ng tomondagi bo'sh joylarni olib tashlaydi
# lstrip() - Chap tomondagi bo'sh joylarni olib tashlaydi

text = "             Lorem ipsum dolor sit amet consectetur      ".strip()
print(text)

kurs = "    python         "
print(f"Biz sifatli kursda {kurs.strip().title()} o'rganamiz")
