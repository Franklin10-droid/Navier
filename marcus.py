
import numpy as np

caso1 = np.array([
[0.50, 0.059, 169.18, 42.29 ],
[0.51, 0.063, 158.42, 41.20 ],
[0.52, 0.068, 148.64, 40.19 ],
[0.53, 0.073, 139.70, 39.24 ],
[0.54, 0.078, 131.55, 38.36 ],
[0.55, 0.084, 124.10, 37.53 ],
[0.56, 0.089, 117.25, 36.77 ],
[0.57, 0.095, 110.96, 36.05 ],
[0.58, 0.102, 105.19, 35.38 ],
[0.59, 0.108, 99.86, 34.76 ],
[0.60, 0.115, 94.94, 34.18 ],
[0.61, 0.122, 90.40, 33.64 ],
[0.62, 0.129, 86.20, 33.13 ],
[0.63, 0.136, 82.30, 32.66 ],
[0.64, 0.144, 78.68, 32.23 ],
[0.65, 0.151, 75.32, 31.82 ],
[0.66, 0.159, 72.19, 31.44 ],
[0.67, 0.168, 69.27, 31.09 ],
[0.68, 0.176, 66.54, 30.99 ],
[0.69, 0.185, 63.99, 30.46 ],
[0.70, 0.194, 61.60, 30.18 ],
[0.71, 0.203, 59.37, 29.93 ],
[0.72, 0.212, 57.27, 29.69 ],
[0.73, 0.221, 55.29, 29.47 ],
[0.74, 0.231, 53.44, 29.26 ],
[0.75, 0.240, 51.69, 29.07 ],
[0.76, 0.250, 50.04, 28.90 ],
[0.77, 0.260, 48.48, 28.74 ],
[0.78, 0.270, 47.01, 28.60 ],
[0.79, 0.280, 45.61, 28.46 ],
[0.80, 0.290, 44.29, 28.34 ],
[0.81, 0.301, 43.03, 28.23 ],
[0.82, 0.311, 41.84, 28.13 ],
[0.83, 0.322, 40.70, 28.04 ],
[0.84, 0.332, 39.62, 27.96 ],
[0.85, 0.343, 38.59, 27.88 ],
[0.86, 0.354, 37.61, 27.81 ],
[0.87, 0.364, 36.67, 27.75 ],
[0.88, 0.375, 35.77, 27.70 ],
[0.89, 0.385, 34.91, 27.65 ],
[0.90, 0.396, 34.09, 27.61 ],
[0.91, 0.407, 33.30, 27.57 ],
[0.92, 0.417, 32.54, 27.54 ],
[0.93, 0.428, 31.81, 27.51 ],
[0.94, 0.438, 31.11, 27.49 ],
[0.95, 0.449, 30.44, 27.47 ],
[0.96, 0.459, 29.79, 27.45 ],
[0.97, 0.469, 29.17, 27.44 ],
[0.98, 0.480, 28.57, 27.43 ],
[0.99, 0.490, 27.99, 27.43 ],
[1.00, 0.500, 27.43, 27.43 ],
[1.00, 0.500, 27.43, 27.43],
[1.01, 0.510, 26.89, 27.43],
[1.02, 0.520, 26.37, 27.43],
[1.03, 0.529, 25.87, 27.44],
[1.04, 0.539, 25.38, 27.45],
[1.05, 0.549, 24.91, 27.47],
[1.06, 0.558, 24.46, 27.48],
[1.07, 0.567, 24.02, 27.50],
[1.08, 0.576, 23.60, 27.52],
[1.09, 0.585, 23.19, 27.55],
[1.10, 0.594, 22.79, 27.57],
[1.11, 0.603, 22.41, 27.61],
[1.12, 0.611, 22.03, 27.64],
[1.13, 0.620, 21.67, 27.67],
[1.14, 0.628, 21.32, 27.71],
[1.15, 0.636, 20.99, 27.76],
[1.16, 0.644, 20.66, 27.80],
[1.17, 0.652, 20.34, 27.85],
[1.18, 0.660, 20.04, 27.90],
[1.19, 0.667, 19.74, 27.95],
[1.20, 0.675, 19.45, 28.01],
[1.21, 0.682, 19.17, 28.07],
[1.22, 0.689, 18.90, 28.13],
[1.23, 0.696, 18.64, 28.20],
[1.24, 0.703, 18.39, 28.27],
[1.25, 0.709, 18.14, 28.34],
[1.26, 0.716, 17.90, 28.42],
[1.27, 0.722, 17.67, 28.50],
[1.28, 0.729, 17.44, 28.58],
[1.29, 0.735, 17.23, 28.67],
[1.30, 0.741, 17.01, 28.76],
[1.31, 0.746, 16.81, 28.85],
[1.32, 0.752, 16.61, 28.94],
[1.33, 0.758, 16.42, 29.04],
[1.34, 0.763, 16.23, 29.14],
[1.35, 0.769, 16.05, 29.25],
[1.36, 0.774, 15.87, 29.36],
[1.37, 0.779, 15.70, 29.47],
[1.38, 0.784, 15.53, 29.58],
[1.39, 0.789, 15.37, 29.70],
[1.40, 0.793, 15.21, 29.82],
[1.41, 0.798, 15.06, 29.95],
[1.42, 0.803, 14.91, 30.07],
[1.43, 0.807, 14.77, 30.20],
[1.44, 0.811, 14.63, 30.34],
[1.45, 0.815, 14.49, 30.47],
[1.46, 0.820, 14.36, 30.61],
[1.47, 0.824, 14.23, 30.76],
[1.48, 0.827, 14.11, 30.90],
[1.49, 0.831, 13.99, 31.05],
[1.50, 0.835, 13.87, 31.21],
[1.50, 0.835, 13.87, 31.21],
[1.51, 0.839, 13.75, 31.36],
[1.52, 0.842, 13.64, 31.52],
[1.53, 0.846, 13.53, 31.68],
[1.54, 0.849, 13.43, 31.85],
[1.55, 0.852, 13.32, 32.01],
[1.56, 0.855, 13.22, 32.18],
[1.57, 0.859, 13.13, 32.36],
[1.58, 0.862, 13.03, 32.53],
[1.59, 0.865, 12.94, 32.71],
[1.60, 0.868, 12.85, 32.80],
[1.61, 0.870, 12.76, 33.08],
[1.62, 0.873, 12.68, 33.27],
[1.63, 0.876, 12.59, 33.46],
[1.64, 0.878, 12.51, 33.65],
[1.65, 0.881, 12.43, 33.85],
[1.66, 0.884, 12.35, 34.04],
[1.67, 0.886, 12.28, 34.24],
[1.68, 0.888, 12.21, 34.45],
[1.69, 0.891, 12.13, 34.65],
[1.70, 0.893, 12.06, 34.87],
[1.71, 0.895, 12.00, 35.08],
[1.72, 0.897, 11.93, 35.29],
[1.73, 0.899, 11.86, 35.51],
[1.74, 0.902, 11.80, 35.73],
[1.75, 0.904, 11.74, 35.95],
[1.76, 0.906, 11.68, 36.17],
[1.77, 0.907, 11.62, 36.40],
[1.78, 0.909, 11.56, 36.63],
[1.79, 0.911, 11.51, 36.86],
[1.80, 0.913, 11.45, 37.10],
[1.81, 0.915, 11.40, 37.33],
[1.82, 0.916, 11.34, 37.58],
[1.83, 0.918, 11.29, 37.82],
[1.84, 0.920, 11.24, 38.06],
[1.85, 0.921, 11.19, 38.31],
[1.86, 0.923, 11.15, 38.56],
[1.87, 0.924, 11.10, 38.81],
[1.88, 0.926, 11.05, 39.07],
[1.89, 0.927, 11.01, 39.32],
[1.90, 0.929, 10.96, 39.58],
[1.91, 0.930, 10.92, 39.84],
[1.92, 0.931, 10.88, 40.10],
[1.93, 0.933, 10.84, 40.37],
[1.94, 0.934, 10.80, 40.63],
[1.95, 0.935, 10.76, 40.91],
[1.96, 0.936, 10.72, 41.18],
[1.97, 0.938, 10.68, 41.45],
[1.98, 0.939, 10.64, 41.73],
[1.99, 0.940, 10.60, 42.01],
[2.00, 0.941, 10.57, 42.29],])



