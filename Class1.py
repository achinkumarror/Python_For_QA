class Bank:
    name = "Hind Ror"
    dob = 30
    def withdraw(self):
        print("Hi this is withdraw method")

Bank()  #Object creation
Bank().name
print(Bank().name)
Bank().dob
print(Bank().dob)
Bank().withdraw()

Obj2= Bank() #Object creation and assigning it to a variable
Obj2.name
print(Obj2.name)
Obj2.dob
print(Obj2.dob)
Obj2.withdraw()