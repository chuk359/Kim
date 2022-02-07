class train:

    def __init__(self, model = "deafult_model", company = "deafult_comapany", number = "deafult_number", capasity = "deafult_capasity"):
        self.__model = model
        self.__company = company
        self.__number = number
        self.__capasity = int(capasity)

    def move(self, to):
        print(f"Train {self.__model} belongs to {self.__company} corporation, number {self.__number} goes to railwastation {to}")

    def stop(self, where):
        print(f"Train {self.__model} belongs to {self.__company} corporation, number {self.__number} arrived at railwastation {where}")

    def load(self, amount):
        if amount > self.__capasity:
            print(f"Train {self.__model} belongs to {self.__company} corporation, number {self.__number} can't be loaded this amount {amount}")
        else:
            print(f"Train {self.__model} belongs to {self.__company} corporation, number {self.__number} was loaded this amount {amount}")

train1 = train("SD70M-2", "EMD", "2017E", "18000")
train1.move("Port Elizabeth")
train1.stop("Port Elizabeth")
train1.load(20000)
train1.load(15000)