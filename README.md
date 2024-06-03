French version :
# Méthode des moindres carrés pour l'ajustement de données

La méthode des moindres carrés est utilisée lorsque l'on souhaite ajuster une fonction à un ensemble de données. Plus précisément, nous considérons une famille de fonctions \( F \) dont les éléments \( f_a \) dépendent d'un paramètre \( a \) appartenant à \( \mathbb{R}^d \). Par exemple,

\[ F = \{ f_a : \mathbb{R} \rightarrow \mathbb{R}; x \mapsto ax \} \]

est l'ensemble des fonctions linéaires paramétrées par un paramètre réel \( a \in \mathbb{R} \).

Nous disposons d'un ensemble de points de données \( \{(x_i, y_i)\}_{1 \leq i \leq n} \) tels que

\[ \forall i \in \{1, \ldots, n\}, \quad y_i = f_{a_0}(x_i) + \epsilon_i \]

où \( x_i \in \mathbb{R}^p \) et \( y_i \in \mathbb{R} \) pour un certain paramètre \( a_0 \). La présence de \( \epsilon_i \) peut être due au bruit d'acquisition (arrondi numérique, erreur ou imprécision) et/ou à l'approximation dans la modélisation.

Dans de nombreuses applications, nous cherchons à trouver la meilleure fonction de \( F \) qui modélise la génération de données. Autrement dit, étant donné l'ensemble de données \( u = \{(x_i, y_i)\}_{1 \leq i \leq n} \), quelle est la fonction \( f_a \in F \) pour laquelle le nuage de points \( v_{f_a} = \{(x_i, f_a(x_i))\}_{1 \leq i \leq n} \) correspond le mieux aux données initiales \( u \)?

Ces deux ensembles de points appartiennent à un espace euclidien, donc nous pouvons mesurer la distance entre eux en utilisant la distance de Frobenius, écrite comme

\[ \| v_{f_a} - u \|_F = \sum_{i=1}^{n} \| f_a(x_i) - y_i \|_2^2 \]

Le problème d'ajustement peut ainsi être écrit sous la forme de problème d'optimisation suivant :

\[ \min_{f_a \in F} \sum_{i=1}^{n} \| f_a(x_i) - y_i \|_2^2 \]

ce qui revient à minimiser l'erreur quadratique moyenne entre les données \( y_i \) et le modèle théorique \( f_a(x_i) \) ; d'où le nom "méthode des moindres carrés". Puisque la famille \( F \) est paramétrée par le vecteur \( a \in \mathbb{R}^d \), la forme finale du problème d'ajustement devient

\[ \min_{a \in \mathbb{R}^d} \sum_{i=1}^{n} \| f_a(x_i) - y_i \|_2^2 \].

