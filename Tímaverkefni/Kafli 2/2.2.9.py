# Reikna út einkunn A, B , C etc út frá prósentu

percent_float = float(input("Sláðu inn prósentuna þína: " ))

if 90 <= percent_float < 100:
    print('Þú færð A')
elif 80 <= percent_float < 90:
    print('Þú færð B')
elif 70 <= percent_float < 80:
    print('Þú færð C')
elif 60 <= percent_float < 70:
    print('Þú færð D')
else:
    print('Þú ert í vondum málum ven')

                      
