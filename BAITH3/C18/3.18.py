print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("18)")
n = int(input("Nhập số nguyên dương n: "))
alist = []
a,b = 0,1
while a < n:
    alist.append(a)
    a,b = b,a + b
print(f"Dãy Fibonacci nhỏ hơn {n}: {alist}")
