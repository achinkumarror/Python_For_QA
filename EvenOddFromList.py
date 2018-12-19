#print a even/odd number from given list

numbers = [4,2,42,4,2,1,1,20,3,5]

def evennumber(numbers):
    evenlist = []
    oddlist = []
    for n in numbers:
        if n%2==0:
            print("Even number is :", n)
            evenlist.append(n)
        if n%2 != 0:
             print("Odd number is :", n)
             oddlist.append(n)
    print("Even number list is: ", evenlist)
    print("Odd number list is: ", oddlist)

evennumber(numbers)