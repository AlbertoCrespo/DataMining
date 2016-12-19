# -*- coding: utf-8 -*-

# function for plotting
from matplotlib.colors import ListedColormap
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import csv


#Reading the initial data
df = pd.read_csv('BDC.csv')

y = targets = labels = df["Grupo"].values

columns = ['Vehi_Comercial','Tipo_de_Vehiculo','Anio','Marca','Modelo']
clases = ['1','2','3']
features = df[list(columns)].values



from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(features)

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=5)
clf = clf.fit(X, y)


# 3. Plot the decision tree: 
# http://nbviewer.jupyter.org/github/kittipatkampa/python_dev/blob/master/demo_decision_tree_v1.ipynb
from sklearn.externals.six import StringIO  
import pydot 

# It is necessary to install GraphViz
# http://www.graphviz.org/Download..php
# PATH = C:\Program Files (x86)\Graphviz2.38\bin\:$PATH$


# Extract the decision tree logic from the trained model
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data
						,feature_names=columns,
						 class_names=clases,    
                         filled=True, rounded=True,  
                         special_characters=True)


# convert the logics into graph
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 

## This will plot decision tree in pdf file
graph.write_pdf(path="Arbol.pdf")