caso2 = np.array([	
[0.50, 0.135, 140.93, 59.20, 45.13],
[0.51, 0.145, 132.95, 55.31, 44.11],
[0.52, 0.154, 125.68, 51.77, 43.22],
[0.53, 0.165, 119.03, 48.56, 42.38],
[0.54, 0.175, 112.94, 45.64, 41.60],
[0.55, 0.186, 107.35, 42.97, 40.88],
[0.56, 0.197, 102.20, 40.54, 40.21],
[0.57, 0.209, 97.46, 38.32, 39.60],
[0.58, 0.220, 93.08, 36.28, 39.03],
[0.59, 0.232, 89.03, 34.41, 38.51],
[0.60, 0.245, 85.28, 32.69, 38.04],
[0.61, 0.257, 81.79, 31.11, 37.60],
[0.62, 0.270, 78.55, 29.66, 37.20],
[0.63, 0.282, 75.53, 28.31, 36.83],
[0.64, 0.295, 72.71, 27.07, 36.49],
[0.65, 0.308, 70.07, 25.93, 36.19],
[0.66, 0.322, 67.60, 24.86, 35.92],
[0.67, 0.335, 65.28, 23.88, 35.67],
[0.68, 0.348, 63.10, 22.97, 35.44],
[0.69, 0.362, 61.05, 22.12, 35.25],
[0.70, 0.375, 59.12, 21.33, 35.07],
[0.71, 0.388, 57.30, 20.59, 34.92],
[0.72, 0.402, 55.58, 19.91, 34.78],
[0.73, 0.415, 53.95, 19.27, 34.67],
[0.74, 0.428, 52.41, 18.67, 34.57],
[0.75, 0.442, 50.94, 18.11, 34.50],
[0.76, 0.455, 49.56, 17.59, 34.44],
[0.77, 0.468, 48.24, 17.10, 34.39],
[0.78, 0.481, 46.98, 16.64, 34.36],
[0.79, 0.493, 45.79, 16.21, 34.35],
[0.80, 0.506, 44.65, 15.81, 34.35],
[0.81, 0.518, 43.56, 15.43, 34.36],
[0.82, 0.531, 42.53, 15.08, 34.39],
[0.83, 0.543, 41.54, 14.74, 34.42],
[0.84, 0.554, 40.60, 14.43, 34.48],
[0.85, 0.566, 39.69, 14.13, 34.54],
[0.86, 0.578, 38.83, 13.85, 34.62],
[0.87, 0.589, 38.01, 13.59, 34.70],
[0.88, 0.600, 97.22, 13.34, 34.80],
[0.89, 0.611, 96.46, 13.10, 34.91],
[0.90, 0.621, 95.73, 12.88, 35.03],
[0.91, 0.632, 35.04, 12.67, 35.16],
[0.92, 0.642, 34.37, 12.47, 35.29],
[0.93, 0.652, 33.73, 12.28, 35.44],
[0.94, 0.661, 33.12, 12.10, 35.60],
[0.95, 0.671, 32.53, 11.93, 35.77],
[0.96, 0.680, 31.97, 11.77, 35.95],
[0.97, 0.689, 31.43, 11.61, 36.13],
[0.98, 0.697, 30.91, 11.47, 36.33],
[0.99, 0.706, 30.41, 11.33, 36.53],
[1.00, 0.714, 29.93, 11.20, 36.74],
[ 1.00, 0.714, 29.93, 11.20, 36],
[ 1.02, 0.730, 29.02, 10.96, 37],
[ 1.04, 0.745, 28.18, 10.73, 37],
[ 1.06, 0.759, 27.41, 10.53, 38],
[ 1.08, 0.773, 26.69, 10.35, 38],
[ 1.10, 0.785, 26.02, 10.18, 39],
[ 1.12, 0.797, 25.40, 10.03, 39],
[1.14, 0.808, 24.83, 9.89, 40.55],
[1.16, 0.819, 24.29, 9.77, 41.21],
[1.18, 0.829, 23.79, 9.65, 41.90],
[1.20, 0.838, 23.33, 9.45, 42.62],
[1.22, 0.847, 22.89, 9.44, 43.36],
[1.24, 0.855, 22.49, 9.35, 44.13],
[1.26, 0.863, 22.11, 9.27, 44.93],
[1.28, 0.870, 21.75, 9.19, 45.75],
[1.30, 0.877, 21.42, 9.12, 46.59],
[1.32, 0.884, 21.11, 9.05, 47.46],
[1.34, 0.889, 20.82, 8.99, 48.34],
[1.36, 0.895, 20.54, 8.93, 49.26],
[1.38, 0.901, 20.28, 8.88, 50.20],
[1.40, 0.906, 20.04, 8.83, 51.15],
[1.42, 0.910, 19.81, 8.79, 52.14],
[1.44, 0.915, 19.59, 8.74, 53.14],
[1.46, 0.919, 19.39, 8.70, 54.16],
[1.48, 0.923, 19.20, 8.67, 55.21],
[1.50, 0.927, 19.01, 8.63, 56.28],
[1.52, 0.930, 18.84, 8.60, 57.36],
[1.54, 0.934, 18.68, 8.57, 58.47],
[1.56, 0.937, 18.52, 8.54, 59.60],
[1.58, 0.940, 18.37, 8.51, 60.74],
[1.60, 0.942, 18.23, 8.49, 61.91],
[1.62, 0.945, 18.10, 8.46, 63.11],
[1.64, 0.948, 17.97, 8.44, 64.31],
[1.66, 0.950, 17.85, 8.42, 65.53],
[1.68, 0.952, 17.74, 8.40, 66.78],
[1.70, 0.954, 17.63, 8.38, 68.04],
[1.72, 0.956, 17.52, 8.36, 69.33],
[1.74, 0.958, 17.42, 8.35, 70.63],
[1.76, 0.960, 17.33, 8.33, 71.96],
[1.78, 0.962, 17.25, 8.32, 73.30],
[1.80, 0.963, 17.15, 8.30, 74.65],
[1.82, 0.965, 17.07, 8.29, 76.03],
[1.84, 0.966, 16.99, 8.28, 77.42],
[1.86, 0.968, 16.91, 8.27, 78.85],
[1.88, 0.969, 16.84, 8.26, 80.27],
[1.90, 0.970, 16.77, 8.24, 81.73],
[1.92, 0.971, 16.70, 8.23, 83.18],
[1.94, 0.972, 16.64, 8.23, 84.67],
[1.96, 0.974, 16.57, 8.22, 86.19],
[1.98, 0.975, 16.51, 8.21, 87.70],
[2.00, 0.976, 16.46, 8.20, 89.22],])


