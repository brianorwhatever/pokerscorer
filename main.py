from Game import Game

if __name__ == '__main__':
    game = Game(player_count=4)
    print('\n')
    print('Hands:')
    for hand in game.hands:
        print(hand)
    print('\n')
    print('Winners:')
    winners = game.compare_hands()
    for winner in winners:
        print('{winner} wins with {val}'.format(winner=winner, val=winner.hand_type()))