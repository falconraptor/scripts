import json


def ignore_exception(IgnoreException=Exception, DefaultVal=None):
    """ Decorator for ignoring exception from a function
    e.g.   @ignore_exception(DivideByZero)
    e.g.2. ignore_exception(DivideByZero)(Divide)(2/0)
    """

    def dec(function):
        def _dec(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except IgnoreException:
                return DefaultVal

        return _dec

    return dec


players = {}
while True:
    print('1) Display All')
    print('2) Select Player')
    print('3) Add Player')
    print('4) Remove Player')
    print('5) Save File')
    print('6) Load File')
    print('7) Quit')
    command = ignore_exception(ValueError)(int)(input())
    print()
    if command == 1:
        for player_name, owes in players.items():
            for owe in owes:
                to_player = owe['to']
                items = owe['owes']
                for item in items:
                    print(player_name + ' owes ' + str(items[item]) + ' ' + item + ' to ' + to_player)
    elif command == 2:
        print('Which player do you want to select? ')
        for i, player in enumerate(players):
            print(str(i + 1) + ') ' + player, '')
        player_index = input()
        if player_index in players:
            player = players[player_index]
            if player:
                pass
            else:
                print('That player is not found!')
        else:
            print('That player is not found!')
    elif command == 3:
        player = input('Player Username: ')
        players[player] = []
    elif command == 4:
        player = input('Player Username: ')
        del players[player]
    elif command == 5:
        file_name = input('File to save: ')
        with open(file_name, 'w') as file:
            json.dump(players, file, indent=4, sort_keys=True)
    elif command == 6:
        file_name = input('File to load: ')
        with open(file_name) as file:
            players = json.load(file)
    elif command == 7:
        quit()
    print()
