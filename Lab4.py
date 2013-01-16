'''
Created on Nov 19, 2012

@author: Nat Troyer
'''
from matplotlib import pyplot as plt
from numpy import *
import numpy.random as rand
import numpy as np
import math

def loadBalancer(n):
    lines = [0]*n
    for i in range (0, n):
        cust = rand.randint(0,n)
        lines[cust] = lines[cust] + 1   
    return max(lines)
     
def num7():
    arr=[]
    arr2 = []
    count = 0
    for j in range (2, 501):   
        count = 0 
        for i in range (0, 1000):
            maxLin = loadBalancer(j)
            count = maxLin + count
        answer = count/1000.0
        arr.append(answer)
        eq = (3*np.log(j))/(np.log(np.log(j)))
        arr2.append(eq)
    plt.figure(1)
    plt.title("Load Balancing Graph for loadbalancer")
    plt.xlabel("Number of people")
    plt.ylabel("Avg. Max Line")
    plt.plot(range(2,501),arr)
    plt.plot(range(2,501),arr2, 'r--')
    plt.show() 

num7()

def modloadbalancer(n, d):
    lines = [0]*n
    for i in range (0, n):
        huehue = rand.randint(0,n)
        for j in range (0, d-1):
            cust = rand.randint(0,n)
            if lines[huehue] > lines[cust]:
                huehue = cust
        lines[huehue] = lines[huehue] + 1   
    return max(lines)

def num10():
    arr=[]
    arr2=[]
    for j in range (2, 11):   
        count = 0 
        for i in range (0, 1000):
            maxLin = modloadbalancer(1000, j)
            count = maxLin + count
        answer = count/1000.0
        arr.append(answer)
        eq = (math.log(math.log(1000))/(math.log(j))+1)
        arr2.append(eq)
    plt.figure(1)
    plt.title("Load Balancing Graph for modloadbalancer")
    plt.xlabel("Number of people")
    plt.ylabel("Avg. Max Line")
    plt.plot(range(2, 11), arr)
    plt.plot(range(2, 11), arr2, 'r--')
    plt.show()
    
num10()

def resetPaths():
    paths = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    return paths
'''
Generates packets and "sends" them by calling naiveRoute or valiantRoute. 
@param numnPackets the number of packets to generate and send. 
@param valiant a boolean variable specifying which kind of routing to use.
@param paths the paths upon which packete transmission occurs. At the beginning              run resetPaths() to initialize them.

'''
def sendPackets(numPackets, valiant, paths):
    for i in range (0, numPackets):
        dubz = ((rand.randint(0,6)), (rand.randint(0,6)))
        if valiant:
            valiantRoute(dubz, paths)
        else:
            naiveRoute(dubz, paths)
    return paths

'''
Routes according to the most direct path - a,b.
Add 1 to the index of the path every time route is called
'''
def naiveRoute((a,b), paths):
    if b < a :
        temp = a
        a = b
        b = temp
    if not(a==b):    
        paths[a][b] += 1
    return paths

'''
Routes according to the Valiant Routing policy defined in the lab - first take a random hop
then route to destination
'''
def valiantRoute((a,b), paths):
    d = rand.randint(0,6)
    while d == a:
        d = rand.randint(0,6)
        
    if d == b:
        naiveRoute((a,d),paths)
    else:
        naiveRoute((a,d), paths)
        naiveRoute((d,b), paths)
    return paths

def avgNonZero(paths):
    total = 0
    counted = 0
    for i in range (0, 6):
        for j in range(0,6):
            if not(paths[i][j]==0):
                total += paths[i][j]
                counted += 1 
    return total*1.0 / counted

def num17():
    print avgNonZero(sendPackets(1000, True, resetPaths()))

def num18best():
    bestPacksNaive = [0]*1000
    bestPacksValiant = [0]*1000
    for i in range(0, 1000):
        bestPacksNaive[i] = avgNonZero(sendPackets(1000, False, resetPaths()))
        bestPacksValiant[i] = avgNonZero(sendPackets(1000, True, resetPaths()))
    
    plt.figure(1)
    plt.title("Laod Balancer Graph for Random Routing")
    plt.xlabel("Simulations")
    plt.ylabel("Avg. Num of Packets")
    plt.plot(range(0, 1000), bestPacksNaive)
    plt.plot(range(0, 1000), bestPacksValiant)
    plt.show()
    
def num18worst():
    worstPacksNaive = [0]*1000
    for i in range(0, 1000):
        worstPacksNaive[i] = avgNonZero(worstPackets(1000, False, resetPaths()))
    
    worstPacksValiant = [0]*1000
    for i in range(0, 1000):
        worstPacksValiant[i] = avgNonZero(worstPackets(1000, True, resetPaths()))
    
    plt.figure(1)
    plt.title("Load Balancer Graph for when all traffic starts at router A")
    plt.xlabel("Simulations")
    plt.ylabel("Avg. Num of Packets")
    plt.plot(range(0, 1000), worstPacksNaive)
    plt.plot(range(0, 1000), worstPacksValiant)
    plt.show()
    
def num18worstworst():
    worstworstPacksNaive = [0]*1000
    for i in range(0, 1000):
        worstworstPacksNaive[i] = avgNonZero(worstworstPackets(1000, False, resetPaths()))
    
    worstworstPacksValiant = [0]*1000
    for i in range(0, 1000):
        worstworstPacksValiant[i] = avgNonZero(worstworstPackets(1000, True, resetPaths()))
    
    plt.figure(1)
    plt.ylim(100, 1100)
    plt.title("Load Balancer Graph for when all traffic starts at A and ends at B")
    plt.xlabel("Simulations")
    plt.ylabel("Avg. Num of Packets")
    plt.plot(range(0, 1000), worstworstPacksNaive)
    plt.plot(range(0, 1000), worstworstPacksValiant)
    plt.show()
    
def worstPackets(numPackets, valiant, paths):
    for i in range (0, numPackets):
        dubz = ((0), (rand.randint(0,6)))
        if valiant:
            valiantRoute(dubz, paths)
        else:
            naiveRoute(dubz, paths)
    return paths

def worstworstPackets(numPackets, valiant, paths):
    for i in range (0, numPackets):
        dubz = ((0), (1))
        if valiant:
            valiantRoute(dubz, paths)
        else:
            naiveRoute(dubz, paths)
    return paths
        
num17()
num18best()
num18worst()
num18worstworst()