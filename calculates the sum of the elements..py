import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)

reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped_arr)


print("\nElement at index 2:", arr[2])
print("Element at row 1, column 2:", reshaped_arr[1, 2])


total = np.sum(arr)
print("\nSum of elements:", total)
