# Console.log eller Console.WriteLine
# print("goodbye world")
import decimal

num = 2
def summer(num1, num2):
    print( num1 + num2)

def Num2Creator(num1):
    print("give second number")
    NummerTo = decimal.Decimal(input())
    summer(num1, NummerTo)


def num1Creator(): 
    print("give first number")
    NummerEn = decimal.Decimal(input())
    Num2Creator(NummerEn)


num1Creator()


if num == 2:
    print("hei")
elif num == 1:
    print("hade")
else:
    print("kansje")