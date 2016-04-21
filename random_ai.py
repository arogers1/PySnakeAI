from snake import SnakeGame
import random

sg = SnakeGame(human_player=False)
#sg.run()

while True:
    sg.clock.tick(10)
    print(sg.xs, sg.ys)
    sg.dirs = random.randint(0, 3)  # 0=Down, 1=Right, 2=Up, 3=Left
    sg.next_step()