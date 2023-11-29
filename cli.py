from logic import Game, Human, Bot

def play_game():
    game = Game()
    human_player = Human()
    bot_player = Bot()

    while not game.leaveLoop:
        if game.turnCounter % 2 == 0:
            game.print_board()
            number_picked = human_player.make_move()
            if 1 <= number_picked <= 9:
                game.modify_array(number_picked)
                game.other_player()
            else:
                print("Invalid input. Please try again.")
            game.turnCounter += 1
        else:
            other_player_choice = bot_player.make_move()
            print("\nOther Player's Choice:", other_player_choice)
            game.modify_array(other_player_choice)
            game.other_player()
            game.turnCounter += 1

        winner = game.get_winner()
        if winner != "N":
            game.print_board()
            print(f"{winner} won!")
            break
        elif game.turnCounter == 9:
            game.print_board()
            print("It's a draw!")
            break

    # Record the outcome of the game
    winner = game.get_winner()
    player1 = "Human" if winner == "X" else "Bot"
    player2 = "Bot" if winner == "X" else "Human"
    moves = game.turnCounter

    game.log_game(winner, player1, player2, moves)

if __name__ == '__main__':
    play_game()