#import used libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv('Upwork.csv')
#split data into two dataframes , S and E
df_s = df[df['P'] == 'S']
df_e = df[df['P'] == 'E']
print(df_s.head())
print(df_e.head())
#needed for plotting
x = [1,2,4,8,16]
y1 = dict()
y2 = dict()

# extracting y1 and y2 from dataframes
for _type in df_s['Type']:
    data = []
    for i in x:
        num = df_s[df_s['Type'] == _type].loc[:,str(i)].values.tolist()[0]
        data.append(num)
    y1[_type] = data 

for _type in df_e['Type']:
    data = []
    for i in x:
        num = df_e[df_e['Type'] == _type].loc[:,str(i)].values.tolist()[0]
        data.append(num)
    y2[_type] = data 


#creating the plots side by side "Subplots"
figure,axis = plt.subplots(1,2,figsize=(10,5))

axis[0].plot(x,y1["Half"],linestyle = 'dotted',label = 'Half')
axis[0].plot(x,y1["Original"])
axis[0].plot(x,y1["Double"],linestyle = 'dashed',label = 'Double')
axis[0].legend(['Half','Original','Double'])

axis[1].plot(x,y2["Half"],linestyle = 'dotted',label = 'Half')
axis[1].plot(x,y2["Original"])
axis[1].plot(x,y2["Double"],linestyle = 'dashed',label = 'Double')
axis[1].legend(['Half','Original','Double'])

#Creating The Processes - Speed Up Graph
plt.figure(2)
plt.xlabel("Processes")
plt.ylabel('Speedup')
plt.plot(x,y1["Half"],linestyle = 'dotted',label = 'Half')
plt.plot(x,y1["Original"])
plt.plot(x,y1["Double"],linestyle = 'dashed',label = 'Double')
plt.legend(['Half','Original','Double'])

#Creating The Processes - Efficiency Graph
plt.figure(3)
plt.xlabel('Processes')
plt.ylabel('Efficiency')
plt.title("Efficiencies of parallel program on different problem sizes")
plt.plot(x,y2["Half"],linestyle = 'dotted',label = 'Half')
plt.plot(x,y2["Original"])
plt.plot(x,y2["Double"],linestyle = 'dashed',label = 'Double')
plt.legend(['Half','Original','Double'])



