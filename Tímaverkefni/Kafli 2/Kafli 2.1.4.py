# 1. Með hversu mörgum stigum leiðir liðið?
points_str = input("Með hversu mörgum stigum leiðir annað liðið? ")
points_ahead_int = int(points_str)

# 2 Draga þrjá frá
lead_calculation_float = float(points_ahead_int - 3)

# 3 +0.5 ef liðið er með boltann annars -0,5
has_ball_str = input("Er liðið með boltann? (Já eða Nei): ")

if has_ball_str == "Já":
    lead_calculation_float = lead_calculation_float + 0.5
else:
    lead_calculation_float = lead_calculation_float - 0.5

# Ef lead_calculation_float er < 0 þá er = 0

if lead_calculation_float < 0:
    lead_calculation_float = 0

# Setja í annað veldi
lead_calculation_float = lead_calculation_float ** 2

# Sek eftir af leiknum
sec_remaining_int = int(input("Hvað eru margar sek eftir: "))

# Er fjöldi sek sem er eftir meiri en lead_calculation_float?
if lead_calculation_float > sec_remaining_int:
    print("Forskotið er öruggt!")
else:
    print("Forskotið er ekki öruggt!")


                   
