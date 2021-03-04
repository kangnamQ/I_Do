import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

#샘플의 개수는 300개, 센터(클러스터의 개수)는 4개,
# std = 중심점에서 얼마나 떨어져 있느냐, 랜덤 값 초기화
X, y_true = make_blobs(n_samples = 300, centers=4,
                       cluster_std=0.60, random_state=0)

#Scatter로 찍어보는 것 (단색으로 찍힘)
#s라고하는 것은 도트 사이즈
plt.scatter(X[:,0], X[:,1], s=50);


#4개로 하고 학습을 시킨다.
kmeans = KMeans(n_clusters = 4)
kmeans.fit(X)

#기존의 X라는 데이터로 predict를 해본다.
y_kmeans = kmeans.predict(X)

#그것을 바탕으로 컬러맵으로 점들을 다시 찍는다.
# c =  숫자에 따라서 컬러맵에 있는 컬러가 매핑이 되서 다시한번 점을 찍음.
plt.scatter(X[:,0],X[:,1], c=y_kmeans, s=50, cmap='viridis')


centers = kmeans.cluster_centers_
#센터를 200도트의 크리고 찍는 것이다.
plt.scatter(centers[:,0], centers[:,1], c='black', s=200, alpha=0.5);