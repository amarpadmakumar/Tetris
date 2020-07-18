# Amartya Padmakumar 47886594. Lab sec 7. Project 4.
from copy import deepcopy

def build_empty_field(row:int, col:int) -> [[str]]:
    # Builds empty field
    field=[]
    for i in range(3):
        field.append([])
        for j in range(col):
            field[-1].append(' ')
            
    for i in range(row):
        field.append([])
        for j in range(col):
            field[-1].append(' ')
    return field

def read_contents(row:int, col:int) -> [[str]]:
    # Reads contents of field from user
    contents=[]            
    for i in range(row):
        line=input()
        contents.append([])
        for j in range(col):
            try:
                contents[-1].append(line[j])
            except IndexError:
                return
    return contents

def build_content_field(contents: [[str]]) -> [[str]]:
    # Builds field with contents specified
    field=[]
    for i in range(3):
        field.append([])
        for j in range(len(contents[i])):
            field[-1].append(' ')
            
    for i in range(len(contents)):
        field.append([])
        for j in range(len(contents[i])):
            try:
                field[-1].append(contents[i][j])
            except IndexError:
                return
    return field

def get_faller_info(line:str) -> list:
    # Gets column and color info of faller
    try:
        column=int(line[2])
        faller=[line[4],line[6],line[8]]
    except ValueError:
        return
    except IndexError:
        return
    return [column,faller]

            