caso3 = np.array([
[1.00, 0.500, 37.14, 16.00, 37.14, 16.00],
[1.01, 0.510, 36.42, 15.69, 37.15, 16.00],
[1.02, 0.520, 35.72, 15.39, 37.16, 16.01],
[1.03, 0.529, 35.05, 15.11, 37.19, 16.03],
[1.04, 0.539, 34.42, 14.84, 37.22, 16.05],
[1.05, 0.549, 33.81, 14.58, 37.27, 16.08],
[1.06, 0.558, 33.21, 14.34, 27.32, 16.11],
[1.07, 0.567, 32.65, 14.10, 37.38, 16.15],
[1.08, 0.576, 32.11, 13.88, 37.45, 16.19],
[1.09, 0.585, 31.59, 13.67, 37.53, 16.24],
[1.10, 0.594, 31.09, 13.46, 37.61, 16.29],
[1.11, 0.603, 30.61, 13.27, 37.71, 16.35],
[1.12, 0.611, 30.14, 13.08, 37.81, 16.41],
[1.13, 0.620, 29.70, 12.91, 37.92, 16.48],
[1.14, 0.628, 29.27, 12.74, 38.04, 16.55],
[1.15, 0.636, 28.85, 12.57, 38.16, 16.63],
[1.16, 0.644, 28.46, 12.42, 38.29, 16.71],
[1.17, 0.652, 28.08, 12.27, 38.43, 16.79],
[1.18, 0.660, 27.71, 12.13, 38.58, 16.88],
[1.19, 0.667, 27.35, 11.99, 38.73, 16.98],
[1.20, 0.674, 27.00, 11.85, 38.89, 17.07],
[1.21, 0.682, 26.68, 11.73, 39.06, 17.18],
[1.22, 0.690, 26.36, 11.61, 39.23, 17.28],
[1.23, 0.696, 26.05, 11.49, 39.41, 17.39],
[1.24, 0.703, 25.75, 11.38, 39.59, 17.50],
[1.25, 0.709, 25.46, 11.28, 39.78, 17.62],
[1.26, 0.716, 25.18, 11.17, 39.98, 17.74],
[1.27, 0.722, 24.92, 11.07, 40.19, 17.86],
[1.28, 0.729, 24.66, 10.98, 40.40, 17.99],
[1.29, 0.735, 24.40, 10.89, 40.61, 18.12],
[1.30, 0.741, 24.16, 10.80, 40.83, 18.25],
[1.31, 0.746, 23.93, 10.72, 41.06, 18.39],
[1.32, 0.752, 23.70, 10.63, 41.29, 18.53],
[1.33, 0.758, 23.48, 10.56, 41.53, 18.67],
[1.34, 0.763, 23.26, 10.48, 41.77, 18.82],
[1.35, 0.769, 23.06, 10.41, 42.02, 18.97],
[1.36, 0.774, 22.86, 10.34, 42.28, 19.12],
[1.37, 0.779, 22.66, 10.27, 42.54, 19.28],
[1.38, 0.784, 22.48, 10.21, 42.80, 19.43],
[1.39, 0.789, 22.29, 10.14, 43.07, 19.60],
[1.40, 0.793, 22.12, 10.08, 43.35, 19.76],
[1.41, 0.798, 21.95, 10.02, 43.63, 19.93],
[1.42, 0.803, 21.78,  9.97, 43.92, 20.10],
[1.43, 0.807, 21.62,  9.91, 44.21, 20.27],
[1.44, 0.811, 21.46,  9.86, 44.50, 20.45],
[1.45, 0.815, 21.31,  9.81, 44.80, 20.62],
[1.46, 0.820, 21.16,  9.76, 45.11, 20.80],
[1.47, 0.824, 21.02,  9.71, 45.42, 20.99],
[1.48, 0.827, 20.88,  9.67, 45.74, 21.17],
[1.49, 0.831, 20.75,  9.62, 46.06, 21.36],
[1.50, 0.835, 20.61,  9.38, 46.38, 21.55],
[1.50, 0.835, 20.61, 9.58, 46.38, 21.55],
[1.51, 0.839, 20.49, 9.54, 46.71, 21.75],
[1.52, 0.842, 20.36, 9.50, 47.05, 21.94],
[1.53, 0.846, 20.24, 9.46, 47.38, 22.14],
[1.54, 0.849, 20.12, 9.42, 47.73, 22.34],
[1.55, 0.852, 20.01, 9.39, 48.07, 22.55],
[1.56, 0.855, 19.90, 9.35, 48.43, 22.76],
[1.57, 0.859, 19.79, 9.32, 48.78, 22.96],
[1.58, 0.862, 19.69, 9.28, 49.14, 23.17],
[1.59, 0.865, 19.58, 9.25, 49.51, 23.09],
[1.60, 0.868, 19.48, 9.22, 49.88, 23.60],
[1.61, 0.870, 19.39, 9.19, 50.25, 23.82],
[1.62, 0.873, 19.29, 9.16, 52.63, 24.04],
[1.63, 0.876, 19.20, 9.13, 51.01, 24.26],
[1.64, 0.878, 19.11, 9.11, 51.40, 24.49],
[1.65, 0.881, 19.02, 9.08, 51.79, 24.72],
[1.66, 0.884, 18.94, 9.05, 52.19, 24.95],
[1.67, 0.886, 18.86, 9.03, 52.58, 25.18],
[1.68, 0.888, 18.77, 9.00, 52.99, 25.41],
[1.69, 0.891, 18.70, 8.98, 53.39, 25.65],
[1.70, 0.893, 18.62, 8.96, 53.81, 25.89],
[1.71, 0.895, 18.54, 8.93, 54.22, 26.13],
[1.72, 0.897, 18.47, 8.91, 54.64, 26.37],
[1.73, 0.899, 18.40, 8.89, 55.07, 26.61],
[1.74, 0.902, 18.33, 8.87, 55.49, 26.86],
[1.75, 0.904, 18.26, 8.85, 55.92, 27.11],
[1.76, 0.906, 18.18, 8.83, 56.36, 27.36],
[1.77, 0.907, 18.13, 8.81, 56.80, 27.61],
[1.78, 0.909, 18.07, 8.80, 57.24, 27.87],
[1.79, 0.911, 18.00, 8.78, 57.68, 28.13],
[1.80, 0.913, 17.94, 8.76, 58.14, 28.39],
[1.81, 0.915, 17.88, 8.74, 58.59, 28.65],
[1.82, 0.916, 17.83, 8.73, 59.05, 28.91],
[1.83, 0.918, 17.77, 8.71, 59.51, 29.18],
[1.84, 0.920, 17.72, 8.70, 59.97, 29.44],
[1.85, 0.921, 17.66, 8.68, 60.44, 29.72],
[1.86, 0.923, 17.61, 8.67, 60.92, 29.99],
[1.87, 0.924, 17.56, 8.65, 61.39, 30.26],
[1.88, 0.926, 17.51, 8.64, 61.88, 30.54],
[1.89, 0.927, 17.46, 8.63, 62.36, 30.81],
[1.90, 0.929, 17.41, 8.61, 62.85, 31.09],
[1.91, 0.930, 17.36, 8.60, 63.34, 31.38],
[1.92, 0.931, 17.32, 8.59, 63.83, 31.66],
[1.93, 0.933, 17.27, 8.58, 64.33, 31.94],
[1.94, 0.934, 17.23, 8.56, 64.83, 32.23],
[1.95, 0.935, 17.18, 8.55, 65.34, 32.52],
[1.96, 0.936, 17.14, 8.54, 65.84, 32.81],
[1.97, 0.938, 17.10, 8.53, 66.36, 33.10],
[1.98, 0.939, 17.06, 8.52, 66.88, 33.40],
[1.99, 0.940, 17.02, 8.51, 67.39, 33.70],
[2.00, 0.941, 16.93, 8.50, 67.92, 34.00],])


