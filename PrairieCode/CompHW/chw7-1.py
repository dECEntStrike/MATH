import numpy as np
import numpy.linalg as la

markov_matrix = np.array([[0.85, 0.2, 0.1, 0.05],
                        [0.05, 0.4, 0.1, 0.05],
                        [0.05, 0.1, 0.75, 0.25],
                        [0.05, 0.3, 0.05, 0.65]])
steady_state = np.array([0.85, 0.05, 0.05, 0.05])
for i in range(0,100):
    steady_state = markov_matrix @ steady_state
prob_stark = np.array([0.85, 0.05, 0.05, 0.05])
for i in range(0,2):
    prob_stark = markov_matrix @ prob_stark
    print(i)
prob_stark = prob_stark[1]