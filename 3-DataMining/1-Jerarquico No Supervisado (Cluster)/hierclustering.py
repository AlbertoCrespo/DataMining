# -*- coding: utf-8 -*-


import codecs
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import numpy
import csv


#http://docs.scipy.org/doc/scipy/reference/cluster.html
from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors
from sklearn.decomposition import PCA


print("1-7 Cargando Datos....")

# 0. Load Data
f = codecs.open("BD.csv", "r", "utf-8")
states = []
count = 0
for line in f:
	if count > 0: 
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0)
		if row != []:
			data = [int(el) for el in row]
			states.append(data)
	count += 1

 
print("2-7 Normalizando Datos.....")
#1. Normalization of the data
#http://scikit-learn.org/stable/modules/preprocessing.html
min_max_scaler = preprocessing.MinMaxScaler()
states = min_max_scaler.fit_transform(states)

print("3-7 Estimador del PCA...")
#2. PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(states)

print("4-7 Matriz de similitud...")
# 2. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(states)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Distancia Media', avSim)

print("5-7 Construyendo Dendograma...")
# 3. Building the Dendrogram	
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
clusters = cluster.hierarchy.linkage(matsim, method = 'ward')
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.cluster.hierarchy.dendrogram.html
cluster.hierarchy.dendrogram(clusters, color_threshold=0)
plt.show()

cut = float(input("Threshold cut:"))
#cut = float(1250)

print("6-7 Haciendo Cluster Jerarquico...")
labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Number of clusters %d' % (len(set(labels)))


print("7-7 Escribiendo los datos...")
reader = csv.reader(open('BD.csv', 'rb'))
archivo=open ("BDC.csv","a")


x = 0
y = 0

for index,row in enumerate(reader):
	if x == 0:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+",Grupo")
		archivo.write("\n")
		x = x + 1
	else:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(labels[y]))
		archivo.write("\n")
		y = y +1

archivo.close()


