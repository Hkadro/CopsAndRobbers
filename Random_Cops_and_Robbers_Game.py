# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:55:48 2021

@author: HKadro
"""
#CSCI 39575 Project 1
#THIS IS A COP-WIN Graph Eventually the Cop Will Win. However, In this implementation
#If the Cop Cant cath the robbber After 3 Rounds They Get Fired and the Robber Wins
#Random Implementation of Cops and Robbers on Standard Finite Graph
#Rule can only move to neighbor nodes or Stay in the same Place
#Rule only one Person can occupy a single node at a time.The Exception is when 
#the cop and Robber meet.
#Assign Colors Purple Robbers Pink Cops
#one cop one Robber

#Import Libraries
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

#Create the Playing Field
G = nx.Graph()

color_map = []
cop = random.randint(1,9)
robber = random.randint(1,9)
#Starts Timing from Same Place as Controlled Game
start_time = time.time()
G.add_node(cop)
G.add_node(robber)
range = [1,2,3,4,5,6,7,8,9]
#if cop and robber spawn in the same Place There is an automatic cop win
if cop == robber:
    print("Cop Win!")
G.add_nodes_from(range)
G.add_edges_from([(1,2),(2,3),(4,5),(2,4),(3,4),(5,6),(6,7),(6,8),(8,9)])

#Color the Nodes
for node in G:
    if node == cop:
        color_map.append("pink")
    elif node == robber:
        color_map.append("purple")
    else:
        color_map.append("aqua")
        
print("Starting Graph: ")
#Draws the Starting Graph
nx.draw_shell(G, node_color=color_map, with_labels=True)
plt.show()

#Uses built in Algorithm to find the Shortest Path
print("Shortest Path from Cop to Robber")
print(nx.shortest_path(G,cop,robber))

#Movement by 1 because the connected nodes are mostly in order 
copup = cop + random.randint(0,1)
copdown = cop - random.randint(0,1)
robup = robber + random.randint(0,1)
robdown = robber - random.randint(0,1)
#list of possible movement for Cop and Robber nodes
movecop = [copup,copdown]
moverob = [robup,robdown]

#Randomly Move cop and robber nodes up or down Along The Path
if cop != robber:
#Randomly moves the cop (copup or copdown) and the robber(robup or robdown)
    movementcop = movecop[random.randint(0,1)]
    movementrob = moverob[random.randint(0,1)]
#if the addition takes us to 10 cycle back to 9
    if movementcop == 10:
        movementcop = 9
#if the Subtraction takes us to 0 cycle back to 1
    if movementcop == 0:
        movementcop = 1
    if movementrob == 10:
        movementrob = 9
    if movementrob == 0:
        movementrob = 1
#Update The values of Cop and Robber
    robber = movementrob
    cop = movementcop
    print("Robber", robber)
    print("Cop", cop)
    print("Round One")
    if robber == movementcop:
        print("Cop Win")
    elif robber != movementcop:
        print("Robber Safe")
        
#Movement by 1 because the connected nodes are mostly in order 
copup = cop + random.randint(0,1)
copdown = cop - random.randint(0,1)
robup = robber + random.randint(0,1)
robdown = robber - random.randint(0,1)
#list of possible movement for Cop and Robber nodes
movecop = [copup,copdown]
moverob = [robup,robdown]

if cop != robber:
    movementcop = movecop[random.randint(0,1)]
    movementrob = moverob[random.randint(0,1)]
    if movementcop == 10:
        movementcop = 9
    if movementcop == 0:
        movementcop = 1
    if movementrob == 10:
        movementrob = 9
    if movementrob == 0:
        movementrob = 1
    robber = movementrob
    cop = movementcop
    print("Robber", robber)
    print("Cop", cop)
    print("Round Two")
    if robber == movementcop:
        print("Cop Win")
    elif robber != movementcop:
        print("Robber Safe")

#Movement by 1 because the connected nodes are mostly in order 
copup = cop + random.randint(0,1)
copdown = cop - random.randint(0,1)
robup = robber + random.randint(0,1)
robdown = robber - random.randint(0,1)
#list of possible movement for Cop and Robber nodes
movecop = [copup,copdown]
moverob = [robup,robdown]

if cop != robber:
    movementcop = movecop[random.randint(0,1)]
    movementrob = moverob[random.randint(0,1)]
    if movementcop == 10:
        movementcop = 9
    if movementcop == 0:
        movementcop = 1
    if movementrob == 10:
        movementrob = 9
    if movementrob == 0:
        movementrob = 1
    robber = movementrob
    cop = movementcop
    print("Robber", robber)
    print("Cop", cop)
    print("Final Round")
    if robber == movementcop:
        print("Cop Win")
    elif robber != movementcop:
        print("Robber Win")
        
#Generates the Operation Time
print("--- %s seconds ---" % (time.time() - start_time))





