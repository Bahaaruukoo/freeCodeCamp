import copy
import random

class Hat:    
    def __init__(self, **kwargs):
        self.contents = []
        for col, val in kwargs.items():            
            for i in range(int(val)):
                self.contents.append(col)
        self.contents_copy = copy.deepcopy(self.contents)
    def draw(self, amount):
        self.contents = copy.deepcopy(self.contents_copy)
        result = []        
        if amount > len(self.contents):
            result = self.contents
        else:
            for i in range(amount):
                drawnBall = random.choice(self.contents)                
                result.append(drawnBall)
                self.contents.remove(drawnBall)
        return result

def experiment( hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for game in range(num_experiments):
        drawing = {}
        flag = False
        balls_drawn = hat.draw(num_balls_drawn)
        for item in balls_drawn:
            if item in drawing:
                drawing[item] = drawing[item] + 1
            else:
                drawing[item] = 1

        for key in expected_balls:     
            if( key in drawing and drawing[key] >= expected_balls[key]):
                flag = True              
            else:
                flag = False
                break            
        if flag:               
            M += 1                          
    return M/num_experiments
