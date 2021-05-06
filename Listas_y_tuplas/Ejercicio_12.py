

vec_1 = [1, 2, 3]
vec_2 = [4, 5, 6]
vec_3 = [-1, 0, 1]
vec_4 = [0, 1, 1]
num1 = 0
num2 = 0
num3 = 0
num4 = 0

for i in range(len(vec_1)):
    num1 += vec_3[i] * vec_1[i]
    num2 += vec_3[i] * vec_2[i]
    num3 += vec_4[i] * vec_1[i]
    num4 += vec_4[i] * vec_2[i]

C = [[num1, num3], [num2, num4]]
print(C)