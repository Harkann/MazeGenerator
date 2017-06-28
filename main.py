#! /bin/env python3
import numpy as np

grid_size = (10,10)


def display_case(shape) :
    return ([[ 0, shape[0], 0],
            [ shape[1], " ", shape[2]],
            [ 0, shape[3], 0]])
    

def display_line(shape_line) :
    cases = [[],[],[]]
    for shape in shape_line:
        cases[0] += display_case(shape)[0]
        cases[1] += display_case(shape)[1]
        cases[2] += display_case(shape)[2]
    return cases

def display_grid(shape_grid) :
    for shape_line in shape_grid :
        for i in range(3):
            line = ""
            for square in display_line(shape_line)[i]:
                line+=str(square)
            print(line)
    return 



#print(display_grid([[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]]))
class MazeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Maze():
    def __init__(self,size=None,entrypoint=None,debug=False):

        if entrypoint not in ["North","South","East","West",None]:
            raise MazeError("Wrong entrypoint, must be 'North','South','East','West or None")
        else :    
            self.entrypoint = entrypoint
        if size == None :
            raise MazeError("Size must be specified")
        else :
            self.n_lines,self.n_columns = size
            self.grid=[]
            for i in range(self.n_lines):
                self.grid.append([])
                for j in range(self.n_columns):
                    self.grid[i].append("")


    def display(self):
        print(np.array(self.grid))
        print("plop")


    def create_maze(self):
        if self.entrypoint == None:
            for i in range(self.n_lines):
                self.grid[i][0] = 0
                self.grid[i][-1] = 0
            for i in range(self.n_columns):
                #print(self.grid[-1])
                self.grid[0][i] = 0
                self.grid[-1][i] = 0
                pass
        self.display()





maze1 = Maze(size=(10,10),debug=True)
maze1.create_maze()