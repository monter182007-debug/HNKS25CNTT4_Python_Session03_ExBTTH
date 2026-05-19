
choice =""
while choice !='n':
    # Nhap vao so luong nhan vien
    number_of_employees = int(input("Nhap vao so luong nhan vien: "))
    for i in range(number_of_employees):
        print(f"Nhan vien {i+1}")
        # Nhap vao thong tin nhan vien
        full_name=input("Nhap ten nhan vien: ")
        day_of_work = int(input("Nhap so ngay di lam: ")) 

        #  Hien thi thong tin
        print("--- Thong tin nhan vien ---")
        print(f'Ten: {full_name}')
        print(f'So ngay di lam: {day_of_work}')
        
        # Danh gia chuyen can
        status =''
        if day_of_work < 20:
            status = "Cần cải thiện chuyên cần"
            print(status)
        else:
            status= "Nhân viên chuyên cần tốt"
            print(status)
    choice = input("Tiep tuc chuong trinh? (y/n): ")
    if choice == 'n':
        print("END!")
        

