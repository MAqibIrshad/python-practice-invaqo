import numpy as np

arr = np.array([
    10, 20, 30, 40, 50
])

#using min max normalization

norm = (arr - arr.min()/(arr.max()-arr.min()))

print(norm)

mean = norm.mean()
print(mean)

mask = norm > mean
print(mask)

result = norm[mask]