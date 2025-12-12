print("Đoàn Văn Tân")
print("MSV: 045751030110009")
print("################################")
print("26)")
def calculate():
    balance = 0
    print("Nhập nhật ký giao dịch (Ví dụ: D 100 hoặc W 50).")
    print("Nhấn Enter liên tiếp 2 lần (dòng trống) để kết thúc nhập liệu.")
    while True:
        transaction = input()
        if not transaction:
            break 
        parts = transaction.split()
        if len(parts) != 2:
            print(f"Cảnh báo: Định dạng không hợp lệ cho dòng '{transaction}'. Vui lòng nhập đúng 'D [số tiền]' hoặc 'W [số tiền]'.")
            continue 
        trans_type = parts[0].upper()         
        try:
            amount = int(parts[1])
        except ValueError:
            print(f"Cảnh báo: Số tiền không hợp lệ cho dòng '{transaction}'. Vui lòng nhập số nguyên.")
            continue
        if trans_type == 'D':
            balance += amount
        elif trans_type == 'W':
            balance -= amount
        else:
            print(f"Cảnh báo: Loại giao dịch không xác định '{trans_type}'. Chỉ chấp nhận 'D' hoặc 'W'.")
            continue
    print(f"Đầu ra (Số tiền thực trong tài khoản): {balance}")
if __name__ == "__main__":
    calculate()
