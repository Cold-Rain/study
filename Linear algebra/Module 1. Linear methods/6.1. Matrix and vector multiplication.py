'''
Найдите произведение матрицы A и вектора х в том порядке, в котором их можно умножить.
В качестве ответа запишите координаты получившегося вектора через запятую, без пробелов. Пример ввода ответа: 1,1.
'''
import numpy as np
A = np.array([[5,-1,3,1,2], [-2,8,5,-1,1]])
x = np.array([1,2,3,4,5])
print(np.dot(A,x))
#out [26 30] 
