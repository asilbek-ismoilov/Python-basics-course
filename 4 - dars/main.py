# ============================================
#         Ro'yxatlar (Listlar) darsi
# ============================================
# Ro'yxatlar Python’da o'zgaruvchan (mutable) va tartiblangan
# ma'lumotlar tuzilmasidir. Ular turli xil turdagi
# ma'lumotlarni o'z ichiga olishi mumkin: matnlar, sonlar,
# mantiqiy qiymatlar va hatto boshqa ro'yxatlar.


#    [ ]

# a, b, c, = 4, 5, 6

# 1. Ro'yxat yaratish
# Misol uchun:
mevalar = ["Olma", "Anjir", "Shaftoli", "O'rik", "Banan"]  # Matnli ro'yxat
narxlar = [12000, 32000, 46500, 8000, 22000]                  # Sonli ro'yxat
sonlar  = ["bir", "ikki", 3, 4.0, 5]                           # Aralash ro'yxat
bosh = []                                                   # Bo'sh ro'yxat


# mevalar = ["Olma", "Anjir", "Shaftoli", "O'rik", "Banan"] 
#              0        1          2         3        4


# 2. Ro'yxat turlarini va ularning uzunligini ko'rish:
print("mevalar =", mevalar)
print("narxlar =", narxlar)
print("sonlar  =", sonlar)
print("Bo'sh ro'yxat =", bosh)
print("mevalar uzunligi:", len(mevalar))  # len() - ro'yxatdagi elementlar sonini qaytaradi

# 3. Indeks orqali ro'yxat elementlariga kirish:
# Indeks 0 dan boshlanadi. Shuningdek, manfiy indekslash ham mumkin.
print("Birinchi meva:", mevalar[0])
print("Uchinchi meva:", mevalar[2])

# mevalar = ["Olma", "Anjir", "Shaftoli", "O'rik", "Banan"] 
# #            -5        -4        -3        -2      -1

print("Oxirgi meva (manfiy indeks bilan):", mevalar[-1])
print("Birinchi meva (manfiy indeks bilan):", mevalar[-5])

# 4. Ro'yxatlar bilan arifmetik amallar
# Ro'yxatda turli turdagi qiymatlar bo'lishi mumkin,
# ammo arifmetik amallar uchun raqamlar mos bo'lishi kerak.
narxlar2 = [12000, 32000, int("25000"), 46500, 8000, 22000.0]
yigindi = narxlar2[4] + narxlar2[2]  # 8000 + 25000
print("Narxlar ro'yxatidagi 5-chi va 3-chi elementlarning yig'indisi:", yigindi)

# 5. Ro'yxatga element qo'shish
# 5.1 append() metodi: ro'yxat oxiriga qo'shadi.
cars = ["BMW"]
cars.append("Audi")
print("append bilan qo'shilgan:", cars)

# 5.2 insert() metodi: belgilangan indeks bo'yicha element qo'shadi.
cars = ["BMW", "Mersedes"]
cars.insert(2, "Bugatti")
print("insert bilan qo'shilgan:", cars)

# 6. Ro'yxat elementini o'zgartirish
cars = ["BMW", "Mersedes"]
cars[0] = "Audi"  # 0-indeksdagi elementni o'zgartirish
print("Element almashtirildi:", cars)

# 7. Ro'yxatdan element o'chirish
# 7.1 del operatori: indeks bo'yicha elementni o'chiradi.
phones = ["Iphone", "Redmi", "Samsung", "Honor", "Infinix"]
del phones[4]
print("del bilan o'chirilgan:", phones)

# 7.2 remove() metodi: birinchi uchragan mos qiymatni o'chiradi.
phones = ["Iphone", "Redmi", "Samsung", "Honor", "Infinix"]
phones.remove("Honor")  # "Honor" qiymati o'chiriladi
print("remove bilan o'chirilgan:", phones)

# 7.3 clear() metodi: ro'yxatdagi barcha elementlarni o'chiradi.
phones = ["Iphone", "Redmi", "Samsung", "Honor", "Infinix"]
phones.clear()
print("clear bilan bo'shatilgan:", phones)

# 8. Elementni sug'urib olish (pop)
# pop() metodi belgilangan indeksdagi elementni sug'urib olib qaytaradi.
phones = ["Iphone", "Redmi", "Samsung", "Honor", "Infinix"]
top_tel = phones.pop(2)  # 2-indeksdagi "Samsung" ni sug'urib olamiz
print("Sug'urib olingan telefon:", top_tel)
print("pop dan keyingi ro'yxat:", phones)

# 9. Ro'yxatni nusxalash (copy)
phones = ["Iphone", "Redmi", "Samsung", "Honor", "Infinix"]
yangi_phones = phones.copy()
print("Nusxa olingan ro'yxat:", yangi_phones)

# 10. Qo'shimcha ro'yxat funksiyalari va amallari
# 10.1 index() metodi - berilgan elementning indeksini qaytaradi.
print("Banan indeksi:", mevalar.index("Banan"))

# 10.2 count() metodi - ro'yxatda berilgan elementdan nechta mavjudligini aniqlaydi.
print("Olma soni:", mevalar.count("Olma"))

# 10.3 Slicing (kesish) - ro'yxatning ma'lum bir qismini olish.
print("Birinchi ikki meva:", mevalar[0:2])
print("Oxirgi ikki meva:", mevalar[-2:])

# 10.4 Ro'yxatlarni qo'shish (concatenation)
yangi_mevalar = mevalar + ["Anor", "Uzum"]
print("Qo'shilgan ro'yxat:", yangi_mevalar)

# 10.5 Ro'yxatlarni ko'paytirish - elementlarni takrorlash.
takror_mevalar = ["Olma"] * 3
print("Ko'paytirish:", takror_mevalar)

# Eslatma:
# Ro'yxatlar ustida o'zgartirishlar amalga oshirilganda, 
# asl ro'yxatga ta'siri bo'lishi mumkin (mutable tuzilma).
# Shuning uchun nusxa olish (copy) amali ko'pincha muhim hisoblanadi.
