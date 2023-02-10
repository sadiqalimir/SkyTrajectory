# SkyTrajectory <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/sadiqalimir/Orbitron-">

## Overview
SkyTrajectort, this project aims to simulate the flight of an aircraft, rocket, or satellite based on user input. The simulation calculates the motion of the object in two dimensions (horizontal and vertical) and displays the results graphically using the matplotlib library. The code takes the initial velocity and launch angle as inputs and calculates various parameters such as the maximum height, time of flight, and horizontal range of the flight.

## Requirements
The following libraries are required for this project:
```
`math`
`matplotlib`
```

## Functions
The following functions are defined in the code:
```
`simulate_flight(velocity, angle)`
```
This function takes two inputs, the initial velocity and launch angle. It then calculates the horizontal and vertical velocity components, sets the gravitational acceleration, and calculates the maximum height, time of flight, and horizontal range of the flight. The function generates time values for the simulation and calculates the height and x values for each time step. The function returns the following values:
```
`time`
``` 
A list of time values for the simulation.

height: A list of height values for each time step. <br>
```
`x`
```
A list of horizontal distance values for each time step. <br>
```
`max_height`
```
The maximum height reached during the flight.<br>
```
`time_of_flight`
``` 
The total time of flight.<br>
```
`horizontal_range`
```
The horizontal range of the flight.<br>
```
`plot(x, h)`
```
This function takes the x and h values (horizontal and vertical distances) and plots the results using matplotlib.

## Inputs
The user is prompted to enter the following inputs:
`velocity`: The initial velocity in meters per second (m/s).
`angle`: The launch angle in degrees.

## Outputs
The code generates the following outputs:
A graphical representation of the flight simulation, showing the horizontal and vertical distances over time.
The maximum height, time of flight, and horizontal range are displayed in the console.

## Usage
To use the code, simply run the code in a Python environment and follow the prompts to enter the initial velocity and launch angle. The code will then generate a graphical representation of the flight simulation and display the maximum height, time of flight, and horizontal range in the console.

## Contributing
If you would like to contribute to the development of the SkyTrajectory, please fork the repository and submit a pull request with your changes.

## License
The "SkyTrajectory" is open-source software and is released under the MIT License.
