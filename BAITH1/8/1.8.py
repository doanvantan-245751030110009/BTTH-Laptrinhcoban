print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("8)")
a,b=1,2
t=0
print(a,end=" ")
while(a<=4000000-1):
   print(a,end=" ")
   if a%2==0:
        t+=a
   a,b=b,a+b
print("\n tổng dăy số chẵn trong dăy Fibonacci:",t)
