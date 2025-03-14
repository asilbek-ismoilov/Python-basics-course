# PYTHON 3 - dars

# 1. Taqqoslash operatorlari
# ==, !=, >, <, >=, <=
a, b = 10, 5
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

# 2. Mantiq operatorlari
# and, or, not
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# 3. Aniqlash operatorlari
# is, is not
c = [1, 2, 3]
d = c
e = [1, 2, 3]
print(c is d)      # True
print(c is e)      # False
print(c is not e)  # True

# 4. Python ma'lumot turlari

# Matn turi: str
txt = "Hello, Python!"
print(type(txt))

# Raqam turi: int, float, complex
son1 = 42
son2 = 3.14
son3 = 2 + 3j
print(type(son1), type(son2), type(son3))

# Ketma-ketlik turi: list, tuple, range
lst = [1, 2, 3]
tpl = (4, 5, 6)
rng = range(7)
print(type(lst), type(tpl), type(rng))

# Ko‘rsatish turi: dict
dct = {"ism": "Ali", "yosh": 25}
print(type(dct))

# O‘rnatish turi: set, frozenset
st = {1, 2, 3}
frz_st = frozenset([4, 5, 6])
print(type(st), type(frz_st))

# Mantiq turi: bool
mantiqiy = True
print(type(mantiqiy))

# Binar (ikkilik) turi: bytes, bytearray, memoryview
bt = bytes(5)
ba = bytearray(5)
mv = memoryview(bt)
print(type(bt), type(ba), type(mv))
