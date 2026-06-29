import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr_2d.ndim)

arr_3d = np.array([[[1,2,3], [4, 5, 6], [7, 8, 9]]])
print(arr_3d.ndim)

print(arr_3d.shape)

arr_ones_2x2 = np.ones(shape=(2,2))
arr_zeros_3x3 = np.zeros(shape=(3, 3))

print(arr_ones_2x2)
print(arr_zeros_3x3)

arr_range = np.arange(1, 10, 2, dtype=np.float32)

print(arr_range)

arr_randint = np.random.randint(0, 100, size=(3,3))
print(arr_randint)

arr_float = np.random.rand((3,3))
print(arr_float)

arr_n = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
mask = arr_n > 5
print(mask)

print(arr_n[0:3, 1:3])

# [
#     [2, 3],
#     [5, 6].
#     [8, 9]
# ]

print(arr_n ** 2)
#vectorization

a = np.array([
    [1, 2, 3]
])
print(arr_n + a)
#broadcasting


b = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])

arr_simple = np.array(
    [1,2,3,4,5, 6]
)
print(arr_simple.shape)
arr_simple.reshape(2,3)#col and rows