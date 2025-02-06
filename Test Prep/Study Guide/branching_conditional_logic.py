temperature = int(input())
if temperature >= 212:
    water_state="Boiling"
    print(water_state)
    if temperature == 212:
        optional_safety_comment= "Caution: Hot!"
        print(optional_safety_comment)
elif 115 <= temperature < 211:
    water_state= "Hot"
    print(water_state)
elif 80 <= temperature < 115:
    water_state= "Warm"
    print(water_state)
elif 33 <= temperature < 80:
    water_state= "Cold"
    print(water_state)
elif temperature < 33:
    water_state=  "Frozen"
    print(water_state)
    if temperature < 33:
        optional_safety_comment="Watch out for ice!"
        print(optional_safety_comment)
