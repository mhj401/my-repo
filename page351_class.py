class House:
    def __init__(self, year, acreages, address, price):
        self.year = year
        self.acreages = acreages
        self.adress = address
        self.price = price

    def change_price(self, rate):
        self.price = self.price * rate

    def show_info(self):
        print("""***This house is built in {},
                acreages: {}
                adress: {}
                price {}""".format(self.year,self.acreages, self.adress, self.price))

if __name__ == '__main__':
    house_A = House(1999, 100, "seoul", 777777777)
    house_A.show_info()
