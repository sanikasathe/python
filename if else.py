# input the color of the traffic light
light = input("Enter the color of the traffic light: ")

# Check if the input color is 'red'
if light == 'red':
    # If the light is red, the car should stop
    print("Stop")

# Check if the input color is 'green'
elif light == 'green':
    # If the light is green, the car can go
    print("Go")

# Check if the input color is 'yellow'
elif light == 'yellow':
    # If the light is yellow, the car should wait a while
    print("Wait a while")

# If the input is any other color (invalid color)
else:
    # The traffic light is broken
    print("Light is broken")
