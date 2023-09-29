""" Треугольник на классах """
#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

""" ab = int(input("Введите сторону ab : "))
bc = int(input("Введите сторону bc : "))
ac = int(input("Введите сторону ac : ")) """

class Triangle:
  
    def __init__(self,ab, bc, ac ):
        self.ab = ab
        self.bc = bc
        self.ac = ac        
         
    def isosceles (self):
        if ab + bc > ac and bc + ac > ab and ac + ab > bc:
            if ab == bc != ac or ab == ac != bc or ac == bc != ab:
                return True 
    
    def versatile (self):
        if ab != bc or ab != ac or ac != bc:
            return True
        
    def equilateral (self):
        if ab == bc and ab == ac and ac == bc:
            return True        
""" else :
    retern False """
    
tringl1 = Triangle(7,9,10)
print (f'равнобедренный tringl1.equilateral()