# -*- coding: utf-8 -*-
"""

"""
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def pprint(array, say='info'):
    print("shape: {}, dimension:{}, dtype:{}".format(array.shape, array.ndim, array.dtype))
    print(say)
    print(array)
    print("")

def make_list(sart_range='10', end_range='10', how_many='10'):    
    make_range = np.random.randint(sart_range, end_range, size = how_many)
    return make_range

def merge_list(list1, list2):
    merge = []
    for n in range(len(list1)):
        line = []
        for i in range(1):
            line.append(list1[n])
            line.append(list2[n])
        merge.append(line)
    return merge
 
def make_sample(sart_range='10', end_range='100', how_many='10'):
    x = make_list(sart_range,end_range,how_many)
    y = make_list(sart_range,end_range,how_many)
    z = merge_list(x, y)
    X = np.array(z)
    print(z)
    return X
    
    
#------------------------

red = make_sample(0,50,5)
blue = make_sample(50,100,5)

#path=scatter(x, y, s=None(크기), c=None(색))
RED = scatter = plt.scatter(red[:,0],red[:,1], s=40,  cmap='red')
BLUE = plt.scatter(blue[:,0],blue[:,1], s=40,  cmap='blue')
plt.title('Class', fontsize=15)

plt.show()


"""
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print(kmeans.cluster_centers_)

print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')




# 샘플과 레이블이다. 
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0, 0, 0, 1]

# 퍼셉트론을 생성한다. tol는 종료 조건이다. random_state는 난수의 시드이다.
clf = Perceptron(tol=1e-3, random_state=0)

# 학습을 수행한다. 
clf.fit(X, y)

# 테스트를 수행한다. 
print(clf.predict(X))
"""
