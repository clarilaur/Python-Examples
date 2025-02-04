while True:
    rows = input('here:')

    if rows.lower() == 'done':  # Exit loop if the user types 'done'
        break

    words = rows.split()
    result = ','.join(words)

    print(result)
