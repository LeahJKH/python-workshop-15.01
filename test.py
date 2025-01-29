# Console.log eller Console.WriteLine
# print("goodbye world")

#her importer vi decimal så vi kan hente ut desimal tall senere
import decimal

# num = 2

def summer(num1, num2):
    print( num1 + num2)

def Num2Creator(num1):
    print("give second number")
    NummerTo = decimal.Decimal(input()) # her bruker vi input så vi kan skrive selv i consollen
    summer(num1, NummerTo)


def num1Creator(): 
    print("give first number")
    NummerEn = decimal.Decimal(input()) # her bruker vi input så vi kan skrive selv i consollen
    Num2Creator(NummerEn) # vi sender tallet videre i neste function som et argument


num1Creator()


if num == 2:
    print("hei")
elif num == 1:
    print("hade")
else:
    print("kansje")