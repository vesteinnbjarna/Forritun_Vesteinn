# Par of the holes:

hole_1 = 5
hole_2 = 4
hole_3 = 3
hole_4 = 4
numb_holes = 1


while numb_holes < 4: 
    print('Par of hole 1:', hole_1)
    par_score = int(input('Enter your par score for hole one: '))
    if par_score - hole_1 == -3:
        print ('Albatross')
    elif par_score - hole_1 == -2:
        print ('Eagle')
    elif par_score - hole_1 == -1:
        print ('Birdie')
    elif par_score - hole_1 == 0:
        print('Par')
    elif par_score - hole_1 == 1:
        print('bogey')
    elif par_score - hole_1 == 2:
        print('double bogey')
    elif par_score - hole_1 == 3:
        print('triple bogey') 
    elif par_score - hole_1 > 3:
        print('bad hole')
    elif par_score - hole_1 < -3:
        print ('invalid score')
    numb_holes +=1

    print('Par of hole 2:', hole_2)
    par_score = int(input('Enter your par score for hole two: '))
    if par_score - hole_2 == -3:
        print ('Albatross')
    elif par_score - hole_2 == -2:
        print ('Eagle')
    elif par_score - hole_2 == -1:
        print ('Birdie')
    elif par_score - hole_2 == 0:
        print('Par')
    elif par_score - hole_2 == 1:
        print('bogey')
    elif par_score - hole_2 == 2:
        print('double bogey')
    elif par_score - hole_2 == 3:
        print('triple bogey') 
    elif par_score - hole_2 > 3:
        print('bad hole')
    elif par_score - hole_2 < -3:
        print ('invalid score')
    numb_holes +=1
    
    print('Par of hole 3:', hole_3)
    par_score = int(input('Enter your par score for hole three: '))
    if par_score - hole_3 == -3:
        print ('Albatross')
    elif par_score - hole_3 == -2:
        print ('Eagle')
    elif par_score - hole_3 == -1:
        print ('Birdie')
    elif par_score - hole_3 == 0:
        print('Par')
    elif par_score - hole_3 == 1:
        print('bogey')
    elif par_score - hole_3 == 2:
        print('double bogey')
    elif par_score - hole_3 == 3:
        print('triple bogey') 
    elif par_score - hole_3 > 3:
        print('bad hole')
    elif par_score - hole_3 < -3:
        print ('invalid score')
    numb_holes +=1

    print('Par of hole 4:', hole_4)
    par_score = int(input('Enter your par score for hole four: '))
    if par_score - hole_4 == -3:
        print ('Albatross')
    elif par_score - hole_4 == -2:
        print ('Eagle')
    elif par_score - hole_4 == -1:
        print ('Birdie')
    elif par_score - hole_4 == 0:
        print('Par')
    elif par_score - hole_4 == 1:
        print('bogey')
    elif par_score - hole_4 == 2:
        print('double bogey')
    elif par_score - hole_4 == 3:
        print('triple bogey') 
    elif par_score - hole_4 > 3:
        print('bad hole')
    elif par_score - hole_4 < -3:
        print('invalid score')
    numb_holes += 1