caso5 = np.array([
[0.50, 0.111, 246.52, 108.00, 71.43, 36.00],    
[0.51, 0.119, 230.76, 100.70, 69.53, 34.92],   
[0.52, 0.127, 216.51, 95.07, 67.77, 33.91],     
[0.53, 0.136, 203.52, 88.05, 66.13, 32.97],     
[0.54, 0.145, 191.66, 82.56, 64.60, 32.10],     
[0.55, 0.155, 180.83, 77.57, 63.18, 31.29],     
[0.56, 0.164, 170.91, 73.01, 61.86, 30.53],     
[0.57, 0.174, 161.79, 68.84, 60.63, 29.82],     
[0.58, 0.184, 153.42, 65.02, 59.49, 29.16],     
[0.59, 0.195, 145.72, 61.52, 58.42, 28.55],     
[0.60, 0.206, 138.61, 58.30, 57.43, 27.98],     
[0.61, 0.217, 132.05, 55.34, 56.52, 27.45],     
[0.62, 0.228, 125.98, 52.61, 55.67, 26.96],     
[0.63, 0.239, 120.36, 50.09, 54.88, 26.51],     
[0.64, 0.251, 115.15, 47.76, 54.15, 26.08],     
[0.65, 0.263, 110.30, 45.61, 53.48, 25.69],     
[0.66, 0.275, 105.81, 43.62, 52.85, 25.33],     
[0.67, 0.287, 101.61, 41.77, 52.28, 25.00],     
[0.68, 0.299,  97.70, 40.06, 51.76, 24.70],   	
[0.69, 0.312,  94.06, 38.47, 51.28, 24.42],   	
[0.70, 0.324,  90.65, 36.99, 50.84, 24.17],   	
[0.71, 0.337,  87.46, 35.61, 50.45, 23.93],   	
[0.72, 0.349,  84.48, 34.33, 50.09, 23.73],   	
[0.73, 0.362,  81.68, 33.13, 49.77, 23.54],   	
[0.74, 0.375,  82.05, 32.48, 49.05, 23.37],   	
[0.75, 0.387,  76.58, 30.96, 49.23, 23.22],   	
[0.76, 0.400,  74.26, 29.98, 49.00, 23.09],   	
[0.77, 0.413,  72.08, 29.07, 48.81, 22.98],   	
[0.78, 0.425,  70.02, 28.21, 48.65, 22.88],   	
[0.79, 0.438,  68.08, 27.40, 48.51, 22.80],   	
[0.80, 0.450,  66.24, 26.65, 48.40, 22.74],   	
[0.81, 0.463,  64.51, 25.94, 48.32, 22.69],   	
[0.82, 0.475,  62.88, 25.27, 48.26, 22.65],   	
[0.83, 0.487,  61.33, 24.64, 48.22, 22.63],   	
[0.84, 0.499,  59.86, 24.05, 48.21, 22.63],   	
[0.85, 0.511,  58.47, 23.49, 48.22, 22.63],   	
[0.86, 0.522,  57.15, 22.97, 48.25, 22.65],   	
[0.87, 0.543,  55.90, 22.47, 48.30, 22.68],   	
[0.88, 0.545,  54.71, 22.00, 48.37, 22.72],   	
[0.89, 0.558,  53.58, 21.56, 48.46, 22.77],   	
[0.90, 0.567,  52.51, 21.14, 48.57, 22.84],   	
[0.91, 0.578,  51.49, 20.75, 48.69, 22.91],   	
[0.92, 0.589,  50.51, 20.37, 48.83, 22.99],   	
[0.93, 0.599,  49.59, 20.02, 48.99, 23.09],   	
[0.94, 0.610,  48.70, 19.68, 49.17, 23.19],   	
[0.95, 0.620,  47.86, 19.37, 49.06, 13.30],   	
[0.96, 0.629,  47.06, 19.06, 49.57, 23.42],   	
[0.97, 0.639,  46.29, 18.78, 49.80, 23.56],   	
[0.98, 0.648,  45.55, 18.50, 50.04, 23.70],   	
[0.99, 0.658,  44.85, 18.25, 50.29, 23.84],   	
[1.00, 0.667,  44.18, 18.00, 50.56, 24.00],
[1.00, 0.667, 44.18, 18.00,  50.56, 24.00],
[1.02, 0.684, 42.92, 17.54,  51.14, 24.33],
[1.04, 0.700, 41.77, 17.13,  51.76, 24.70],
[1.06, 0.716, 40.71, 16.75,  52.44, 25.10],
[1.08, 0.731, 39.74, 16.41,  53.18, 25.52],
[1.10, 0.745, 38.84, 16.10,  53.95, 25.97],
[1.12, 0.759, 38.01, 15.81,  54.78, 26.45],
[1.14, 0.772, 37.25, 15.55,  55.64, 26.95],
[1.16, 0.784, 36.54, 15.31,  56.55, 27.47],
[1.18, 0.795, 35.88, 15.09,  57.50, 28.02],
[1.20, 0.806, 35.27, 14.89,  58.50, 28.59],
[1.22, 0.816, 34.70, 14.71,  59.53, 29.19],
[1.24, 0.825, 34.17, 14.54,  60.60, 29.80],
[1.26, 0.834, 33.68, 14.38,  61.71, 30.44],
[1.28, 0.843, 33.22, 14.23,  62.85, 31.10],
[1.30, 0.851, 32.79, 14.10,  64.03, 31.77],
[1.32, 0.859, 32.38, 13.98,  65.25, 32.47],
[1.34, 0.866, 32.01, 13.86,  66.50, 33.18],
[1.36, 0.872, 31.65, 13.75,  66.78, 33.92],
[1.38, 0.879, 31.02, 13.65,  69.10, 34.67],
[1.40, 0.885, 31.01, 13.56,  70.45, 35.44],
[1.42, 0.890, 30.72, 13.47,  71.83, 36.23],
[1.44, 0.896, 30.44, 13.39,  73.24, 37.03],
[1.46, 0.901, 30.18, 13.32,  74.69, 37.86],
[1.48, 0.906, 29.94, 13.25,  76.17, 38.70],
[1.50, 0.910, 29.71, 13.18,  77.67, 39.55],
[1.52, 0.914, 29.49, 13.12,  79.20, 40.43],
[1.54, 0.918, 29.28, 13.07,  80.77, 41.32],
[1.56, 0.922, 29.09, 13.01,  82.36, 12.22],
[1.58, 0.926, 28.90, 12.96,  83.98, 43.14],
[1.60, 0.929, 28.73, 12.91,  85.64, 44.08],
[1.62, 0.932, 28.56, 12.87,  87.31, 45.03],
[1.64, 0.935, 28.40, 12.83,  89.02, 46.00],
[1.66, 0.938, 28.25, 12.79,  90.77, 46.99],
[1.68, 0.941, 28.11, 12.75,  92.52, 47.98],
[1.70, 0.943, 27.97, 12.72,  94.32, 49.00],
[1.72, 0.946, 27.84, 12.68,  96.13, 50.03],
[1.74, 0.948, 27.72, 12.65,  97.98, 51.08],
[1.76, 0.950, 27.60, 12.62,  99.86, 52.14],
[1.78, 0.952, 27.49, 12.60, 101.75, 53.21],
[1.80, 0.954, 27.38, 12.57, 103.68, 54.30],
[1.82, 0.956, 27.28, 12.55, 105.63, 55.41],
[1.84, 0.958, 27.18, 12.52, 107.62, 56.63],
[1.86, 0.960, 27.09, 12.50, 109.63, 57.67],
[1.88, 0.961, 27.00, 12.48, 111.65, 58.81],
[1.90, 0.963, 26.91, 12.46, 110.71, 59.97],
[1.92, 0.964, 26.83, 12.44, 115.79, 61.15],
[1.94, 0.966, 26.75, 12.42, 117.89, 62.33],
[1.96, 0.967, 26.68, 12.41, 120.04, 63.55],
[1.98, 0.968, 26.61, 12.39, 122.19, 64.76],
[2.00, 0.970, 26.54, 12.37, 124.35, 65.98]])


