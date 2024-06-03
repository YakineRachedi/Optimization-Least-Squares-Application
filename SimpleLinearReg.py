import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)


#Exercice 1 : cas 1d on cherche à estimier la résistance de la loi d'OHM R = UI

# Pour cela on fait un ajustement linéaire sur les données (Ui,Ii) pour laquelle on applique la méthode des moindres carrées 
# donc on cherche une solutiion du probleme d'optimisation (voir la fueille) et on cherche R optimale pour qu'il soit proche à R théorique

R_theorique = 0.0168   #à modifier !


n = 10  # nombre de données

# Générer n valeurs d'intensité aléatoires entre 0 et 1 ampère
I_intensites = np.random.rand(n)
#print("Les 10 valeurs d'intensité générées sont :", I_intensites)

U_tensions = R_theorique * I_intensites  #ensemble des données initiales (on suppose qu'ils sont exacts)
#print("Les valeurs de la tension sont : ",U_tensions)

sigma = np.var(U_tensions) # variance des données

# régression linaire affine :
U_bruit = U_tensions + sigma * np.random.rand(n)  #répétition de l'expérience plusieurs fois + l'erreur de bruit
#print("les valeurs de la tension à estimier sont : ", U_estimer)

# calcul de R optimale le min apres justifier l'existence (dans la feuille)
R_opt = (np.dot(I_intensites,U_tensions) / np.linalg.norm(I_intensites) ** 2) 
print("la solution du probleme d'optimisation des moindres carrées, le R optimale est : ",R_opt)

# R_opt est présque R_th :)
plt.figure(figsize=(8, 6))
plt.plot(U_tensions,I_intensites,'ro',label = "Données initiales")
plt.plot(U_bruit,I_intensites,'-b*',label = "Données avec l'erreur de bruit")
plt.legend()
plt.grid(True)
plt.xlabel("Intensities")
plt.ylabel("Ensemble des données")
plt.title("Regression linaire 1D d'un probleme d'optimisaiton des moindres carrées des donnes (I,U)")
plt.show()


""" 
Nuage de points par scatter :
plt.scatter(U_tensions,I_intensites,color = 'r')
plt.scatter(U_bruit,I_intensites,color ='b') 
"""