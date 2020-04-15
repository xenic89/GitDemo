from pyautomation.Oops import Calc


class ChildImp(Calc):
    num2 = 200

    def __init__(self):
        Calc.__init__(self,2,10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summ()


obj = ChildImp()
print(obj.getCompleteData())