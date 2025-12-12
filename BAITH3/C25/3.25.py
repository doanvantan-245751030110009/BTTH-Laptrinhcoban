print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("25)")
def filter():
    input_str = input("Nhập các số (phân tách bằng dấu phẩy, ví dụ: 1,2,3,4,5,6,7,8,9): ")
    numbers_list = []
    for item in input_str.split(','):
        try:
            numbers_list.append(int(item.strip()))
        except ValueError:
            continue
    odd_numbers = [num for num in numbers_list if num % 2 != 0]
    output_str = ",".join(map(str, odd_numbers))
    print(f"Đầu ra (các số lẻ đã lọc): {output_str}")
if __name__ == "__main__":
    filter()


