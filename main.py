from game import Game


if __name__ == '__main__':
    game = Game()
    game.show_start_screen()
    while True:
        game.run()
        game.show_go_screen()
