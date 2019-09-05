inp_str = input('Enter a 6 number integer: ')
inp_int = int(inp_str)

#Af hverju virkar þetta?
# heiltöludeiling með 10 tekur einn staf, 100 tvo stafi og 1000 þrjá
first_three = inp_int // 1000
print (first_three)

#Virkar hérna af því fyrst er heiltöludeiling með 100 og núllar út 56  
# síðan er afgangurinn af þeirri tölu mod 100 síðustu tveir stafirnir
middle_two = inp_int // 100 % 100
print (middle_two)


# Virkar af því að afgangurinn af verður síðustu tveir aukastafirnir
last_two = inp_int % 100
print(last_two)


