birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} #DICTIONARY UNORDERED

while True: #WHILE LOOP CHECK IF CONDITIONS ARE True
    print('Enter a name: (blank to quit)') #PLEASE GIVE A NAME
    name = input() #ACCEPT NAME
    if name == '': #IF IT'S BLANK THEN WE STOP
        break
    
    if name in birthdays: #IS THIS NAME IN THE BDAY DICTIONARY
        print(birthdays[name] + ' is the birthday of ' + name) #PRINT THE NAME WITH BIRTHDAY
    else:
        print('I do not have birthday information for ' + name) #IF NAME NOT RECOGNIZED
        print('What is their birthday?') #WHAT IS THEIR BIRTHDAY FOR UNRECOGNIZED NAME
        bday = input() #ACCEPT DOB
        birthdays[name] = bday #update name in dictionary with bday variable
        print('Birthday database updated.')