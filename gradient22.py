from __future__ import division, print_function, unicode_literals
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
# create data
np.random.seed(2)
x = np.random.rand(1000, 1)
#print(len(x))
# create x bar
ones = np.ones((1000,1))
xbar = np.concatenate((ones,x), axis=1)
# create funtion
y = 3*x + 4 + 0.1*np.random.rand(1000,1)
# y = np.zeros(shape=(1000,1))
# for i in range(len(x)):
#     for k in range(3):
#         if k==0:
#              y[i] += 3*x[i][k] + 4 + 0.5*np.random.rand()
#         elif k==1:
#             y[i] += 10*x[i][k] + 4 + 0.5*np.random.rand()
#         else:
#             y[i] += 5*x[i][k] + 4 + 0.5*np.random.rand()
#for directively
# A = np.dot(xbar.T,xbar)
# w = np.dot(np.dot(y.T,xbar),np.linalg.pinv(A))
# for Gradient descent
#create funtion Gradient
def grad_22(w,x,y):
    grad = -np.dot(y.T,x) + np.dot(w,np.dot(x.T,x))
    return grad
# create initiate
w = 5*np.random.rand(2,1)
def myGrad(w0,eta):
    w = w0
    for i in range(500):
        w = w - eta*grad_22(w,xbar,y)
        if abs(np.dot(grad_22(w,xbar,y).T,grad_22(w,xbar,y))) <= 1e-3:
            break
    return w

w0 = 10*np.random.rand(2,1)
myGrad(w0,0.1)
# plt.plot(x,y,'b.')
# # # plt.axis([0,1,0,10])
# plt.show()

