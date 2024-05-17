class Calculator:
    def add(self, x, y):
        return x + y
    
    def multi(self,x,y):
        return x*y
 
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")
        

    def subtract(number1, number2):
        result = number1 - number2
        return result