class GameState:

    def __init__(self, field):
        self.field=field
        self.game_over = False
        self.faller_present = False

    def check_game_over(self) -> bool:
        # Checks if game is over
        over=False
        for i in range(3):
            for j in range(len(self.field[i])):
                if self.field[i][j][0] not in ' [|':
                    self.game_over=True
                    over = True
                    return over
        return over

    def move_jewels_down(self) -> [[str]]:
        # Move all jewels down if possible
        new=deepcopy(self.field)
        while True:
            move=False
            for i in range(len(self.field)):
                for j in range(len(self.field[i])):
                    if new[i][j][0] not in ' |[':
                        try:
                            if new[i+1][j] == ' ':
                                new[i+1][j] = new[i][j]
                                new[i][j] = ' '
                                move=True
                        except IndexError:
                            pass
            if move == False:
                self.field=new
                return new

    def _match_horizontal(self) -> [[str]]:
        # Match jewels horizontally
        new=deepcopy(self.field)
        for i in range(3,len(new)):
            for j in range(len(new[i])):
                if new[i][j][0] not in ' [|':
                    count=1
                    for n in range(1,len(new[i])):
                        try:
                            if new[i][j] == new[i][j+n]:
                                count+=1
                            elif new[i][j][0] == '*':                           
                                if new[i][j+n][0] == '*':
                                    if new[i][j][1] == new[i][j+n][1]:
                                        count+=1
                                    else:
                                        break
                                else:
                                    if new[i][j][1] == new[i][j+n]:
                                        count+=1
                                    else:
                                        break
                            elif new[i][j+n][0] == '*':
                                if new[i][j]==new[i][j+n][1]:
                                    count+=1
                                else:
                                    break
                            else:
                                break
                        except IndexError:
                            break
                    if count >=3:
                        for d in range(count):
                            if new[i][j+d][0] != '*':
                                new[i][j+d] = f'*{self.field[i][j+d]}*'
        self.field=new
        return new

    def _match_vertical(self) -> [[str]]:
        # Match jewels vertically
        new=deepcopy(self.field)
        for i in range(3,len(new)):
            for j in range(len(new[i])):
                if new[i][j][0] not in ' [|':
                    count=1
                    for n in range(1,len(new)):
                        try:
                            if new[i][j] == new[i+n][j]:
                                count+=1
                            elif new[i][j][0] == '*':                           
                                if new[i+n][j][0] == '*':
                                    if new[i][j][1] == new[i+n][j][1]:
                                        count+=1
                                    else:
                                        break
                                else:
                                    if new[i][j][1] == new[i+n][j]:
                                        count+=1
                                    else:
                                        break
                            elif new[i+n][j][0] == '*':
                                if new[i][j]==new[i+n][j][1]:
                                    count+=1
                                else:
                                    break
                            else:
                                break
                        except IndexError:
                            break
                    if count >=3:
                        for d in range(count):
                            if new[i+d][j][0] != '*':
                                new[i+d][j] = f'*{self.field[i+d][j]}*'
        self.field=new
        return new

    def _match_diagonal(self) -> [[str]]:
        # Match jewels diagonally
        new=deepcopy(self.field)
        for i in range(3,len(new)):
            for j in range(len(new[i])):
                if new[i][j][0] not in ' [|':
                    for m in range(2):
                        count1=1
                        count2=1
                        for n in range(1,len(new)):
                            if m == 0:
                                try:
                                    if new[i][j] == new[i+n][j+n]:
                                        count1+=1
                                    elif new[i][j][0] == '*':                           
                                        if new[i+n][j+n][0] == '*':
                                            if new[i][j][1] == new[i+n][j+n][1]:
                                                count+=1
                                            else:
                                                break
                                        else:
                                            if new[i][j][1] == new[i+n][j+n]:
                                                count1+=1
                                            else:
                                                break
                                    elif new[i+n][j+n][0] == '*':
                                        if new[i][j]==new[i+n][j+n][1]:
                                            count1+=1
                                        else:
                                            break
                                    else:
                                        break
                                except IndexError:
                                    break

                            elif m==1:
                                try:
                                    if new[i][j] == new[i+n][j-n] and (j-n) in range(len(new[i])) :
                                        count2+=1
                                    elif new[i][j][0] == '*':                           
                                        if new[i+n][j-n][0] == '*' and (j-n) in range(len(new[i])):
                                            if new[i][j][1] == new[i+n][j-n][1]:
                                                count2+=1
                                            else:
                                                break
                                        else:
                                            if new[i][j][1] == new[i+n][j-n] and (j-n) in range(len(new[i])):
                                                count2+=1
                                            else:
                                                break
                                    elif new[i+n][j-n][0] == '*':
                                        if new[i][j]==new[i+n][j-n][1] and (j-n) in range(len(new[i])):
                                            count2+=1
                                        else:
                                            break
                                    else:
                                        break
                                except IndexError:
                                    break
                        if count1 >=3:
                            for d in range(count1):
                                if new[i+d][j+d][0] != '*':
                                    new[i+d][j+d] = f'*{self.field[i+d][j+d]}*'
                        elif count2 >=3:
                            for d in range(count2):
                                if new[i+d][j-d][0] != '*':
                                    new[i+d][j-d] = f'*{self.field[i+d][j-d]}*'
        self.field=new
        return new

    def match_jewels(self) -> [[str]]:
        # Matches jewels vertically, horizontally and diagonally
        self._match_horizontal()
        self._match_vertical()
        self._match_diagonal()
        return self.field

    def remove_matches(self) -> [[str]]:
        # Replaces matched jewels with empty space
        new=deepcopy(self.field)
        for i in range(3,len(new)):
            for j in range(len(new[i])):
                if self.field[i][j][0] == '*':
                    new[i][j] = ' '
        self.field=new
        return new
                
    

