# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:41:11 2021

@author: Hkadro
"""
#CSCI 39575 Project 1
#THIS IS A COP-WIN Graph Eventually the Cop Will Win. However, In this implementation
#If the Cop Cant cath the robbber After 3 Rounds They Get fired and the Robber Wins
#Controlled Implementation of Cops and Robbers on Standard Finite Graph
#Rule can only move to neighbor nodes
#Rule only one Person can occupy a single node at a time.The Exception is when 
#the cop and Robber meet.
#Assign Colors Purple Robbers Pink Cops

#Import Libraries
import networkx as nx
import matplotlib.pyplot as plt
import time

#Create the Playing Field
G = nx.Graph()

color_map = []
#Asks User for Cop and Robber 
cop = input("Place the Cop: ")
cop = int(cop)
robber = input("Place the Robber: ")
robber = int(robber)
#Start Timing without the seconds wasted Typing in Initial Input
start_time = time.time()
G.add_node(cop)
G.add_node(robber)
range = [1,2,3,4,5,6,7,8,9]
#if cop and robber spawn in the same Place There is an automatic cop win
if cop == robber:
    print("Cop Win!")
G.add_nodes_from(range)
G.add_edges_from([(1,2),(2,3),(4,5),(2,4),(3,4),(5,6),(6,7),(6,8),(8,9)])

#Coloring The Nodes
for node in G:
    if node == cop:
        color_map.append("pink")
    elif node == robber:
        color_map.append("purple")
    else:
        color_map.append("aqua")

print("Starting Graph: ")
#Draws the Starting Graph in a shell Shape
nx.draw_shell(G, node_color=color_map, with_labels=True)
plt.show()

#Using in The Built in algorithm to retrieve the Shortest Path      
print("Shortest Path from Cop to Robber")
print(nx.shortest_path(G,cop,robber))

#User moves the cop and robber nodes along the Path
if cop != robber:
#Takes User Input and Moves Cop
    movecop1 = input("Round 1: Move The cop Along the Path: ")
    movecop1 = int(movecop1)
#Takes User Input and Moves Rob
    moverob1 = input("Round 1: Move The robber Along the Path: ")
    moverob1 = int(moverob1)
#Updates cop and robber
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
        
#Prints the time
print("--- %s seconds ---" % (time.time() - start_time))
