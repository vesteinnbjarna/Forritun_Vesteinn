# Present population in the US
present_population = 307357870

# creating a variable for how many in one year
# the first number is seconds in one minute
# the second number is minutes in one hour
# the third number is hours in a single day
# the fourth is the exact number of days in a year
sec_year = (60 * 60 * 24 * 365)



# A variable for birthrate for 1 year
birth_rate = float(sec_year / 7)



# Variable for mortality rate for 1 year :
death_rate = float(sec_year / 13)



# Variable for immigration rate for 1 year
immigration_rate = float(sec_year / 35)



years = int(input('Years: '))
# Creating and if and else statement 
if years >= 0:
    #changing years to a float
    years = float(years)
    # creating a population increase and decrease variable
    birth_year = years * birth_rate
    
    death_year = years * death_rate
    
    immigration_year = years * immigration_rate
    

# Population growth in regrards to years:
    pop_increase = birth_year + immigration_year
    pop_decrease = (-1.0 ) * (death_year)



    population_change = pop_increase + pop_decrease
   

# Adding a calculation for future population and
# changing the future population to an integer

    future_population = present_population + population_change
    future_population_int = int(future_population)
    years_int = int(years)
    print('New population after', years_int, 'years is', future_population_int)
else:
    print('Invalid input!')
