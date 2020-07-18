# Amartya Padmakumar 47886594. Lab sec 7. Project 4.

import mechanics

def row_input() -> int:
    # Gets number of rows from user
    try:
        row=int(input().strip())
    except ValueError:
        return
    if row < 4:
        return
    return row

def column_input() -> int:
    # Gets number of columns from user
    try:
        col=int(input().strip())
    except ValueError:
        return
    if col < 3:
        return
    return col

def display_field(field) -> None:
    # Displays field
    for i in range(3,len(field)):
        print('|',end='')
        for j in range(len(field[i])):
            print(field[i][j].center(3),end='')

        print('|')
    c=len(field[0])
    print(' ',end='')
    print('---'*c,end='')
    print(' ')

def interface():
    row=row_input()
    if row == None:
        return
    col=column_input()
    if col== None:
        return
    field_contents=input()
    if field_contents == 'EMPTY':
        field = mechanics.build_empty_field(row,col)
    elif field_contents == 'CONTENTS':
        contents = mechanics.read_contents(row,col)
        if contents == None:
            return
        field = mechanics.build_content_field(contents)
        if field == None:
            return
    else:
        return
    game = mechanics.GameState(field)
    game.move_jewels_down()
    game.match_jewels()
    display_field(game.field)
    game.remove_matches()
    game.move_jewels_down()
    while game.game_over==False:
        command=input()
        if len(command.strip())==0:
            game.move_jewels_down()
            if game.faller_present:
                game.current_faller.move_faller_down(game)
        elif command[0] == 'F':
            if game.faller_present == False:
                if mechanics.get_faller_info(command)==None:
                    return
                faller=mechanics.Faller(command)
                faller.place_faller(game)
                faller.move_faller_down(game)
        elif command == 'R':
            if game.faller_present == True:
                game.current_faller.rotate_faller(game)
        elif command == '>':
            if game.faller_present == True:
                game.current_faller.move_faller_right(game)
        elif command == '<':
            if game.faller_present == True:
                game.current_faller.move_faller_left(game)
        elif command == 'Q':
            return
        game.move_jewels_down()
        game.match_jewels()
        display_field(game.field)
        game.remove_matches()
        game.move_jewels_down()
        game.check_game_over()
        if game.game_over == True:
            print('GAME OVER')
            return
        

if __name__ == '__main__':
    interface()

