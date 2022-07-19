# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from cmath import pi

# вычисление через формулу Лейбница

print(pi)
n = 5000000
pi_result = 4 * sum((-1.)**k / (2*k + 1) for k in range(n))
print("{0:.3f}".format(pi_result)) 
