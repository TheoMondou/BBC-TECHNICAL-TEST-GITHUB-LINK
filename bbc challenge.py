# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:26:31 2019

@author: Mondou
"""
from random import*
#Parametres that can be modified
N=10                    #for a N*N grid
Beginning=False          #True if the grid is randomly filled, False if not (there is a configuration with a line of three living cells)
Numberiterations=100
Cyclic=False           #True if the N-1 case is next to the 0 case, false if not



Life=[[0 for i in range (0,N)] for j in range (0,N)]   #1 for live, 0 if not
Neighbours=[[0for i in range (0,N)] for j in range (0,N)]   #count the number of neighbours


def Affiche():
    for k in range (0,N) :
        print Life[k]

def Initialize():
    if Beginning==True :
        for i in range (0,N) :
            for j in range (0,N) :
                Life[i][j]=randint(0,1)
    else :
        if N>3 :
            Life[1][0]=1
            Life[1][1]=1
            Life[1][2]=1

def Iteration():
    for i in range (0,N) :
        for j in range (0,N) :
            if Neighbours[i][j]<2:
                Life[i][j]=0
            if Neighbours[i][j]>3:
                Life[i][j]=0
            if (Neighbours[i][j]==3):
                Life[i][j]=1
def Count() :
    for i in range (0,N) :
        for j in range (0,N) :
            Neighbours[i][j]=0
    for i in range (0,N) :
        for j in range (0,N) :
            if Life[i][j]==1:
                if Cyclic :
                    Neighbours[(i+1)%N][(j)%N]=Neighbours[(i+1)%N][(j)%N]+1
                    Neighbours[(i-1)%N][(j)%N]=Neighbours[(i-1)%N][(j)%N]+1
                    Neighbours[(i)%N][(j+1)%N]=Neighbours[(i)%N][(j+1)%N]+1
                    Neighbours[(i)%N][(j-1)%N]=Neighbours[(i)%N][(j-1)%N]+1
                    Neighbours[(i+1)%N][(j+1)%N]=Neighbours[(i+1)%N][(j+1)%N]+1
                    Neighbours[(i+1)%N][(j-1)%N]=Neighbours[(i+1)%N][(j-1)%N]+1
                    Neighbours[(i-1)%N][(j-1)%N]=Neighbours[(i-1)%N][(j-1)%N]+1
                    Neighbours[(i-1)%N][(j+1)%N]=Neighbours[(i-1)%N][(j+1)%N]+1
                else :
                    if i<N-1 :
                        Neighbours[(i+1)%N][(j)%N]=Neighbours[(i+1)%N][(j)%N]+1
                        if j<N-1 :
                            Neighbours[(i+1)%N][(j+1)%N]=Neighbours[(i+1)%N][(j+1)%N]+1
                        if j>0 :
                            Neighbours[(i+1)%N][(j-1)%N]=Neighbours[(i+1)%N][(j-1)%N]+1
                    if i>0:
                        Neighbours[(i-1)%N][(j)%N]=Neighbours[(i-1)%N][(j)%N]+1
                        if j>0 :
                            Neighbours[(i-1)%N][(j-1)%N]=Neighbours[(i-1)%N][(j-1)%N]+1
                        if j<N-1 :
                            Neighbours[(i-1)%N][(j+1)%N]=Neighbours[(i-1)%N][(j+1)%N]+1
                    if j<N-1 :
                        Neighbours[(i)%N][(j+1)%N]=Neighbours[(i)%N][(j+1)%N]+1
                    if j>0 :
                        Neighbours[(i)%N][(j-1)%N]=Neighbours[(i)%N][(j-1)%N]+1
                    
                    
                    
                

def Program() :
    Initialize()
    for k in range (0,Numberiterations) :
        Count()
        Iteration()
        print ("*************")
        print ("ITERATION "+str(k)+" :")
        Affiche()
            
            

Program()