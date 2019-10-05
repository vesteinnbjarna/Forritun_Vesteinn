def my_function(param): #print value and id:
    param = 32
    print('parameter value is: {}, its ID is: {}'.format(param,id(param)))

arg = 25
print ('arg: {}, ID: {}'.format(arg, id(arg)))

my_function(arg)