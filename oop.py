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

hpMonitor.switchOnMonitor()
dellMonitor.switchOnMonitor()


print(f"===> {hpMonitor.shape}")
print(f"===> {dellMonitor.shape}")
