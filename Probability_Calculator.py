import copy
import random


class Hat:
    def __init__(self, **kwargs):
        """Initialize hat with variable number of colored balls"""
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)
    
    def draw(self, num_balls):
        """Draw random balls from the hat without replacement"""
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents = []
            return drawn_balls
        
        drawn_balls = []
        for i in range(num_balls):
            random_index = random.randrange(len(self.contents))
            drawn_ball = self.contents.pop(random_index)
            drawn_balls.append(drawn_ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform experiments to calculate probability of drawing expected balls
    
    Args:
        hat: A Hat object containing balls
        expected_balls: Dictionary of balls we expect to draw (e.g., {'red': 2, 'blue': 1})
        num_balls_drawn: Number of balls to draw in each experiment
        num_experiments: Number of experiments to perform
    
    Returns:
        Probability (between 0 and 1) of drawing at least the expected balls
    """
    successful_experiments = 0
    
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_counts.get(color, 0) < expected_count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    probability = successful_experiments / num_experiments
    return probability


if __name__ == "__main__":
    hat1 = Hat(yellow=3, blue=2, green=6)
    print("Hat 1 contents:", hat1.contents)
    
    hat2 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    drawn = hat2.draw(3)
    print("Drawn balls:", drawn)
    print("Remaining in hat:", len(hat2.contents))
    
    hat3 = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat3,
        expected_balls={'red': 2, 'green': 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print(f"Probability: {probability}")
    
    hat4 = Hat(blue=4, red=2, green=6)
    probability2 = experiment(
        hat=hat4,
        expected_balls={'blue': 2, 'red': 1},
        num_balls_drawn=4,
        num_experiments=3000
    )
    print(f"Probability 2: {probability2}")