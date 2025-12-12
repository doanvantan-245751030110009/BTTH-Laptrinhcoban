print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("2)")
class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def area(self):
        return self.dai * self.rong
    
hinh_chu_nhat = Hinhchunhat(8,10)
print(hinh_chu_nhat.area())
hinh_chu_nhat = Hinhchunhat(8,90)
print(hinh_chu_nhat.area())
