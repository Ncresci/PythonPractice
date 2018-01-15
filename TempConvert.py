user = float(input('What tempurature would you like to convert?'))
intial = input('What beginning unit?(f for Fehrenheit c for Celcius k for Kelvin)')
end = input('What ending unit?(f for Fehrenheit c for Celcius k for Kelvin)')

def converter(x, y, z):
    if intial == 'c':
        if end == 'f': 
            temp = (user * 1.8) + 32
            return(str(round(temp, 2)))
        elif end == 'k':
            temp = user + 273.15
            return(str(round(temp, 2)))
        else:
            print('Invalid input')
    elif intial == 'f':
        if end =='c':
            temp = (user - 32) * 0.5556
            return(str(round(temp, 2)))
        elif end == 'k':
            temp = (273.15 + (user - 32) * 0.5556)
            return(str(round(temp, 2)))
        else:
            print('Invalid input')
    elif intial == 'k':
        if end =='c':
            temp = user - 273.15
            return(str(round(temp, 2)))
        elif end == 'f':
            temp = ((user * 1.8) + 32) - 273.15
            return(str(round(temp, 2)))
        else:
            print('Invalid input')
    else:
        print('Not valid input!')

print(converter(user, intial, end))
