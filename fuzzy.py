import numpy as np

a = np.array([2,5,6,9])
b = np.array([8,2,5,6])

# Union
union = np.maximum(a, b)
print("Union:", union)

# Intersection
intersection = np.minimum(a, b)
print("Intersection:", intersection)

# Complement of A
complement = 1 - a
print("Complement of A:", complement)

# Difference (A - B)
difference = np.maximum(a, 1 - b)
print("Difference (A - B):", difference)

# Cartesian Product
cartesian_product = np.array([[np.minimum(i, j) for j in b] for i in a])
print("Cartesian Product:\n", cartesian_product)

# Max-Min Composition
c = np.array([[2,4], [4,6], [9,1]])
d = np.array([[5,3,2], [9,5,2]])

if c.shape[1] == d.shape[0]:
    max_min_comp = np.array([[np.max(np.minimum(i, j)) for j in d.T] for i in c])
    print("Max-Min Composition:\n", max_min_comp)
else:
    print("Matrix dimensions incompatible")