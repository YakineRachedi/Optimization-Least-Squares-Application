import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
np.random.seed(7)

# fonction qui renvoi un polynome de degré - 1
def polynome(coeff,variable,degre):
    P_x = 0
    for i in range(degre):
        P_x += coeff[i] * variable ** i
    return P_x

# Données initiales
p = 6
a = np.random.rand(p)  #vecteur de R^6
n = 10
Intensities = np.random.random(n)   #valeurs de xi
sigma = np.var(Intensities)
U_theorique = polynome(a, Intensities, p)  #tension théorique : Polynome associé au vecteur a

U_bruit = U_theorique + np.random.normal(0 , sigma * sigma, n)   # Données bruits

# création de la matrice des données n lignes p colones
X = np.zeros((n , p))  

for i in range(n):
    for j in range(p):
        X[i,j] = Intensities[i] ** j

# calcul de la solution du probleme d'optimisation :
a_opt = np.dot(inv(X.T @ X) @ X.T, U_bruit)
print('a_opt ===>',a_opt)
# création des polynomes d'ajustement :
x = np.linspace(0,1,100)
for i in range(1,p+1):
    P_x = polynome(a_opt,x, i)
    print("Polynome de degré : ",i)
    print(P_x)
    plt.plot(x, P_x, label = f"polynome de degré {i}")
plt.plot(Intensities, U_theorique, 'ro',label = "Données initiales")
plt.legend()
plt.grid(True)
plt.show()    