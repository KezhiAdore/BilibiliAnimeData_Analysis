import numpy as np
import pandas as pd
import math
import random
import copy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 对播放量，追番数，弹幕数进行数值压缩
def trans_data(data):
    for index,item in enumerate(data):
        data[index]=math.log(item)
    Max=max(data)
    Min=min(data)
    for index,item in enumerate(data):
        data[index]=(item-Min)/(Max-Min)

# 计算数据距离，返回坐标矩阵
def get_dire(filepath):
    df=pd.read_csv(filepath)
    barrage,follow,play=df['barrage'].to_list(),df['follow'].to_list(),df['play'].to_list()
    trans_data(barrage)
    trans_data(follow)
    trans_data(play)
    result=[barrage,follow,play]
    return list(map(list, zip(*result)))

# 计算欧氏距离
def distance(point1,point2):
    dim=len(point1)
    if dim != len(point2):
        print('error! dim of point1 and point2 is not same')
    dist=0
    for i in range(dim):
        dist+=(point1[i]-point2[i])*(point1[i]-point2[i])
    return math.sqrt(dist)

# 以给定的k个点为中心进行分类
def get_category(dire,k,k_center):
    shape=np.array(dire).shape
    k_categories=[[] for col in range(k)]
    for i in range(shape[0]):
        Min=1
        for j in range(k):
            dist=distance(dire[i],k_center[j])
            if dist<Min:
                Min=dist
                MinNum=j
        k_categories[MinNum].append(i)
    return k_categories

def show_k_means(k_result):
    k,k_categories,dire=k_result['k'],k_result['k_categories'],k_result['dire']
    for i in range(k):
        x,y,z=[],[],[]
        for index in k_categories[i]:
            x.append(dire[index][0])
            y.append(dire[index][1])
            z.append(dire[index][2])
        fig = plt.gcf()
        ax = fig.gca(projection='3d')
        ax.scatter(x,y,z)
    plt.show()

def k_means(dire,k):
    # 随机选取k个点作为中心
    shape=np.array(dire).shape
    k_center_index=[]
    k_center=[]
    temp_k=k
    while(temp_k):
        temp=random.randrange(0,shape[0])
        if temp not in k_center_index:
            k_center_index.append(temp)
            k_center.append(list(dire[temp]))
            temp_k-=1

    # 最大迭代次数
    Maxloop=500
    k_center_new=k_center
    k_center=[]
    count=0
    while(k_center!=k_center_new and count<Maxloop):
        count+=1
        k_center=copy.deepcopy(k_center_new)
        k_categories=get_category(dire,k,k_center_new)
        for i in range(shape[1]):
            for j in range(k):
                temp=0
                for w in k_categories[j]:
                    temp+=dire[w][i]
                if len(k_categories[j])!=0:
                    k_center_new[j][i]=temp/len(k_categories[j])
    return {'k_center':k_center,'k_categories':k_categories,'dire':dire,'k':k}

def dbi(k_result):
    k_center,k_categories,dire,k=k_result['k_center'],k_result['k_categories'],k_result['dire'],k_result['k']
    # 簇内平均距离
    k_ave_dist=[0 for index in range(k)]
    for i in range(k):
        temp=0
        for item in k_categories[i]:
            temp+=distance(k_center[i],dire[item])
        k_ave_dist[i]=temp/len(k_categories[i])
    # 簇中心之间距离
    k_center_dist=[[0 for row in range(k)] for col in range(k)]
    for i in range(k):
        for j in range(k):
            k_center_dist[i][j]=distance(k_center[i],k_center[j])
    # 计算dbi
    DB=0
    for i in range(k):
        Max=0
        for j in range(k):
            if i !=j:
                temp=(k_ave_dist[i]+k_ave_dist[j])/k_center_dist[i][j]
                if temp>Max:
                    Max=temp
        DB+=Max
    return DB/k



if __name__ == "__main__":
    data=get_dire('data_processed.csv')
    # show_k_means(k_means(data,10))
    DBI=[]
    for i in range(2,50):
        k_result=k_means(data,i)
        DBI.append(dbi(k_result))
        print(DBI[-1])
    plt.plot(DBI)
    plt.show()
