#print a duplicate numbers from given list
numbers = [4,2,42,4,2,1,1,20,3,5]

def dupnumber(numbers):
    duplist =[]
    for n in range (len(numbers)-1):
        if numbers[n] == numbers[n+1]:
            print("Duplicate nbr is :", numbers[n])
            duplist.append(numbers[n])

    print("Dup number list is: ", duplist)

dupnumber(numbers)