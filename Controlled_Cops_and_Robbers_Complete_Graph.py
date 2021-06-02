# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:49:20 2021

@author: Hkadro
"""
#CSCI 39575 Project 1
#This Is A Robber Win Graph
#Controlled Implementation of Cops and Robbers on Connected Graph
#Rule can only move to neighbor nodes or Stay in Place
#Rule only one Person can occupy a single node at a time.The Exception is when 
#the cop and Robber meet.
#Assign Colors Purple Robbers Pink Cops

#Import Libraries
import networkx as nx
import matplotlib.pyplot as plt
import time

color_map = []
#asks User for Cop and Robber 
cop = input("Place the Cop: ")
cop = int(cop)
robber = input("Place the Robber: ")
robber = int(robber)
start_time = time.time()
range = [1,2,3,4,5,6,7,8,9]
#if cop and robber spawn in the same Place There is an automatic cop win
if cop == robber:
    print("Cop Win!")
#Create the Playing Field
G = nx.complete_graph(range)

#Coloring The Nodes
for node in G:
    if node == cop:
        color_map.append("pink")
    elif node == robber:
        color_map.append("purple")
    else:
        color_map.append("aqua")

print("Starting Graph: ")
#Draws The Starting Graph in a Shell Shape
nx.draw_shell(G, node_color=color_map, with_labels=True)
plt.show()

#Using in The Built in algorithm to retrieve the Shortest Path
print("Shortest Path from Cop to Robber")
print(nx.shortest_path(G,cop,robber))


#Randomly Move cop and robber nodes up or down Along The Path
if cop != robber:
#Takes User Input and Moves Cop
    movecop1 = input("Round 1: Move The cop Along the Path: ")
    movecop1 = int(movecop1)
#Takes User Input and Moves Robber
    moverob1 = input("Round 1: Move The robber Along the Path: ")
    moverob1 = int(moverob1)
# Updates The values of Cop and Robber
    robber = moverob1
    cop = movecop1
    print("Robber", robber)
    print("Cop", cop)
    print("Round One")
    if robber == movecop1:
        print("Cop Win")
    elif robber != movecop1:
        print("Robber Safe")

if cop != robber:
    movecop2 = input("Round 2: Move The cop Along the Path: ")
    movecop2 = int(movecop2)
    moverob2 = input("Round 2: Move The robber Along the Path: ")
    moverob2 = int(moverob2)
    robber = moverob2
    cop = movecop2
    print("Robber", robber)
    print("Cop", cop)
    print("Round Two")
    if robber == movecop2:
        print("Cop Win")
    elif robber != movecop2:
        print("Robber Safe")

if cop != robber:
    movecop3 = input("Round 3: Move The cop Along the Path: ")
    movecop3 = int(movecop3)
    moverob3 = input("Round 3: Move The robber Along the Path: ")
    moverob3 = int(moverob3)
    robber = moverob3
    cop = movecop3
    print("Robber", robber)
    print("Cop", cop)
    print("Final Round")
    if robber == movecop3:
        print("Cop Win")
    elif robber != movecop3:
        print("Robber Win")

#Prints Time
print("--- %s seconds ---" % (time.time() - start_time))
