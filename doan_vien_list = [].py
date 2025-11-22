doan_vien_list = []

def them_doan_vien():
    print("\n=== THÊM ĐOÀN VIÊN ===")
    mssv = input("Nhập MSSV: ")
    hoten = input("Nhập họ tên: ")
    lop = input("Nhập lớp: ")
    sdt = input("Nhập số điện thoại: ")

    doan_vien = {
        "mssv": mssv,
        "hoten": hoten,
        "lop": lop,
        "sdt": sdt
    }

    doan_vien_list.append(doan_vien)
    print(">> Thêm thành công!\n")


def xem_danh_sach():
    print("\n=== DANH SÁCH ĐOÀN VIÊN ===")
    if len(doan_vien_list) == 0:
        print("Chưa có đoàn viên nào.\n")
        return

    for dv in doan_vien_list:
        print(f"MSSV: {dv['mssv']} | Họ tên: {dv['hoten']} | Lớp: {dv['lop']} | SĐT: {dv['sdt']}")
    print("")


def tim_kiem():
    print("\n=== TÌM KIẾM ĐOÀN VIÊN ===")
    tukhoa = input("Nhập MSSV hoặc họ tên: ").lower()

    found = False
    for dv in doan_vien_list:
        if tukhoa in dv["mssv"].lower() or tukhoa in dv["hoten"].lower():
            print(f"→ Tìm thấy: {dv['mssv']} - {dv['hoten']} - {dv['lop']} - {dv['sdt']}")
            found = True

    if not found:
        print("Không tìm thấy đoàn viên nào.\n")


def menu():
    while True:
        print("===== QUẢN LÝ ĐOÀN VIÊN =====")
        print("1. Thêm đoàn viên")
        print("2. Xem danh sách")
        print("3. Tìm kiếm")
        print("0. Thoát")

        chon = input("Nhập lựa chọn: ")

        if chon == "1":
            them_doan_vien()
        elif chon == "2":
            xem_danh_sach()
        elif chon == "3":
            tim_kiem()
        elif chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!\n")

menu()
