# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 06:18:33 2020

@author: kang
"""

"""
input : 학습 데이터 (x_1, d_1) ... (x_m, d_m)

모든 w들과 바이어스 b를 0 또는 작은 난수로 초기화 한다.
while (가중치가 변경되지 않을 때까지 반복)
    각 학습 데이터 x_k와 정답 d_k에 대하여
        y_k(t) = f (w * x)
        if d_k == y_k(t)
            continue
        else
            모든 가중치 wi에 대하여 wi(t+1) = w_i(t) + n * (d_k - y_k(t)) * xi_x
            여기서 n (에타) = 학습량 (보통 0.1)
            n * 오차


y = w_1 * x_1 + w_2 * x_2 + b
y = 0 이되는 선
