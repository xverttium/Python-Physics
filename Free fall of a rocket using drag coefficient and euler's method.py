#Importing libraries
import matplotlib   #Plotting library (not yet used)

#Defining parameters
g = 9.81    #Graitational Acceleration

dt = 0.01   #Time step

d = 0.75 #Drag Coefficient - "A typical value for the drag coefficient of a model rocket is .75, based on the cross-sectional area of the rocket", NASA Glenn Research Center's Beginners Guide to Aeronautics

velocities = []    #Recording the speed of the object after every time step

heights = []    #Recording its position after every time step

time = []     #Recording every time step xD

T = float(input('Simulation time, in seconds: '))

number_of_time_steps = int(T/dt)

m = float(input("Object's mass, in kg: "))

v0 = float(input('Initial speed, in m/s: '))

y0 = float(input('Initial height, in m: '))

#Defining the function to obtain speed and position over time
def new_speed_and_new_height(v0, g, dt):
    vf = v0
    yf = y0
    a = g
    for c in range (0, number_of_time_steps+1):
        time.append(c*dt)
        if abs(vf) < 0.5:
            a = g-((d*vf)/m)
        else:
            a = g-((d*vf*vf)/m)
        vf -= a*dt  #accumulative subtraction for every velocity absolute value increase
        velocities.append(vf)
        yf += vf*dt
        heights.append(yf)
        if yf <= 0: break   #Stops simulation if the body hits the ground
    return vf, yf   #Returns final speed and position values
final_speed, final_height = new_speed_and_new_height(v0, g, dt)
if final_height <= 0:
    print(f"Approximate speed of the object right before hitting the ground: {final_speed:.2f}m/s")
    print(f'Final height: 0 (ground level)')
else:
    print(f'Final speed: {final_speed:.2f}m/s')
    print(f'Final height: {final_height:.2f}m')
#These values are only approximations, based on an idealized and simplified free fall.
#Plotting is yet to be done










