import matplotlib.pyplot as plt 
import os

def reader(file):
    csv=open(file,"r")

    x=[]
    y=[]

    day=1
        
    for data in csv:
        data=data.replace(","," ")
        data=data.split()
        x.append(day)
        y.append(float(data[2]))
        day += 1

    plt.plot(x,y)
    plt.show()

files=os.listdir()
f1="market-price.csv"
f2="trade-volume.csv"


if f1 in files:
    print("1) for market-price chart")
if f2 in files:
    print("2) for trade-volumes chart")

choose=input("-->  ")

if choose == "1":
    reader(f1)

if choose == "2":
    reader(f2)

