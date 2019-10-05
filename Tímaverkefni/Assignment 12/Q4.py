
def merge_lists(first_list, second_list):
    a_new_list = []

    for element in first_list:
        if element not in a_new_list:
            a_new_list.append(element)

    for element in second_list:
        if element not in a_new_list:
            a_new_list.append(element)

    
    a_new_list = sorted(a_new_list)
    return a_new_list



# Main program starts here - DO NOT change it

def main():
    list1 = input("Enter elements of list separated by commas: ").split(',')
    list2 = input("Enter elements of list separated by commas: ").split(',')
    print(merge_lists(list1, list2))

main()