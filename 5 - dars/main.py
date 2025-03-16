# ======================================================
#          Ro'yxatlar | List: Funksiyalar va Metodlar
# ======================================================

# 1. Ro'yxatlarni tartiblash
# ---------------------------
# .sort() metodi: ro'yxatni joyida (in-place) tartiblaydi.
cars = ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print("sort() bilan tartiblangan (in-place):", cars)
# Diqqat: sort() metodi katta va kichik harflarga sezgir bo'lib,
# natijada, katta harflar kichik harflardan oldin keladi.

# Agar ro'yxatdagi matnlar aralash holatda bo'lsa (katta-kichik),
# key parametridan foydalanib, ularni bir xil ko'rinishga keltirib tartiblash mumkin.
cars_mixed = ['Bmw', 'mercedes benz', 'Volvo', 'gm', 'Tesla', 'audi']
cars_mixed.sort(key=str.lower)
print("key=str.lower bilan tartiblangan:", cars_mixed)

# sorted() funktsiyasi: asl ro'yxatni o'zgartirmasdan tartiblangan yangi ro'yxat qaytaradi.
cars_original = ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
sorted_cars = sorted(cars_original)
print("sorted() qaytargan ro'yxat:", sorted_cars)
print("Asl ro'yxat (o'zgarmagan):", cars_original)

# sorted() funktsiyasidan reverse=True parametri bilan teskari tartibda sort qilish:
sorted_cars_desc = sorted(cars_original, reverse=True)
print("Teskari tartibda sorted() bilan:", sorted_cars_desc)


# 2. Ro'yxatni teskari tartibda chiqarish
# -----------------------------------------
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# a) Slicing yordamida (oxiridan boshiga):
print("Slicing orqali teskari:", fruits[::-1])
# b) .reverse() metodi: ro'yxatni joyida teskari tartibga o'zgartiradi.
fruits.reverse()
print("reverse() metodi bilan teskari:", fruits)


# 3. range() funktsiyasi yordamida ro'yxat yaratish
# ---------------------------------------------------
# a) 0 dan 100 gacha bo'lgan juft sonlar:
even_numbers = list(range(0, 101, 2))
print("0 dan 100 gacha juft sonlar:", even_numbers)

# b) Juft va toq sonlar misoli:
juft_sonlar = list(range(0, 20, 2))   # 0, 2, 4, ... 18
toq_sonlar  = list(range(1, 20, 2))    # 1, 3, 5, ... 19
print("Juft sonlar:", juft_sonlar)
print("Toq sonlar:", toq_sonlar)


# 4. Sonli ro'yxatlar ustida oddiy amallar
# -------------------------------------------
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
eng_arzon = min(narhlar)
eng_qimmat = max(narhlar)
jami_narh = sum(narhlar)
print("Eng arzon narh:", eng_arzon)
print("Eng qimmat narh:", eng_qimmat)
print("Narhlar jami:", jami_narh)


# 5. TUPLES - O'ZGARMAS RO'YXAT
# -------------------------------
# Tuple yaratishda qavs () ishlatiladi va ularni o'zgartirish mumkin emas.
tomonlar = (20, 30, 55.2)
print("Tomonlar tuple:", tomonlar)
# Tuple slicing:
print("Tomonlar slicing (birinchi 2 element):", tomonlar[:2])


# 6. Ro'yxatning boshqa metodlari va funktsiyalari
# -------------------------------------------------

# a) append() - ro'yxat oxiriga element qo'shadi.
numbers = [1, 2, 3]
numbers.append(4)
print("append() bilan qo'shish:", numbers)

# b) insert() - belgilangan indeksga element qo'shadi.
numbers.insert(1, 1.5)  # 1-indeksga 1.5 ni qo'shamiz
print("insert() bilan qo'shish:", numbers)

# c) remove() - ro'yxatdan birinchi uchragan mos elementni o'chiradi.
numbers.remove(1.5)
print("remove() bilan o'chirish:", numbers)

# d) pop() - berilgan indeksdagi elementni sug'urib oladi va qaytaradi
# Agar indeks ko'rsatilmasa, oxirgi elementni o'chiradi.
popped_element = numbers.pop(2)
print("pop() bilan o'chirilgan element:", popped_element)
print("pop() dan keyingi ro'yxat:", numbers)

# e) clear() - ro'yxatdagi barcha elementlarni o'chirib, bo'sh ro'yxatga aylantiradi.
temp_list = [10, 20, 30]
temp_list.clear()
print("clear() bilan bo'shatilgan ro'yxat:", temp_list)

# f) copy() - ro'yxatning nusxasini yaratadi.
original_list = ['a', 'b', 'c']
copied_list = original_list.copy()
print("copy() bilan nusxa:", copied_list)

# g) index() - ro'yxatdagi elementning birinchi uchragan indeksini qaytaradi.
fruits = ['apple', 'banana', 'cherry', 'date']
index_banana = fruits.index('banana')
print("index() bilan 'banana' indeksi:", index_banana)

# h) count() - ro'yxatda berilgan element necha marta uchraganligini sanaydi.
sample_list = [1, 2, 3, 2, 2, 4, 5]
count_2 = sample_list.count(2)
print("count() bilan 2 elementining takrorlanishi:", count_2)

# i) extend() - ro'yxatni boshqa ro'yxat bilan kengaytiradi.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("extend() bilan kengaytirilgan ro'yxat:", list1)

# j) Ro'yxatlarni ko'paytirish - elementlarni takrorlash.
repeat_list = ['hello'] * 3
print("Ro'yxatni ko'paytirish:", repeat_list)

