import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

# Données :
x = np.array([-2.6605, -2.5024, -2.4075, -2.0656, -1.2418, -1.1105, -1.0194,
-0.8459, -0.8403, -0.4906, 0.7695, 0.8933, 1.0023, 1.5085, 2.3193])
y =np.array([ 97.1414, 80.8250, 72.0406, 46.0602, 12.0776, 9.4146, 7.8925,
5.6353, 5.5751, 3.0525, -0.3093, -1.3142, -2.4258, -11.0032, -39.9284])

# on utilise la méthode des moindres carrées pour approcher ces données

n = len(y)
def Polynome(coeff,var,deg):
    P_x = 0
    for i in range(deg):
        P_x += coeff[i] * var ** i
    return P_x

degre = [1, 2, 3, 4, 5, 6]
courbe_erreur = []
for p in degre:
    A = np.zeros((n, p+1))
    for i in range(n):
        for j in range(p):
            A[i,j] = x[i] ** j

    coeff_opt = np.linalg.pinv(A) @ y
    pol = Polynome(coeff_opt, x, p)
    plt.plot(x,pol,label=f"polynome de degré {p}")
    # erreur :
    erreur = np.linalg.norm(pol - y)**2
    courbe_erreur.append(erreur)
plt.scatter(x,y,label = "nuage des points",s=50)
plt.grid(True)
plt.legend()
plt.show() 
plt.plot(np.arange(1,7),courbe_erreur)
plt.xlabel("erreur pour chaque degré de polynome")
plt.ylabel("courbe d'erreur")
plt.legend()
plt.grid(True)
plt.show()


"""
 Création d'une fonction pour ajuster un polynôme de degré n aux données
def fit_polynomial(x, y, degree):
    coefficients = np.polyfit(x, y, degree)  # Coefficients du polynôme
    polynomial = np.poly1d(coefficients)     # Polynôme à partir des coefficients
    return polynomial

# Tracer les données et les ajustements polynomiaux
plt.figure(figsize=(12, 8))
plt.scatter(x, y, label='Données réelles')

for degree in range(1, 7):
    polynomial = fit_polynomial(x, y, degree)
    plt.plot(x, polynomial(x), label=f'Degré {degree}')


"""