caso6 = np.array([
[1.00, 0.500, 55.74, 24.00, 55.74, 24.00], 
[1.01, 0.510, 54.65, 32.53, 55.75, 24.00], 
[1.02, 0.520, 53.61, 32.09, 55.78, 24.02], 
[1.03, 0.529, 52.62, 22.66, 55.82, 24.04], 
[1.04, 0.539, 51.76, 22.26, 55.88, 24.07], 
[1.05, 0.549, 50.76, 21.87, 55.96, 24.11], 
[1.06, 0.558, 49.89, 21.50, 56.06, 24.16], 
[1.07, 0.567, 49.06, 21.15, 56.17, 24.22], 
[1.08, 0.576, 48.27, 20.82, 56.30, 24.28], 
[1.09, 0.585, 47.50, 20.50, 56.44, 24.36], 
[1.10, 0.594, 46.77, 20.20, 56.59, 24.44], 
[1.11, 0.603, 46.07, 19.90, 56.76, 24.52], 
[1.12, 0.611, 45.40, 19.63, 56.95, 24.62], 
[1.13, 0.620, 44.75, 19.36, 57.14, 24.72], 
[1.14, 0.628, 44.13, 19.10, 57.36, 24.83], 
[1.15, 0.636, 43.54, 18.86, 57.58, 24.94], 
[1.16, 0.644, 42.97, 18.63, 57.82, 25.06], 
[1.17, 0.652, 42.42, 18.40, 58.07, 25.19], 
[1.18, 0.660, 41.89, 18.19, 58.33, 25.33], 
[1.19, 0.667, 41.38, 17.98, 58.60, 25.47], 
[1.20, 0.675, 40.90, 17.79, 58.89, 25.61], 
[1.21, 0.682, 40.42, 17.60, 59.19, 25.76], 
[1.22, 0.689, 39.97, 17.42, 59.49, 25.92], 
[1.23, 0.696, 39.54, 17.24, 59.81, 26.09], 
[1.24, 0.703, 39.12, 17.07, 60.15, 26.25], 
[1.25, 0.709, 38.71, 16.91, 60.49, 26.43], 
[1.26, 0.716, 38.32, 16.76, 60.84, 26.61], 
[1.27, 0.722, 37.95, 16.61, 61.20, 26.79], 
[1.28, 0.729, 37.58, 16.47, 61.57, 26.98], 
[1.29, 0.735, 37.23, 16.33, 61.96, 27.18], 
[1.30, 0.741, 36.89, 16.20, 62.05, 27.38], 
[1.31, 0.746, 36.57, 16.07, 62.75, 27.58], 
[1.32, 0.752, 36.25, 15.95, 63.16, 27.79], 
[1.33, 0.758, 35.95, 15.83, 63.59, 28.01], 
[1.34, 0.763, 35.65, 15.72, 64.02, 28.23], 
[1.35, 0.769, 35.37, 15.61, 64.46, 28.45], 
[1.36, 0.774, 35.09, 15.51, 64.91, 28.68], 
[1.37, 0.779, 34.83, 15.41, 65.36, 28.91], 
[1.38, 0.784, 34.57, 15.31, 65.83, 29.15], 
[1.39, 0.789, 34.32, 15.21, 66.31, 29.39], 
[1.40, 0.793, 34.08, 15.12, 66.79, 29.64], 
[1.41, 0.798, 33.85, 15.04, 67.29, 29.89], 
[1.42, 0.803, 33.62, 14.95, 67.79, 30.15], 
[1.43, 0.807, 33.40, 14.87, 68.30, 30.40], 
[1.44, 0.811, 33.19, 14.79, 68.82, 30.67], 
[1.45, 0.815, 32.98, 14.71, 69.34, 30.94], 
[1.46, 0.820, 32.78, 14.64, 69.88, 31.21], 
[1.47, 0.824, 32.59, 14.57, 70.42, 31.48], 
[1.48, 0.827, 32.40, 14.50, 70.97, 31.76], 
[1.49, 0.831, 32.22, 14.43, 71.53, 32.04], 
[1.50, 0.835, 32.04, 14.37, 72.10, 32.33], 
[1.50, 0.835, 32.04, 14.37,  72.10, 32.33],
[1.51, 0.839, 31.87, 14.31,  72.67, 32.62],
[1.52, 0.842, 31.71, 14.25,  73.25, 32.92],
[1.53, 0.846, 31.54, 14.19,  73.84, 33.22],
[1.54, 0.849, 31.39, 14.13,  74.44, 33.52],
[1.55, 0.852, 31.24, 14.08,  75.04, 33.82],
[1.56, 0.855, 31.09, 14.03,  75.65, 34.13],
[1.57, 0.859, 30.94, 13.97,  76.27, 34.45],
[1.58, 0.862, 30.80, 13.92,  76.90, 34.79],
[1.59, 0.865, 30.67, 13.88,  77.52, 35.08],
[1.60, 0.868, 30.54, 13.83,  78.17, 35.41],
[1.61, 0.870, 30.41, 13.79,  78.81, 35.73],
[1.62, 0.873, 30.28, 13.74,  79.47, 36.06],
[1.63, 0.876, 30.16, 13.70,  80.13, 36.40],
[1.64, 0.878, 30.04, 13.66,  80.80, 36.74],
[1.65, 0.881, 29.93, 13.62,  81.48, 37.08],
[1.66, 0.884, 29.82, 13.58,  82.16, 37.42],
[1.67, 0.886, 29.71, 13.54,  82.84, 37.77],
[1.68, 0.888, 29.60, 13.51,  83.54, 38.12],
[1.69, 0.891, 29.50, 13.47,  84.24, 38.47],
[1.70, 0.893, 29.40, 13.44,  84.95, 38.83],
[1.71, 0.895, 29.30, 13.40,  85.67, 39.19],
[1.72, 0.897, 29.20, 13.37,  86.38, 39.55],
[1.73, 0.899, 29.11, 13.34,  87.12, 39.92],
[1.74, 0.902, 29.02, 13.31,  87.85, 40.29],
[1.75, 0.904, 28.93, 13.28,  88.60, 40.67],
[1.76, 0.906, 28.84, 13.25,  89.34, 41.04],
[1.77, 0.907, 28.76, 13.22,  90.09, 41.42],
[1.78, 0.909, 28.68, 13.19,  90.86, 41.81],
[1.79, 0.911, 28.60, 13.17,  91.61, 42.19],
[1.80, 0.913, 28.52, 13.14,  92.39, 42.58],
[1.81, 0.915, 28.44, 13.12,  93.17, 42.97],
[1.82, 0.916, 28.37, 13.09,  93.96, 43.37],
[1.83, 0.918, 28.29, 13.07,  94.75, 43.77],
[1.84, 0.920, 28.22, 13.05,  95.54, 44.17],
[1.85, 0.921, 28.15, 13.02,  96.35, 44.57],
[1.86, 0.923, 28.09, 13.00,  97.16, 44.98],
[1.87, 0.924, 28.02, 12.98,  97.98, 45.09],
[1.88, 0.926, 27.95, 12.96,  98.80, 45.81],
[1.89, 0.927, 27.89, 12.94,  99.62, 46.22],
[1.90, 0.929, 27.83, 12.92, 100.46, 46.64],
[1.91, 0.930, 27.77, 12.90, 101.30, 47.06],
[1.92, 0.931, 27.71, 12.88, 102.14, 47.49],
[1.93, 0.933, 27.65, 12.86, 103.00, 47.92],
[1.94, 0.934, 27.60, 12.85, 103.85, 48.35],
[1.95, 0.935, 27.54, 12.83, 104.72, 48.78],
[1.96, 0.936, 27.49, 12.81, 105.58, 49.21],
[1.97, 0.938, 27.43, 12.80, 106.45, 49.65],
[1.98, 0.939, 27.38, 12.78, 107.35, 50.10],
[1.99, 0.940, 27.33, 12.76, 108.23, 50.55],
[2.00, 0.941, 27.28, 12.75, 109.12, 50.99],])


