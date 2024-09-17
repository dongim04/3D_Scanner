import serial
import math
import matplotlib.pyplot as plt

# Initialize serial connection (adjust 'COM3' to your serial port)
ser = serial.Serial('COM3', 9600)

# Lists to store data
pan_angles = []
distances = []
x_coords = []
y_coords = []

# Function to parse the serial data
def parse_data(line):
    data = line.decode().strip().split(", ")
    pan = int(data[0].split(": ")[1])
    distance = float(data[2].split(": ")[1])
    return pan, distance

# Read data from Arduino
while len(pan_angles) < 100:  # Adjust number of points to collect
    if ser.in_waiting > 0:
        line = ser.readline()
        try:
            pan_angle, distance = parse_data(line)
            pan_angles.append(pan_angle)
            distances.append(distance)
        except:
            pass

# Convert polar coordinates (angle, distance) to Cartesian (x, y)
for pan_angle, distance in zip(pan_angles, distances):
    # Convert pan_angle from degrees to radians
    pan_angle_rad = math.radians(pan_angle)
    # Polar to Cartesian conversion
    x = distance * math.cos(pan_angle_rad)
    y = distance * math.sin(pan_angle_rad)
    x_coords.append(x)
    y_coords.append(y)

# Plot the 2D top-down view
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords)
plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')
plt.title('2D Top-Down View of Scanned Object')
plt.grid(True)
plt.axis('equal')  # To ensure the plot is proportional
plt.show()