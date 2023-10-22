seasons = ('Winter', 'Spring', 'Summer', 'Autumn', 'Winter')

month_number = int(input("Enter a month number (1-12): "))

if 1 <= month_number <= 12:
    season_index = month_number // 3
    season = seasons[season_index]

    print(f"The season for month {month_number} is {season}")
else:
    print("Invalid input. Month number must be between 1 and 12.")
