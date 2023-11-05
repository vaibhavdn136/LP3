import numpy as np

import matplotlib.pyplot as plt



def f(x):
    return (x+3)**2


def df(x):
    return 2*(x+3)


def gradient_descent(intial_x,learning_rate,num_iteration):
    x=intial_x
    x_history=[x]
    
    for i in range(num_iteration):
        gradient=df(x)
        x=x-learning_rate*gradient
        x_history.append(x)
    return x,x_history



intial_x=2
learning_rate=0.1
num_iteration=100

x,x_history = gradient_descent(intial_x,learning_rate,num_iteration)

print("Local Minima : {:.2f}".format(x))




#create range of x value to plot

x_vals = np.linspace(-10,4,100)

#The starting value (-10 in this case).
#The ending value (4 in this case).
#The number of values you want to generate (100 in this case).

# Plot the function f(x)
plt.plot(x_vals,f(x_vals))
plt.plot(x_history,f(np.array(x_history)),'rx')
#'rx' specifies that the data points should be plotted as red (r) 'x' markers.


plt.xlabel('X')
plt.ylabel('f(x)')
plt.title("Gradient Descent")
plt.show







