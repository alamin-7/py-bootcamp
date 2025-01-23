
# Array slicing
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

'''
# Search in array
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
'''

# filtering

'''
import numpy as np

arr = np.array([41, 42, 43, 44])

x = arr[[True, False, True, False]]

print(x)
'''