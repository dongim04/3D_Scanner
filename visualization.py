import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv('scan_data.csv', header=None, names=['PanAngle', 'TiltAngle', 'Distance'])

df['PanAngleRad'] = df['PanAngle'].apply(math.radians)
df['TiltAngleRad'] = df['TiltAngle'].apply(math.radians)

df['X'] = df['Distance'] * df['TiltAngleRad'].apply(math.cos) * df['PanAngleRad'].apply(math.cos)
df['Y'] = df['Distance'] * df['TiltAngleRad'].apply(math.cos) * df['PanAngleRad'].apply(math.sin)
df['Z'] = df['Distance'] * df['TiltAngleRad'].apply(math.sin)

plt.figure(figsize=(8, 8))
plt.scatter(df['X'], df['Z'], c='r', marker='o')
plt.xlabel('X (cm)')
plt.ylabel('Z (cm)')
plt.title('2D Side View Projection of Scanned Object (X-Z Plane)')
# plt.grid(True)
# plt.axis('equal')

plt.show()
