
from smartphone import Smartphone

# Объявляем переменную catalog и заполняем список экземплярами класса Smartphone
catalog = [
    Smartphone("Apple", "iPhone 12", "+79123456789"),
    Smartphone("Samsung", "Galaxy S12", "+79123456788"),
    Smartphone("Xiaomi", "Mi 11", "+79123456787"),
    Smartphone("OnePlus", "8T", "+79123456786"),
    Smartphone("Google", "Pixel 4", "+79123456785")
]

# Печатаем весь каталог 
print("Каталог смартфонов:")
for phone in catalog:
    print(phone.brand , phone.model , phone.phone_number)