class Faller:

    def __init__(self,line):
        self.column = get_faller_info(line)[0]
        self.colors = get_faller_info(line)[1]
        self.status = 'FALLING'

    def place_faller(self, game:GameState) -> [[str]]:
        # Places faller on board
        game.faller_present = True
        game.current_faller=self
        new=deepcopy(game.field)
        new[0][self.column-1]=f'[{self.colors[0]}]'
        new[1][self.column-1]=f'[{self.colors[1]}]'
        new[2][self.column-1]=f'[{self.colors[2]}]'
        game.field=new
        return new

    def move_faller_down(self, game:GameState) -> [[str]]:
        # Moves faller down
        new=deepcopy(game.field)
        counter=0
        move_down=False
        if self.status == "LANDED":
            new=self.freeze_faller(game)
            return new
        elif self.status =='FROZEN':
            return new
        for i in range(len(game.field)):
            if game.field[i][self.column-1][0] == '[' and game.field[i][self.column-1][2]==']':
                counter+=1
                if counter==3:
                    bottom=i
        try:
            if game.field[bottom+1][self.column-1] == ' ':
                move_down=True
            else:
                new=self.land_faller(game)
                game.field=new
                return game.field
        except IndexError:
            return game.field
        if move_down == True:
            try:
                if game.field[bottom+2][self.column-1] == ' ':
                    new[bottom+1][self.column-1]=game.field[bottom][self.column-1]
                    new[bottom][self.column-1]=game.field[bottom-1][self.column-1]
                    new[bottom-1][self.column-1]=game.field[bottom-2][self.column-1]
                    new[bottom-2][self.column-1] = ' '
                else:
                    new[bottom+1][self.column-1]=game.field[bottom][self.column-1]
                    new[bottom][self.column-1]=game.field[bottom-1][self.column-1]
                    new[bottom-1][self.column-1]=game.field[bottom-2][self.column-1]
                    new[bottom-2][self.column-1] = ' '
                    game.field=new
                    new=self.land_faller(game)
            except IndexError:
                new[bottom+1][self.column-1]=game.field[bottom][self.column-1]
                new[bottom][self.column-1]=game.field[bottom-1][self.column-1]
                new[bottom-1][self.column-1]=game.field[bottom-2][self.column-1]
                new[bottom-2][self.column-1] = ' '
                game.field=new
                new=self.land_faller(game)
            finally:
                game.field=new
                return new

    def land_faller(self, game:GameState) -> [[str]]:
        # Lands Faller
        new=deepcopy(game.field)
        for i in range(len(game.field)):
            if game.field[i][self.column-1][0] == '[' and game.field[i][self.column-1][2] == ']':
                jewel = game.field[i][self.column-1][1]
                new[i][self.column-1] = f'|{jewel}|'
        self.status = 'LANDED'
        game.field=new
        return new
    
    def rotate_faller(self, game: GameState) -> [[str]]:
        # Rotates faller
        x=deepcopy(self.colors)
        self.colors[0],self.colors[1],self.colors[2] = x[2],x[0],x[1]
        new=deepcopy(game.field)
        count=0
        if self.status != 'FROZEN':
            for i in range(len(game.field)):
                if game.field[i][self.column-1][0] in '|[' and game.field[i][self.column-1][2] in '|]':
                    if count==0:
                        new[i][self.column-1], new[i+1][self.column-1], new[i+2][self.column-1] = game.field[i+2][self.column-1], game.field[i][self.column-1], game.field[i+1][self.column-1]
                    count+=1
        game.field=new
        return new

    def freeze_faller(self, game:GameState) -> [[str]]:
        # Freezes faller
        new=deepcopy(game.field)
        if self.status == 'LANDED':
            self.status = 'FROZEN'
            for i in range(len(game.field)):
                if game.field[i][self.column-1][0] == '|' and game.field[i][self.column-1][2] == '|':
                    new[i][self.column-1]= game.field[i][self.column-1][1]
        game.field=new
        game.faller_present=False
        return new


    def move_faller_right(self, game: GameState) -> [[str]]:
        # Moves faller right
        new=deepcopy(game.field)
        move_right = False
        for i in range(len(game.field)):
            if game.field[i][self.column-1][0] in '[|' and game.field[i][self.column-1][2] in '|]':
                try:
                    if self.column in range(len(game.field[i])) and game.field[i][self.column] == ' ':
                        move_right = True
                    else:
                        move_right = False
                        return game.field
                except IndexError:
                    move_right = False
                    return game.field
        if move_right == True:
            count=0
            for i in range(len(game.field)):
                if game.field[i][self.column-1][0] in '[|' and game.field[i][self.column-1][2] in '|]':
                    count+=1
                    if count == 3:
                        try:
                            if game.field[i+1][self.column] == ' ':
                                new[i][self.column] = f'[{game.field[i][self.column-1][1]}]'
                                new[i][self.column-1] = game.field[i][self.column]
                                new[i-1][self.column] = f'[{game.field[i-1][self.column-1][1]}]'
                                new[i-1][self.column-1] = game.field[i-1][self.column]
                                new[i-2][self.column] = f'[{game.field[i-2][self.column-1][1]}]'
                                new[i-2][self.column-1] = game.field[i-2][self.column]
                                self.status = "FALLING"
                                self.column=self.column+1
                            else:
                                new[i][self.column] = game.field[i][self.column-1]
                                new[i][self.column-1] = game.field[i][self.column]
                                new[i-1][self.column] = game.field[i-1][self.column-1]
                                new[i-1][self.column-1] = game.field[i-1][self.column]
                                new[i-2][self.column] = game.field[i-2][self.column-1]
                                new[i-2][self.column-1] = game.field[i-2][self.column]
                                game.field=new
                                self.column=self.column+1
                                new=self.land_faller(game)
                        except IndexError:
                                new[i][self.column] = game.field[i][self.column-1]
                                new[i][self.column-1] = game.field[i][self.column]
                                new[i-1][self.column] = game.field[i-1][self.column-1]
                                new[i-1][self.column-1] = game.field[i-1][self.column]
                                new[i-2][self.column] = game.field[i-2][self.column-1]
                                new[i-2][self.column-1] = game.field[i-2][self.column]
                                self.column=self.column+1
                        finally:
                            game.field=new
                            return new


    def move_faller_left(self, game: GameState) -> [[str]]:
        # Moves faller left
        new=deepcopy(game.field)
        move_left = False
        for i in range(len(game.field)):
            if game.field[i][self.column-1][0] in '[|' and game.field[i][self.column-1][2] in '|]':
                try:
                    if (self.column-2) in range(len(game.field[i])) and game.field[i][self.column-2] == ' ':
                        move_left = True
                    else:
                        move_left = False
                        return game.field
                except IndexError:
                    move_left = False
                    return game.field
        if move_left == True:
            count=0
            for i in range(len(game.field)):
                if game.field[i][self.column-1][0] in '[|' and game.field[i][self.column-1][2] in '|]':
                    count+=1
                    if count == 3:
                        try:
                            if game.field[i+1][self.column-2] == ' ':
                                new[i][self.column-2] = f'[{game.field[i][self.column-1][1]}]'
                                new[i][self.column-1] = game.field[i][self.column-2]
                                new[i-1][self.column-2] = f'[{game.field[i-1][self.column-1][1]}]'
                                new[i-1][self.column-1] = game.field[i-1][self.column-2]
                                new[i-2][self.column-2] = f'[{game.field[i-2][self.column-1][1]}]'
                                new[i-2][self.column-1] = game.field[i-2][self.column-2]
                                self.status = "FALLING"
                                self.column=self.column-1
                            else:
                                new[i][self.column-2] = game.field[i][self.column-1]
                                new[i][self.column-1] = game.field[i][self.column-2]
                                new[i-1][self.column-2] = game.field[i-1][self.column-1]
                                new[i-1][self.column-1] = game.field[i-1][self.column-2]
                                new[i-2][self.column-2] = game.field[i-2][self.column-1]
                                new[i-2][self.column-1] = game.field[i-2][self.column-2]
                                game.field=new
                                self.column=self.column-1
                                new=self.land_faller(game)
                        except IndexError:
                                new[i][self.column-2] = game.field[i][self.column-1]
                                new[i][self.column-1] = game.field[i][self.column-2]
                                new[i-1][self.column-2] = game.field[i-1][self.column-1]
                                new[i-1][self.column-1] = game.field[i-1][self.column-2]
                                new[i-2][self.column-2] = game.field[i-2][self.column-1]
                                new[i-2][self.column-1] = game.field[i-2][self.column-2]
                                self.column=self.column-1
                        finally:
                            game.field=new
                            return new
