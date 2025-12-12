print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("1)")
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2 * 3.14

aCricle = Circle(5)
print(aCricle.area())
aCricle = Circle(6)
print(aCricle.area())
aCricle = Circle(9)
print(aCricle.area())
