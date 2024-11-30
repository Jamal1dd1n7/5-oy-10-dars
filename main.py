import main1
from database import db
from datetime import datetime
date_format = "%Y-%m-%d"

def run():
    while True:
        print("Buyruqlar:\n1 -> Models dan ma`lumot olish\n"
              "2 -> Emails dan ma`lumot olish\n"
              "3 -> Customers dan ma`lumot olish\n"
              "4 -> Employees dan ma`lumot olish\n"
              "5 -> Brands dan ma`lumot olish\n"
              "6 -> Brands dan ma`lumotlarni filtrlab olish\n"
              "7 -> Orders dan ma`lumot olish\n"
              "8 -> Models dagi mashinalarni umumiy narxini chiqarish\n"
              "9 -> Brands dagi barcha brandlarning sonini chiqarish\n"
              "10 -> Brand qo`shish\n"
              "11 -> Color qo`shish\n"
              "12 -> Order qo`shish\n"
              "13 -> Ishchi qo`shish")
        command = int(input("Buyruq tanlang (Buyruqning tartib raqamini kiritng): "))
        
        if command == 1:
            main1.show_models()
        elif command == 2:
            main1.show_emails()
        elif command == 3:
            main1.show_customers_count()
        elif command == 4:
            main1.show_employee_count()
        elif command == 5:
            main1.show_brands_count()
        elif command == 6:
            main1.show_brands_filtered()
        elif command == 7:
            main1.show_orders()
        elif command == 8:
            main1.show_models_price()
        elif command == 9:
            main1.show_total_brands()
        elif command == 10:
            brand_name = input("Qo'shish uchun brend nomini kiriting: ").title()
            if not brand_name.isalpha():
                print("Brend nomi faqat matndan iborat bo'lishi kerak!")
            else:
                db.input_brands(brand_name)
                print(f"{brand_name} brendi ma'lumotlar omboriga saqlandi!")
                main1.show_brands_count()
        elif command == 11:
            color_name = input("Qanday rang kiritmoqchisiz?: ").title()
            if not color_name.isalpha():
                print("Rang nomi faqat matndan iborat bo'lishi kerak!")
            else:
                db.input_colors(color_name)
                print(f"Yangi rang qo'shildi!: {color_name}")
        elif command == 12:
            print("\"Xaridorlar haqida ma'lumot\"")
            main1.show_customers()
            try:
                customer_id = int(input("Yuqoridagi id lardan foydalanib xaridor id sini kiriting: "))
            except ValueError:
                print("ID uchun raqamlardan foydalaning!")
                continue

            print("\"Xodimlar haqida ma'lumot\"")
            main1.show_employees()
            try:
                employee_id = int(input("Yuqoridagi id lardan foydalanib xodim id sini kiriting: "))
            except ValueError:
                print("ID uchun faqat raqamlardan foydalaning!")
                continue

            print("\"Modellar haqida ma'lumot\"")
            main1.show_next_models()
            try:
                model_id = int(input("Yuqoridagi id lardan foydalanib model id sini kiriting: "))
            except ValueError:
                print("ID uchun faqat raqamlardan foydalaning!")
                continue

            car_count = int(input(f"{model_id} ushbu id dagi avtomildan nechta kerak: "))
            order_date = input("Xarid sanasini kiriting (2024-11-27 formatda bo'lsin): ")
            try:
                datetime.strptime(order_date, date_format)
            except ValueError:
                print("Formatni xato kiritdingiz!")
                continue

            db.input_orders(customer_id, employee_id, model_id, car_count, order_date)
            print("Xarid muvaffaqiyatli amalga oshirildi!")
        elif command == 13:
            try:
                employee_id = int(input("Xodim uchun 4 xonalik id kiriting: "))
            except ValueError:
                print("ID uchun faqat sonlardan foydalaning!")
                continue
            first_name = input("Xodim uchun ism kiriting: ").title()
            last_name = input("Xodimning familiyasini kiriting: ").title()
            birth_date = input("Xodimning tug'ilgan sanasini kiriting (namuna: 1995-05-19): ")
            try:
                datetime.strptime(birth_date, date_format)
            except ValueError:
                print("Tug'ildan sanani ko'rsatilgan formatda kiriting!")
                continue
            phone_number = input("Xodimning telefon raqamini kiriting: ")
            if not phone_number.startswith("+998") and len(phone_number) == 13:
                print("Telefon raqam faqat +998 dan boshlanib 13 xonadan iborat bo'lishi kerak!")
                continue

            email = input("Xodimning e-pochta manzilini kiriting: ")
            if "@" and '.' not in email:
                print("Emailda @ hamda . belgilaridan biri mavjud emas!")
                continue

            country = input("Xodimning qaysi davlat fuqarosi?: ")
            city = input(f"Xodim {country} ning qaysi shahrida yashaydi?: ")
            db.input_employees(employee_id, first_name, last_name, birth_date, phone_number, email, country, city)
            print(f"Yangi xodim yaratildi!: {first_name} {last_name}")
        else:
            print("Nomalum buyruq kiritildi!")           

run()