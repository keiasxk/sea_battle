import random 

class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alve = ships
        self.grid = []
        for i in range(size):
            self.grid.append([None] * size) 

    def display(self, show_ships = False):
        letters = '    A B C D E F G H I J'
        print(letters)
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None or (cell is not None and not show_ships):
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10:
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)

class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15

        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    def place_ships_randomly(self, field, num_ships):
        for i in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display(show_ships=True)

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
        self.player_field.display(show_ships=True)

        while 1:
            while 1:
            # while x not in "ABCDEFGHIJ" and y not in range(0,10):
                x = input('Введите координату x: ')
                y = input('Введите координату y: ')
                if x in "ABCDEFGHIJ" and int(y) in range(0,10):
                    break
                print('Неправильный ввод. Повторите попытку.')
            self.player_turn(x,int(y))
            if self.computer_field.ships_alve == 0:
                print('Вы победили! Все коробли комьютера потопленны.')
                break
            self.computer_turn()
            if self.player_field.ships_alve == 0:
                print('Вы проиграли! Все ваши коробли потопленны.')
                break

    def player_turn(self, x, y):
        x = "ABCDEFGHIJ".index(x)
        y -= 1 
        if self.computer_field.grid[y][x] == 'S':
            print('Вы попали!')
            self.computer_field.grid[y][x] = 'X'
            self.computer_field.ships_alve -= 1
        else:
            print('Промах!')

    def computer_turn(self):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if self.computer_field.grid[y][x] == 'S':
            print('Компьюетр попал!')
            self.computer_field.grid[y][x] = 'X'
            self.computer_field.ships_alve -= 1
        else:
            print('Компьютер промахнулся!')

game = BattleshipGame()
game.play()
