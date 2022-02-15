#import needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_Tserial(n):
    Tserial = pow(n,2)
    return Tserial

def get_Tparallel(n,p):
    Tparallel = (pow(n,2)/p) + np.log2(p)
    return Tparallel
    
n = []
p = []

initial_n = 10
initial_p = 1

while(initial_n <= 320):
    n.append(initial_n)
    initial_n *= 2
    
while(initial_p <= 128):
    p.append(initial_p)
    initial_p *= 2
    
# What Happens to speed up and efficiency when p increase and n is fixed?
#p increase , n is fixed
def case_1(n,p):
    Tserial_dict = dict()
    Tparallel_dict = dict()
    Speed_up_dict = dict()
    Efficiency_dict = dict()
    
    #iterator
    for n_value in n:
        for p_value in p:
            key = str(n_value) + '_' + str(p_value) # initialize our key
            Tserial_dict[key] = get_Tserial(n_value) # get the serial time on Tserial = n^2
            Tparallel_dict[key] = get_Tparallel(n_value,p_value) # get the parallel time on Tparallel = (n^2/p) + log2(p)
            Speed_up_dict[key] = Tserial_dict[key]/Tparallel_dict[key] # S = TSerial / Tparallel
            Efficiency_dict[key] = Speed_up_dict[key]/p_value # E = S / p
    
    return Tserial_dict,Tparallel_dict,Speed_up_dict,Efficiency_dict

#tuple return
Tserial_dict_1,Tparallel_dict_1,Speed_up_dict_1,Efficiency_dict_1 = case_1(n,p)
#print("Hello World")
# What Happens to speed up and efficiency when n increase and p is fixed?
def case_2(n,p):
    Tserial_dict = dict()
    Tparallel_dict = dict()
    Speed_up_dict = dict()
    Efficiency_dict = dict()
    for p_value in p:
        for n_value in n:
            key = str(n_value) + '_' + str(p_value)
            Tserial_dict[key] = get_Tserial(n_value)
            Tparallel_dict[key] = get_Tparallel(n_value,p_value)
            Speed_up_dict[key] = Tserial_dict[key]/Tparallel_dict[key]
            Efficiency_dict[key] = Speed_up_dict[key]/p_value
    
    return Tserial_dict,Tparallel_dict,Speed_up_dict,Efficiency_dict

Tserial_dict_2,Tparallel_dict_2,Speed_up_dict_2,Efficiency_dict_2 = case_2(n,p)

#print("Hello World")

# graphing the answers
#case 1 , p increase , n is fixed
figure,axis = plt.subplots(1,2,figsize=(15,20))

X = p
for n_value in n:
    Y = []
    for p_value in p:
        key = str(n_value) + '_' + str(p_value)
        Y.append(Speed_up_dict_1[key])
    axis[0].plot(X,Y,label=str(n_value),marker = "o")

axis[0].legend(n)
axis[0].set_xlabel('P')
axis[0].set_ylabel('Speed Up')
axis[0].set_title('(fixed n , p increase) - Speed up')

for n_value in n:
    Y = []
    for p_value in p:
        key = str(n_value) + '_' + str(p_value)
        Y.append(Efficiency_dict_1[key])
    axis[1].plot(X,Y,label=str(n_value),marker = "o")
axis[1].legend(n)
axis[1].set_xlabel('P')
axis[1].set_ylabel('Efficiency')
axis[1].set_title('(fixed n , p increase) - Efficiency')

#case 2 , n increase , p is fixed
figure,axis = plt.subplots(1,2,figsize=(20,15))
X = n
for p_value in p:
    Y = []
    for n_value in n:
        key = str(n_value) + '_' + str(p_value)
        Y.append(Speed_up_dict_1[key])
    axis[0].plot(X,Y,label=str(p_value),marker = "o")

axis[0].legend(p)
axis[0].set_xlabel('n')
axis[0].set_ylabel('Speed Up')
axis[0].set_title('(fixed p , n increase) - Speed up')

for p_value in p:
    Y = []
    for n_value in n:
        key = str(n_value) + '_' + str(p_value)
        Y.append(Efficiency_dict_1[key])
    axis[1].plot(X,Y,label=str(p_value),marker = "o")

axis[1].legend(p)
axis[1].set_xlabel('n')
axis[1].set_ylabel('Efficiency')
axis[1].set_title('(fixed p , n increase) - Efficiency')

print("Hello World")