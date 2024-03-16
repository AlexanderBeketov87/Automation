
from address import Address
from mailing import Mailing

# Создаем экземпляр класса Mailing
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "20", "10")
mailing = Mailing(to_address, from_address, 200, "ABCD1234")

# Выводим информацию о почтовом отправлении
print(f"Отправление {mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} "
      f"в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mailing.cost} рублей.")
