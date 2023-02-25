from sys import stdout
from time import sleep
from itertools import cycle


def show_terminal_animation(stop):
    """
    This function is designed to create and animate a simple loading animation.

    :param stop: a function that returns a boolean value indicating whether the animation should stop
    """
    # Animate the loading screen by cycling through a sequence of characters
    for c in cycle(['|', '/', '-', '\\']):
        if stop():
            # If the animation is done, break out of the loop
            break
        # Overwrite the terminal output with the current character
        stdout.write('\rworking, please wait... ' + c)
        stdout.flush()
        sleep(0.1)
    # When the animation is finished, print "Done!"
    stdout.write('\rDone!\r\n')
    stdout.flush()
