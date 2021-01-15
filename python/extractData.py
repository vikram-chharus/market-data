import os, data
class ExtractData():
    price = data.data()
    started = False
    def sendData(self, tick):
        time = tick['ltt']
        data = ''
        if time != 'NA':
            for key in tick.keys():
                data += key + " | " + tick[key] + " | "
            print(data+'\n')
            ExtractData.price.setPrice(tick['ltp'])
            file = open("D:\\SBI_2.txt", 'a', encoding='utf-8')
            file.write(data+"\n")
            file.close()
            if not ExtractData.started:
                os.system(" start D:\\Drive\\OneDrive\\TradingBot\\apis\\plot.py")
                ExtractData.started = True
