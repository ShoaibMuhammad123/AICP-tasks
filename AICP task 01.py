import numpy as np

#Question no 1: Write a NumPy program to create an array of all even integers from 30 to 70

even_integer_30_to70 = np.arange(30,70,2)

print(even_integer_30_to70)

# Question no 2: Write a NumPy program to generate an array of 15 random numbers from a
# standard normal distribution.

numbers_15_random = np.random.normal(0,1,15)
print(numbers_15_random)



# Question no 3: How to compute the cross-product of two matrices in NumPy?
matrix1 = np.array([[20,30,33],[55,23,66]])

matrix2 = np.array([[13,53,75],[5,3,24]])

cross_product = np.cross( matrix1 , matrix2 )

print(cross_product)


# Question no 4: How to Compute determinant of an array using Numpy.

arr = np.array([[3,4],[3,8]])
det_value = np.linalg.det(arr)
print(det_value)


# Question no 4: How to create 3x3x3 arrays with random values using numpy
matrix_3x3x3 = np.random.randint(1,28,27).reshape(3,3,3)

print(matrix_3x3x3)


# Question no 5: How to create a 5x5 array with random values and find the minimum and
# maximum values using NumPy?
Arr = np.random.random(25).reshape(5,5)*100
print(Arr)


# Question no 6: How to compute the mean, standard deviation, and variance of
# a given array along the second axis in NumPy?
Array = np.array([[34,56,64],[32,16,62],[55,42,4]])
mean = np.mean(Array,axis = 1)
print(mean)

std = np.std(Array,axis = 1)
print(std)

var = np.var(Array,axis = 1)
print(var)

