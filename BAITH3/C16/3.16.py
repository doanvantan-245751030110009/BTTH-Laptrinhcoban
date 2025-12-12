print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("16)")
chuoi= input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy, ví dụ: 0100,1010): ")
daynp = chuoi.split(',')
print("Các giá trị nhị phân đã nhập:")
for so in daynp:
    print(so.strip())
