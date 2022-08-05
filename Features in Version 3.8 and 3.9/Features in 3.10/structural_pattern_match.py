
rich_avenger = 'Tony'
# Example 01
match rich_avenger:
    case 'Tony':
        print(f'{rich_avenger} is the richest avenger')
    case _:
        print('He is not the richest avenger')

# Example 02
match rich_avenger:
    case 'Tony' | 'IronMan':
        print(f'{rich_avenger} is the richest avenger')
    case _:
        print('He is not the richest avenger')

# Example 03
avengers = ('Tony','Steve','Thor')
avengers = ('Peter','Stephen','Wong')
match avengers:
    case ('Tony','Steve','Thor'):
        print('Old Avengers')
    case ('Peter','Stephen','Wong'):
        print('New Avengers')
    case _:
        print('Not an Avenger')