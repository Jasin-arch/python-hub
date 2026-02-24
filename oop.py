# """
# OOP: object Oriented 

# """

# class Car:

    # attributes

#     def __init__(self, name, model, color, price):
#         self.name = name
#         self.model = model
#         self.color = color
#         self.price = price
        
#     # class Car:    

#         def cardescription(self):
#             print(f"This is a {self.model} it is of color {self.color}")


# mercedes = Car("Mercedes gle-450", "Mercedes", "Black", "7.5M")


# output = mercedes
# output = mercedes.model

# mercedes.cardescription(self)

# GLE_450= Car("GLE-450", "Mercedes", "Blue", "8.5")
# GLE_450.cardescription()


# output = f"This is a {self.model} it is of color {self.color}"
# GLE_450.name



# print("*******************")       
# print(output)
# print("*******************")       
class Monitor:

    def __init__(self, shape, resolution, size, yom, color):
        self.shape = shape
        self.resolution = resolution
        self.size = size
        self.yom = yom
        self.color = color

    def switchOnMonitor(self):
        print("Turning on monitor")
        
    def displayInterface(self):
        print("display OS")

# hpMonitor = Monitor()
# dellMonitor = Monitor()

            
hpMonitor = Monitor("rectanular", "1080", "21", "2000", "gray")
dellMonitor = Monitor(shape="oval", resolution="1280", size="36", yom="2010", color="black")

# hpMonitor.switchOnMonitor()
# dellMonitor.switchOnMonitor()


# print(f"===> {hpMonitor.shape}")
# print(f"===> {dellMonitor.shape}")



class Car:

    def __init__(self, model, color, isElectric):
        self.model = model
        self.color = color
        self.isElectric = isElectric

    def carFeatures(self):
        print(f"THis vehecle is of model {self.model} it of color{self.color} and is electric {self.isElectric}")
        
    def startCar(self):
        print(f"Starting oyur {self.model} car!")    

tesla = Car("Tesla", "Space gray", True)
toyota = Car("Toyota", "White", False)

# tesla.carFeatures()
# toyota.carFeatures()


# # print(tesla.model)
# # print(toyota.isElectric)
# # print(f"THis vehecle is of model {self.model}")


# class Tuktuk:

#     def __init__(self, model, color, isElectric, numberOfWheels):
#         super().__init__(model, color, isElectric)
#         self.numberOfWheels = numberOfWheels

#     def wheelNumber(self):
#         print(f"Your tuktuk has {self.numberOfWheels}")   

    



class Book:

    def __init__(self, title, author, yop, publisher, costOfProduction):
        self.title = title
        self.author = author
        self.yop = yop
        self.publisher = publisher
        self.costOfProduction = costOfProduction


    def aboutBook(self):
        print(f"TITLE: {self.title}")
        print(f"AOUTHOR: {self.author}")
        print(f"YOP: {self.yop}")
        print(f"PUBLISHER: {self.publisher}")
        print(f"PRODUCTION: {self.costOfProduction}")

# alchemist = Book()
# word = Book()

alchemist = Book("The Alchemist", "Paulo Jasin", "1988", "Kasuku", "3500")
word = Book("The Word", "Fredrick", "2026", "crown", "2000")

output = alchemist.author
alchemist.aboutBook()
word.aboutBook()

# print(output)

        