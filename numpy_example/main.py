import numpy as np

# Tạo một mảng 1 chiều
array_1d = np.array([1, 2, 3, 4])
print(array_1d)

# Tạo một mảng 2 chiều
array_2d = np.array([[1, 2], [3, 4]])
print(array_2d)

print(array_1d.sum())

reshaped = array_1d.reshape(4,1)
print(reshaped)