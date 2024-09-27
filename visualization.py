import pandas as pd
import matplotlib.pyplot as plt
import math

# Load the CSV file with pan, tilt, and distance data
df = pd.read_csv('C:/Users/dlee3/OneDrive - Olin College of Engineering/PIE/3DScanner/3D_Scanner/scan_data.csv', header=None, names=['PanAngle', 'TiltAngle', 'Distance'])

# Convert angles from degrees to radians
df['PanAngleRad'] = df['PanAngle'].apply(math.radians)
df['TiltAngleRad'] = df['TiltAngle'].apply(math.radians)

# Define a distance threshold (adjust as necessary)
min_distance = 20  # Minimum valid distance (e.g., avoid noise too close to sensor)
max_distance = 150  # Maximum valid distance (e.g., avoid far away background points)

# Filter the DataFrame to include only valid distances
df_filtered = df[(df['Distance'] >= min_distance) & (df['Distance'] <= max_distance)]

# Compute Cartesian coordinates for 2D side view (X-Z projection)
df_filtered['X'] = df_filtered['Distance'] * df_filtered['TiltAngleRad'].apply(math.cos) * df_filtered['PanAngleRad'].apply(math.cos)
df_filtered['Y'] = df_filtered['Distance'] * df_filtered['TiltAngleRad'].apply(math.cos) * df_filtered['PanAngleRad'].apply(math.sin)
df_filtered['Z'] = df_filtered['Distance'] * df_filtered['TiltAngleRad'].apply(math.sin)

# Plotting the 2D side view projection (X-Z plane)
plt.figure(figsize=(8, 8))
plt.scatter(df_filtered['X'], df_filtered['Z'], c='r', marker='o')

# Label the axes
plt.xlabel('X (cm)')
plt.ylabel('Z (cm)')
plt.title('2D Side View Projection of Scanned Object (X-Z Plane)')

# Enable grid and equal axis scaling
plt.grid(True)
plt.axis('equal')  # Ensure equal scaling of both axes for a more accurate shape

plt.show()
