import csv

def open_file ():
    '''Opens file, returns file object'''
    filename = 'GOOG.csv'#input('Enter filename: ')
    try:
        opened_file = open(filename, newline='')
        return opened_file
    
    except Exception:
        print('Filename', filename, 'not found!')
        quit()


def file_to_list(file_object):
    '''Turns the fileobject to a list'''
    '''and returns the list'''
    reader = csv.reader(file_object) #using the csv reader
    header = next(reader) # Getting the header 

    data_list = []

    for row in reader:
        # row = Date, open, high, low, close, adj close, volume
        date = row[0]
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        adj_close = float(row[5])
        volume = int(row[6])

        data_list.append([date, open_price, high, low, close, adj_close,volume])

    return data_list,header

def get_high (list_1):
   '''Finds the highest value of adjusted close'''
   '''and stores it in a list'''
   FULL_DATE = 0 # The date is always stored in the [0] of a line
   ADJUSTED_CLOSE = 6 # Adjust close value is always stored in [6] of a line
   a_list_of_highest = []
   for line in list_1:
       date = line[FULL_DATE]
       adjusted_c = line[ADJUSTED_CLOSE]
       a_list_of_highest.append([date, adjusted_c])
   highest = max(a_list_of_highest, key = lambda x: x[1])
    
   return highest


def get_monthly_sum(a_list):
    '''Takes the list and returns a new list'''
    '''only with [YEAR-MONTH, adjusted close and volume'''
    DATE = 0
    ADJUSTED_CLOSE = 5
    VOLUME = 6

    temp_list = []
    list_cleaned = []
    for line in a_list:
        line[0]= line[0][:7]
        temp_list.append(line)
    
    for line in temp_list:
        date = line[DATE]
        adj_close = line[ADJUSTED_CLOSE]
        vol = line[VOLUME]
        list_cleaned.append([date,adj_close,vol])
        
    return list_cleaned


    

   
    

    
    
    
    






def main():
    open_f = open_file()
    file_list, header = file_to_list(open_f)
    highest = get_high(file_list)
    print (highest)
    
    a_test = get_monthly_sum(file_list)
    print (a_test)

main()
