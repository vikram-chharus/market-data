class data():
    def setPrice(self, price):
        file = open("D:\\plot.txt", 'w', encoding='utf-8')
        file.write(price)
        file.close()
    def getPrice(self):
        file = open("D:\\plot.txt", 'r', encoding='utf-8')
        temp = file.readline()
        return float(temp)

