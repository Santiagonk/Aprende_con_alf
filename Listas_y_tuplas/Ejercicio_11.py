vec_1 = [1, 2, 3]
vec_2 = [-1, 0, 2]
producto = 0

for i in range(len(vec_1)):
    producto += vec_1[i] * vec_2[i]
    
print(f'el producto escalar es {producto}')