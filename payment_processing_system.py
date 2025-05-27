# This code implements method overloading in python
# Python doesn't support the traditional overlaoding like in Java but it can stimulate overloading by using default arguments

class PaymentProcessor:
    def pay(self, amount, currency="UGX"):
        print(f"Paying {amount} in {currency}") 

p = PaymentProcessor()
p.pay(1200)
p.pay(1200,"EURO")        