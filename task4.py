""" Банкомат на классах """
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
#  При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
# операцией, даже ошибочной
# Любое действие выводит сумму денег


                                # Пополнение
MULTIPLICITY = 50 
MIN = 30
MAX = 600
balance = 0
STEP = 3
TAX = 0.1 # децемал поставить для плавающей точки
LIMIT = 5000000 

class Add:
    
    def __init__(self, add_sum):
        self.add_sum = add_sum
         
    def func_add_sum (self):
        if self.add_sum >= MULTIPLICITY and self.add_sum% MULTIPLICITY == 0:
            return self.add_sum
        else:    
            print("Сумма пополнения должна быть кратна 50")
            exit()
    

class Balance :
    
    def __init__(self, balance, class1_add):
        self.add_sum = class1_add.add_sum
        self.balance = balance
    
    def total (self):
        return self.balance + self.add_sum 
    
class Tax_sum:
    
    def __init__(self,charge, class1_add, class2_balance):
        self.add_sum = class1_add.add_sum
        self.balance = class2_balance.balance
        self.charge = charge
        
    def  wealth_tax (self):
        if self.balance > LIMIT :
            charge = self.add_sum * TAX
            self.balance -= charge
            return charge
                 
     
    
if __name__ == '__main__':  
    
    money = Add (add_sum=int(input("Введите сумму для пополнения счета : ")))
    money.func_add_sum()  
    total1= Balance (0,money)
    total2 = Tax_sum (0, money, total1)
    print(f'Ваш баланс : {total1.total()}')
    print(f"Ваш баланс c учетом налога на богатство: {total2.wealth_tax()}") 

   
    
"""     
  
  
                                 # Снятие 
take_sum = int(input("Введите сумму для снятия со счета : "))
if take_sum > balans:
    print(f"На вашем счете недостаточно средств!")
    print(f"Ваш баланс : {balans}")
elif take_sum >= MULTIPLICITY and take_sum% MULTIPLICITY == 0:
    balans -=take_sum
    print(f"Ваш баланс: {balans}")
else:
    print("Сумма снятия должна быть кратна 50")
    print(f"Ваш баланс : {balans}")


if balans > sum :
    charge = take_sum * TAX
    balans -= charge
    print(f"Ваш баланс c учетом налога на богатство: {balans}")

def bank_commission(_take_sum):
    balans = 1000
    num = _take_sum*commission/100
    if MAX > num > MIN:
        balans -= (_take_sum + num)
        print(f"Ваш баланс: {balans}")
    elif num > MAX:
        balans -= (_take_sum +MAX)
        print(f"Ваш баланс: {balans}")
    elif num < MIN:
        balans -= (_take_sum + MIN)  
        print(f"Ваш баланс: {balans}")    """