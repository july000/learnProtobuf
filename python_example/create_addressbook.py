import addressbook_pb2

def create_address_book():
    # 创建一个 AddressBook 实例
    address_book = addressbook_pb2.AddressBook()

    # 创建第一个 Person 实例
    person1 = address_book.people.add()
    person1.name = "John"
    person1.id = 123
    person1.email = "john@example.com"

    # 添加第一个 Person 的电话号码
    phone1 = person1.phones.add()
    phone1.number = "1234567890"
    phone1.type = addressbook_pb2.Person.PHONE_TYPE_MOBILE

    # 创建第二个 Person 实例
    person2 = address_book.people.add()
    person2.name = "Jane"
    person2.id = 456
    person2.email = "jane@example.com"

    # 添加第二个 Person 的电话号码
    phone2 = person2.phones.add()
    phone2.number = "9876543210"
    phone2.type = addressbook_pb2.Person.PHONE_TYPE_HOME

    return address_book

# 创建 AddressBook 实例
address_book = create_address_book()

# 将 AddressBook 序列化为字节串
serialized_data = address_book.SerializeToString()

# 将 AddressBook 写入文件
with open("./addressbook.pb", "wb") as f:
    f.write(serialized_data)
