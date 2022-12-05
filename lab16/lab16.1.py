import math
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    
    # x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    
    fig.set_facecolor('green')
    ax.set(facecolor='blue')
    
    x_arr = np.array(range(-10,10))
    y_arr = [math.sin(x * 0.4) + 0.1 * x for x in x_arr]
    print(x_arr)
    print(y_arr)
    
    ax.plot(x_arr, y_arr ,color='red' ,label='sin(0.4x) + 0.1x',linestyle='--')
    
    
    ax.set_xlim(-10,10)
    ax.set_ylim(-20,20)
    
    ax.legend(loc='lower right')
    
    fig.savefig('x.png')
    plt.show()
    
    
main()