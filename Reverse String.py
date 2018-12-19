def rev_name(name):
    strlen = (len(name))-1

    while strlen > -1:
        print(name[strlen])
        strlen -=1

rev_name("My name is Achin Ror")