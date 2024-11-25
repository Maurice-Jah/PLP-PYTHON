# Create a class
# add attributes and methods
# Use constructors
# Add inheritance to explore polymorphism or encapsulation


class Phone:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price


    def get_brand(self):
        return self.__brand
        
    def get_model(self):
        return self.__model
        
    def get_price(self):
         return self.__self
    def make_call(self, number):
        print(f"Calling {number}....")

    def send_message(self,message,number):
        print(f"Sending message to {number}: {message}")

        

class SmartPhone(Phone):
    def __init__(self,brand,model,price,operating_system,storage):
        self.operating_system = operating_system
        self.storage = storage
        super().__init__(brand,model,price)
    
    def get_operating_system(self):
        return self.operating_system
    
    def get_storage(self):
        return self.storage
    
    def browse_interent(self, url):
        print(f"Browsing {url}...")

    def take_photo(self):
        print("Taking photo...")


class AndroidPhone(SmartPhone):
    def __init__(self, brand, model, price, operating_system, storage,andriod_version):
        super().__init__(brand, model, price, operating_system, storage)
        self.__android_version = andriod_version

    def get_android_version(self):
        return self.__android_version 

    def use_google_assistance(self):
        print("Using Google Assistant...")

class Iphone(SmartPhone):
    def __init__(self, brand, model, price, operating_system, storage, ios_version):
        super().__init__(brand, model, price, operating_system, storage)
        self.__ios_version = ios_version

    def get_ios_version(self):
        return self.__ios_version
    
    def use_siri(self):
        print(f"I am using Siri...")


# Using Polymorphic function
def use_phone(phone):
    print(f"Using {phone.get_brand()}")
    phone.get_model() 
    phone.make_call("3923566668")
    phone.send_message("3923566668", "Hello")

    if isinstance(phone, SmartPhone):
        phone.browse_interent("https://plpacademy.org")
        phone.take_photo()
    
    if isinstance(phone, AndroidPhone):
        phone.use_google_assistance()
        phone.get_android_version()
    
    if isinstance(phone, Iphone):
        phone.use_siri()




android = AndroidPhone("Samsung","Galaxy S22", 999, "Android", "128GB", 11)
iphone = Iphone("Apple", "iPhone 13", 999, "ios", "256GB", "15")


phones = [android,iphone]

for phone in phones:
    use_phone(phone)
    print()



# ====================================== #
# Activity 2 Polymorphism Challenge
# A program that includes animals or vehicles with same action like move(). Each class define move() differntly.

class TransportMeans:
    def __init__(self,name):
        self.name = name
        
    def move(self):
        pass

class Plane(TransportMeans):
    def move(self):
        return (f"Flying {self.name} Plane ✈")

class Car(TransportMeans):
    def move(self):
        return "Driving 🚘"

# Instantiating the classes
plane = Plane("Arik")
car = Car("Danfo")


transport_array = [plane.move(),car.move()]

for transport in transport_array:
    print(transport)




