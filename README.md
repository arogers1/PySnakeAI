# PySnakeAI

This is adapated from the Snake Game on pygame.org

http://pygame.org/project-Snake+in+35+lines-818-.html

It has been slightly modified to allow an AI interface in the future.

Forked from rwdavis.

##UPDATE 4-20-16:
Now has an AI interface. The AI class simply needs to have a get_input() method and to accept the SnakeGame object as a constructor parameter.

dirs is the next move of the snake. 0=Down, 1=Right, 2=Up, 3=Left

sg.xs and sg.ys are the current positions of the snake
sg.applepos is the position of the apple
