temperature = int(input())

if temperature < 33:
        print('Frozen')
        print("Watch out for ice!")
elif 33 <= temperature < 80:
    print('Cold')
elif 80 <= temperature < 115:
    print('Warm')
elif 115 <= temperature < 211:
    print('Hot')
elif temperature >= 212:
    print('Boiling')
    if temperature == 212:
        print("Caution: Hot!")
elif temperature < 33:
    print("Watch out for ice!")
