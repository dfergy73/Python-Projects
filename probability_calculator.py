'''This program determines the probability of drawing certain balls
   randomly from a hat.'''

import copy
import random

class Hat:
    # You don't know how many balls you'll get, or of which color.
    def __init__(self, **kwargs):
        self.contents = []
        # Store the numbers of each color ball as strings of the color
        # in a list.
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    # Method to draw balls from the hat.
    def draw(self, number):
        pulled = []
        # If there are not enough or just enough balls, return all the balls.
        if number >= len(self.contents):
            for i in range(len(self.contents)):
                pulled.append(self.contents.pop(0))
        # If there are more than enough balls, randomly select the
        # requested number of balls.
        else:
            for i in range(number):
                pulled.append(self.contents.pop(random.randrange(len(self.contents))))
        return pulled


# Function to determine the probability of pulling certain numbers of
# certain colored balls from a Hat object by using a specified number of
# experiments.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_successes = 0
    # Run the experiment the specified number of times.
    for i in range (num_experiments):
        results = []
        successes = 0
        # Create deep copy of the Hat object so you can keep using the
        # original.
        hat_copy = copy.deepcopy(hat)
    
        # Draw the number of balls requested.
        pulled_balls = hat_copy.draw(num_balls_drawn)

        # Check to see if you got the number of balls expected for each
        # color. Append True to a list if successful.
        for key, value in expected_balls.items():
            if value <= pulled_balls.count(key):
                results.append(True)
            else:
                results.append(False)

        # If you got the minimum number specified of every color of ball,
        # that is a successful experiment.
        if all(results):
            successes += 1
        total_successes += successes
    
    # Find the probability by dividing the number of successes by the
    # number of experiments.
    return total_successes / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)