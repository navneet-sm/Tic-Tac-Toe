print(f"""---------
|       |
|       |
|       |
---------"""
      )
play_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
pg_str = '         '
count = 0                                                                               # for alternating moves
while True:
    move = input('Enter the coordinates:')
    the_split = move.split()                                                                 # this is a list
    if the_split[0].isnumeric() is False or the_split[1].isnumeric() is False:
        print('You should enter numbers!')
    elif int(the_split[0]) > 3 or int(the_split[1]) > 3:
        print('Coordinates should be from 1 to 3!')
    elif play_grid[int(the_split[0])-1][int(the_split[1])-1] != ' ':
        print('This cell is occupied! Choose another one!')
    elif play_grid[int(the_split[0])-1][int(the_split[1])-1] == ' ':
        if count == 0:
            play_grid[int(the_split[0])-1][int(the_split[1])-1] = 'X'  # subtracting 1 for common understanding
            pg_str = ''.join(map(str, sum(play_grid, [])))                          # converting list to string
            count = 1
        elif count == 1:
            play_grid[int(the_split[0]) - 1][int(the_split[1]) - 1] = 'O'  # subtracting 1 for common understanding
            pg_str = ''.join(map(str, sum(play_grid, [])))                          # converting list to string
            count = 0
        print(f"""---------
| {' '.join(pg_str[:3])} |
| {' '.join(pg_str[3:6])} |
| {' '.join(pg_str[6:])} |
---------"""
              )
        solutions = [pg_str[:3], pg_str[3:6], pg_str[6:],
                     pg_str[:9:3], pg_str[1:9:3], pg_str[2:9:3],
                     pg_str[:9:4], pg_str[2:8:2]]
        if 'XXX' in solutions:
            print('X wins')
            break
        elif 'OOO' in solutions:
            print('O wins')
            break
        elif ' ' not in pg_str:
            print('Draw')
