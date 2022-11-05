def fibannoci(f):
    a = 0
    b = 1

    if f <=0:
        print('Sorry, we now are operating on numbers greater than zero.')

    elif f == 1:
        print(a)
        print(b)
        print(b)

    

    else:
        print(a)
        print(b)

        for i in range(2, f+1):
            c = a + b
            print(c)
            a = b
            b = c
            

choice = int(input('Enter a number here: '))
fibannoci(choice)