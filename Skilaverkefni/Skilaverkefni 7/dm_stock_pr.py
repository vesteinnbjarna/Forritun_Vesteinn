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
    reader = csv.reader(file_object) #
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

        data_list.append([date, open_price, high, low, close, adj_close, volume])

    return data_list

def get_monthly_sum():
    pass
    

    
    
    
    






def main():
    open_f = open_file()
    file_list = file_to_list(open_f)
    
    print (file_list)
    #monthly_avarage = get_monthly_avarages(file_list)

main()
