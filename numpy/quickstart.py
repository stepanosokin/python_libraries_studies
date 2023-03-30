# https://numpy.org/devdocs/user/quickstart.html

import numpy as np
import sys

# # An example
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.shape)
# print(a.dtype.name)
# print(a.itemsize)
# print(a.size)
# print(type(a))
# b = np.array([6, 7, 8])
# print(b)
# print(type(b))


# # Array Creation
# a = np.array([2, 3, 4], dtype=np.int64)
# print(a)
# print(a.dtype)
# b = np.array([1.2, 3.4, 5.6])
# print(b)
# print(b.dtype)
#
# # a = np.array(1, 2, 3, 4)    # WRONG
# a = np.array([1, 2, 3, 4])  # RIGHT
#
# b = np.array([(1.5, 2, 3), (4, 5, 6)])
# print(b)
#
# c = np.array([[1, 2], [3, 4]], dtype=complex)
# print(c)
#
# print(np.zeros((3, 4)))
#
# print(np.ones((2, 3, 4), dtype=np.int64))
#
# print(np.empty((2, 3)))
#
# print(np.arange(10, 30, 5))
#
# print(np.arange(0, 2, 0.3))
#
# print(np.linspace(0, 2, 9))



# # Printing Arrays
#
# a = np.arange(6)
# print(a)
#
# a = np.arange(12).reshape(4, 3)
# print(a)
#
# c = np.arange(24).reshape(2, 3, 4)
# print(c)
#
# # np.set_printoptions(threshold=sys.maxsize)
#
# print(np.arange(10000))
# print(np.arange(10000).reshape(100, 100))



# # Basic Operations
#
# a = np.array([20, 30, 40, 50])
# print(a)
# b = np.arange(4)
# print(b)
# c = a - b
# print(c)
# print(b**2)
# print(10 * np.sin(a))
# print(a < 35)
#
# A = np.array([[1, 1],
#               [0, 1]])
# B = np.array([[2, 0],
#               [3, 4]])
# print(A * B)    # elementwise product
# print(A @ B)    # matrix product
# print(A.dot(B)) # another matrix product

rg = np.random.default_rng(1)
# a = np.ones((2, 3), dtype=int)
# b = rg.random((2, 3))
# print(a)
# a *= 3
# print(a)
# b += a
# print(b)
# # a += b    # b is not automatically converted to integer type

# a = np.ones(3, dtype=np.int32)
# b = np.linspace(0, np.pi, 3)
# print(b.dtype.name)
# c = a + b
# print(c)
# print(c.dtype.name)
# d = np.exp(c * 1j)
# print(d)
# print(d.dtype.name)

# a = rg.random((2, 3))
# print(a)
# print(a.sum())
# print(a.min())
# print(a.max())

# b = np.arange(12).reshape(3, 4)
# print(b)
# print(b.sum(axis=0))    # sum of each column
# print(b.min(axis=1))    # min of each row
# print(b.cumsum(axis=1)) # cumulative sum along each row



# # Universal Functions
# # https://numpy.org/devdocs/user/quickstart.html#universal-functions
# B = np.arange(3)
# print(B)
# print(np.exp(B))
# print(np.sqrt(B))
# C = np.array([2., -1., 4.])
# print(np.add(B, C))



# # Indexing, Slicing and Iterating
# a = np.arange(10)**3
# print(a)
# print(a[2])
# print(a[2:5])
# a[:6:2] = 1000
# print(a)
# print(a[::-1])
# for i in a:
#     print(i**(1 / 3.))

# def f(x, y):
#     return 10 * x + y
#
# b = np.fromfunction(f, (5, 4), dtype=int)
# print(b)
# print(b[2, 3])
# print(b[0:5, 1])    # each row in the second column of b
# print(b[:, 1])      # equivalent to the previous example
# print(b[1:3, :])    # each column in the second and third row of b
# print(b[-1])        # the last row. Equivalent to b[-1, :]
#
# c = np.array([[[0, 1, 2],           # a 3D array (two stacked 2D arrays)
#                [10, 12, 13]],
#                [[100, 101, 102],
#                 [110, 112, 113]]])
# print(c.shape)
# print(c[1, ...])                    # same as c[1, :, :] or c[1]
# print(c[..., 2])                    # same as c[:, :, 2]
#
# for row in b:
#     print(row)
#
# for element in b.flat:
#     print(element)



# # Shape Manipulation
# a = np.floor(10 * rg.random((3, 4)))
# print(a)
# print(a.shape)
#
# print(a.ravel())        # returns the array, flattened
# print(a.reshape(6, 2))  # returns the array with a modified shape
# print(a.T)              # returns the array, transposed
# print(a.T.shape)
# print(a.shape)
# a.resize((2, 6))
# print(a)
# print(a.reshape(3, -1))



# Stacking together different arrays
a = np.floor((10 * rg.random((2, 2))))
print(a)
b = np.floor(10 * rg.random((2, 2)))
print(b)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

