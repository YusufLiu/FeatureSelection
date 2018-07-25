# FeatureSelection
By exploring different algorithms, create a new innovated feature selection algorithm. In order to solve a specific problem, models should be built accordingly. However, the selection of features for modelling is a complicated and time consuming problem, since it is hard to predict which features we need to look at in the problem. The feature selection is the process that automatically form a subset of features that most relevant to the project and prepare the data for further processing.
## Motivation
The pure ant colony optimization (ACO) was able to achieve a high accuracy solution with a stunning running time (lower than other searching methods). However, the pure ant colony optimization lacked some domain specific information for the problem of feature selection, and that is the goal is the reduce the number of features selected while maximizing the accuracy. Another search algorithm could be topped thus to find the most proper initial settings for ACO. Simulated Annealing is chosen because it obtains great randomness in the search space.
## Tools
Python 2.7 

numpy : math library, performs ops on arrays.

pandas : library, data manipulation and analysis

scikit-learn : ML library 
## Dataser Reference
Iris: 
https://www.kaggle.com/uciml/iris

Breast Cancer Wisconsin (Diagnostic):
https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

Communities and Crime:
http://archive.ics.uci.edu/ml/datasets/Communities+and+Crime
## How to use:
The final solution is called SA-WACO, which is a combination of SA and ACO algorithm. It uses SA to tune parametures of ACO to obtain higher performance on feature selction problem.

install python

run main.py

options:
In main.py, datasets could be chosen by uncommenting lines for csv import. Defaultly, the final solution, SA-WACO, is enabled.

To run other solutions, such as GA, SA, ACO, BFS, uncomment relavent parts.
## Project Contributors:
YuCheng Liu, 
Tian Zhu, 
Cong Hao He, 
Yiran Tian
## Contact Information:
t27zhu@edu.uwaterloo.ca
