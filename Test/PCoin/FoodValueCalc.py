import hashlib
class FoodCalculator:
    def getFoodValue(self,foodName):
        x=hashlib.md5(foodName.encode('utf-8'))
        value=sum([ord(i) for i in x.hexdigest()])
        return value % 10
if __name__ == '__main__':
    print(FoodCalculator().getFoodValue("苹果"))