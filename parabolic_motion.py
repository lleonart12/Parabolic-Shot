#
# Example parabolic motion
#

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt
 
#
# FUNCTION DRAW A TRAJECTORY FOR PARABOLIC MOTION
# Input: velocity and angle 
#
def draw_trajectory(u, theta):
    #convert angle in degrees to rad
    theta = np.radians(theta)
    #gravity acceleration in m/s2
    g = 9.8
    # Time of flight
    t_flight = ((u*np.sin(theta)+(((u**2)*(np.sin(theta)**2)+2*g*h)**(1/2)))/g)
    print(t_flight)
    # find time intervals
    intervals = np.arange(0, t_flight, 0.001)
    # create an empty list of x and y coordinates
    x = []
    y = []
    #Do a loop over time calculating the coordinates
    for t in intervals:
        x.append(u*np.cos(theta)*t)
        y.append(h+u*np.sin(theta)*t - (0.5*g*t**2))
    #Plot the results
    plt.plot(x, y)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile motion')

#--------------------------------------------------------------------------------
# Main Program: give specific values and call to the function draw_trajectory
#--------------------------------------------------------------------------------

print("Parabolic motion of a projectile\n")

#Ask the user for angle
print("Enter desired launch angle in degrees (recommended 45 degrees):")
theta=float(input())
print("Enter the initial heigth from where you launch the projectile")
h=float(input())
# list of three different initial velocity in m/s
u_list = [20, 40, 60]

for u in u_list:
        draw_trajectory(u, theta)
        
# Add a legend and show the graph
plt.legend(['20', '40', '60'])
plt.show()
