#Простой калькулятор
from colorama import Fore, Back, Style
from colorama import init
init() # use Colorama to make Termcolor work on Windows too
print( Back.WHITE )
print( Fore.BLACK )
what = input("Что сделать? (+, -, *, /): ")
print( Back.CYAN )
print( Fore.BLACK )
a = float( input("Введите первое число: ") )
b = float( input("Введите второе число: ") )
print( Back.GREEN )
print( Fore.BLACK )
if what == "+":
    c = a + b
    print("Результат: " + str(c))
    print( Back.RED)
    print("Нажмите Enter для выхода из калькулятора")         
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
    print( Back.RED)
    print("Нажмите Enter для выхода из калькулятора")    
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
    print( Back.RED)
    print("Нажмите Enter для выхода из калькулятора")       
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
    print( Back.RED)
    print("Нажмите Enter для выхода из калькулятора")             
else:
    print( Back.RED )
    print( Fore.BLACK )   
    print:("Выбрана неверная операция")#если указана другая операция       
input()