caso4 = np.array([
[1.00, 0.833, 37.47, 14.40,  55.74], 
[1.02, 0.844, 36.71, 14.22,  57.01], 
[1.04, 0.854, 36.00, 14.05,  58.33], 
[1.06, 0.863, 35.34, 13.90,  59.70], 
[1.08, 0.872, 34.74, 13.76,  61.12], 
[1.10, 0.880, 34.18, 13.64,  62.59], 
[1.12, 0.887, 33.66, 13.52,  64.10], 
[1.14, 0.894, 33.18, 13.42,  65.66], 
[1.16, 0.900, 32.74, 13.32,  67.26], 
[1.18, 0.906, 32.32, 13.24,  68.91], 
[1.20, 0.912, 31.93, 13.16,  70.60], 
[1.22, 0.917, 31.57, 13.08,  72.33], 
[1.24, 0.922, 31.23, 13.01,  74.11], 
[1.26, 0.926, 30.92, 12.95,  75.92], 
[1.28, 0.931, 30.62, 12.89,  77.78], 
[1.30, 0.934, 30.34, 12.84,  79.66], 
[1.32, 0.938, 30.08, 12.79,  81.60], 
[1.34, 0.942, 29.83, 12.74,  83.58], 
[1.36, 0.945, 29.60, 12.70,  85.58], 
[1.38, 0.948, 29.39, 12.66,  87.63], 
[1.40, 0.950, 29.18, 12.62,  89.72], 
[1.42, 0.953, 28.99, 12.59,  91.84], 
[1.44, 0.955, 28.80, 12.56,  94.01], 
[1.46, 0.958, 28.63, 12.53,  96.20], 
[1.48, 0.960, 28.47, 12.50,  98.45], 
[1.50, 0.962, 28.31, 12.47, 100.72],
[1.52, 0.964, 28.16, 12.45, 103.02],
[1.54, 0.966, 28.02, 12.43, 105.38],
[1.56, 0.967, 27.89, 12.40, 107.76],
[1.58, 0.969, 27.76, 12.38, 110.16],
[1.60, 0.970, 27.64, 12.37, 112.61],
[1.62, 0.972, 27.53, 12.35, 115.12],
[1.64, 0.973, 27.42, 12.33, 117.62],
[1.66, 0.974, 27.31, 12.32, 120.17],
[1.68, 0.975, 27.21, 12.30, 122.76],
[1.70, 0.977, 27.12, 12.29, 125.41],
[1.72, 0.978, 27.03, 12.27, 128.04],
[1.74, 0.979, 26.94, 12.26, 130.75],
[1.76, 0.800, 26.86, 12.25, 133.50],
[1.78, 0.980, 26.78, 12.24, 136.24],
[1.80, 0.981, 26.70, 12.23, 139.05],
[1.82, 0.982, 26.63, 12.22, 141.85],
[1.84, 0.983, 26.56, 12.21, 144.78],
[1.86, 0.983, 26.49, 12.20, 147.65],
[1.88, 0.984, 26.43, 12.19, 150.60],
[1.90, 0.985, 26.37, 12.18, 153.54],
[1.92, 0.985, 26.31, 12.18, 156.53],
[1.94, 0.986, 26.25, 12.17, 159.56],
[1.96, 0.987, 26.19, 12.16, 162.60],
[1.98, 0.987, 26.14, 12.16, 165.75],
[2.00, 0.988, 26.09, 12.15, 168.80],



[0.50, 0.238, 37.06, 50.40, 49.92],
[0.51, 0.253, 30.06, 47.48, 49.11],
[0.52, 0.268, 23.66, 44.83, 48.38],
[0.53, 0.283, 17.79, 42.42, 47.72],
[0.54, 0.298, 12.39, 40.23, 47.13],
[0.55, 0.314, 107.42, 38.23, 46.60],
[0.56, 0.330, 102.83, 36.40, 46.13],
[0.57, 0.345, 98.59, 34.74, 45.72],
[0.58, 0.361, 94.67, 33.21, 45.35],
[0.59, 0.377, 91.02, 31.81, 45.04],
[0.60, 3.930, 87.62, 30.52, 44.77],
[0.61, 0.409, 84.46, 29.33, 44.54],
[0.62, 0.425, 81.51, 28.24, 44.35],
[0.63, 0.441, 78.76, 27.24, 44.21],
[0.64, 0.456, 76.18, 26.30, 44.10],
[0.65, 0.472, 73.76, 25.45, 44.02],
[0.66, 0.487, 71.49, 24.65, 43.98],
[0.67, 0.502, 69.36, 23.91, 47.97],
[0.68, 0.517, 67.36, 23.22, 43.98],
[0.69, 0.531, 65.47, 22.59, 44.03],
[0.70, 0.545, 63.69, 22.00, 44.11],
[0.71, 0.559, 62.01, 21.44, 44.21],
[0.72, 0.573, 60.42, 20.93, 44.34],
[0.73, 0.587, 58.92, 20.45, 44.49],
[0.74, 0.600, 57.51, 20.00, 44.66],
[0.75, 0.613, 56.16, 19.38, 44.86],
[0.76, 0.625, 54.89, 19.19, 45.08],
[0.77, 0.637, 53.69, 18.83, 45.33],
[0.78, 0.649, 52.54, 18.48, 45.59],
[0.79, 0.661, 51.46, 18.16, 45.87],
[0.80, 0.672, 50.42, 17.86, 46.17],
[0.81, 0.683, 49.44, 17.57, 46.30],
[0.82, 0.693, 48.51, 17.31, 46.84],
[0.83, 0.703, 47.62, 17.06, 47.20],
[0.84, 0.713, 46.78, 16.82, 47.57],
[0.85, 0.723, 45.97, 16.60, 47.97],
[0.86, 0.732, 45.21, 16.39, 48.38],
[0.87, 0.741, 44.48, 16.19, 48.81],
[0.88, 0.750, 43.78, 16.00, 49.25],
[0.89, 0.758, 43.12, 15.82, 49.71],
[0.90, 0.766, 42.48, 15.66, 50.19],
[0.91, 0.774, 41.87, 15.50, 50.68],
[0.92, 0.782, 41.30, 15.35, 51.18],
[0.93, 0.789, 40.74, 15.21, 51.50],
[0.94, 0.796, 40.21, 15.07, 52.24],
[0.95, 0.803, 39.70, 14.95, 52.78],
[0.96, 0.809, 39.22, 14.82, 53.35],
[0.97, 0.816, 38.75, 14.72, 53.92],
[0.98, 0.822, 38.31, 14.60, 54.52],
[0.99, 0.828, 37.88, 14.50, 55.12],
[1.00, 0.833, 37.47, 14.40, 55.74],
 

])
'''
lx = 6
ly = 5

lamdia = ly/lx
lamdia = round(lamdia,ndigits=2)

linhas = len(caso2)
colunas = len(caso2[0])

for i in range(linhas):
	aux = caso2[i][0]

	if lamdia == aux:
		print(caso2[i])

print()
'''