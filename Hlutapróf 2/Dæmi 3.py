def enter_sets ():
    '''Get sets from user'''
    set1 = input('Enter elementes of a list seperated by space: ')
    set2 = input('Enter elementes of a list seperated by space: ')
    set1 = set1.split()
    set2 = set2.split()

    return set1, set2

def check_if_sets(set_a, set_b):
    '''Turns the inputs to sets'''
    set_check1 = []
    for element in set_a:
        
        if element not in set_check1:
            set_check1 += element10 1
    set_check2 = []
    for element in set_b:
        
        if element not in set_check2:
            set_check2 += element

    return set_check1, set_check2

def intersection (set_1, set_2):
    '''Gets intersection of sets'''
    intersection = []
    for element in set_1:
        if element in set_2:
            intersection += element
    
    for element in set_2:
        if element in set_1:
            intersection+= element
    
    result = []

    for element in intersection:
        if element not in result:
            result += element
    
    print('Intersection: {}'.format(result))

def union (set_1, set_2):
   '''Gets the union of the sets'''
   result = []
   for element in set_1:
       if element not in result:
           result += element
   for element in set_2:
        if element not in result:
            result += element


   print('Union:  {}'.format(result))

def sorted_sets (set_a, set_b):
    '''sorts the sets in asscending order'''
    set_1_sorted = sorted(set_a)
    set_2_sorted = sorted(set_b)
    print('Set 1: ', set_1_sorted)
    print('Set 2:', set_2_sorted)
    
    return set_1_sorted, set_2_sorted



# Main:

set_1, set_2 = enter_sets()
new_set1, new_set2 = check_if_sets(set_1, set_2)
sorted_set_1, sorted_set_2 = sorted_sets(new_set1,new_set2)
intersection(sorted_set_1, sorted_set_2)
union(sorted_set_1, sorted_set_2)