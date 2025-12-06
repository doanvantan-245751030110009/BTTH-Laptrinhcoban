print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("6)")
j=[]
for i in range(2000,3201):
   if (i%7==0) and (i%5!=0):
      j.append(str(i))
print(",".join(j))
