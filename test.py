#SkyTrajectory by Sadiq Ali

import math
import matplotlib.pyplot as plt

def simulate_flight(velocity, angle):
    # Convert the angle from degrees to radians
    angle = math.radians(angle)
    
    # Calculate the horizontal and vertical velocity components
    vx = velocity * math.cos(angle)
    vy = velocity * math.sin(angle)
    
    # Set the gravitational acceleration
    g = 9.8
    
    # Calculate the maximum height
    max_height = (vy**2) / (2*g)
    
    # Calculate the time of flight
    tf = 2 * vy / g
    
    # Calculate the horizontal range
    h_range = vx * tf
    
    # Generate time values for the simulation
    t = [i for i in range(0, int(tf) + 1)]
    
    # Calculate the height values for each time step
    h = [max_height - g * i**2 / 2 for i in t]
    
    # Calculate the x values for each time step
    x = [vx * i for i in t]
    
    return t, h, x, max_height, tf, h_range

# Get the initial velocity and launch angle from the user
velocity = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the launch angle (degrees): "))

# Call the simulate_flight function and get the results
t, h, x, max_height, tf, h_range = simulate_flight(velocity, angle)

# Plot the results
plt.plot(x, h)
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical distance (m)")
plt.title("Projectile Motion Simulation")
plt.show()

# Print the results
print("Maximum height:", max_height, "meters")
print("Time of flight:", tf, "seconds")
print("Horizontal range:", h_range, "meters")