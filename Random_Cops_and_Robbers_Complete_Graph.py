# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:10:16 2021

@author: Hkadro
"""
#CSCI 39575 Project 1
#This Is A Robber Win Graph
#Random Implementation of Cops and Robbers on Connected Graph
#Rule can only move to neighbor nodes or not move at all
#Rule only one Person can occupy a single node at a time.The Exception is when 
#the cop and Robber meet.
#Assign Colors Purple Robbers Pink Cops

#Import Libraries
import networkx as nx
import matplotlib.pyplot as plt
import random
import time


color_map = []
cop = random.randint(1,9)
robber = random.randint(1,9)
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

#Movement can go 1-9 integers Around Because every node is Connected
copup = cop + random.randint(1,9)
copdown = cop- random.randint(1,9)
robup = robber + random.randint(1,9)
robdown = robber - random.randint(1,9)
#list for Movement
movecop = [copup,copdown]
moverob = [robup,robdown]

#Randomly Move robber or cop node up or down Along The Path
if cop != robber:
#Randomly moves the cop (copup or copdown) and the robber(robup or robdown)
    movementcop = movecop[random.randint(0,1)]
    movementrob = moverob[random.randint(0,1)]
#if the addition takes us above 10 cycle back to 9
    if  movementcop >= 10 :
        movementcop = 9
#if the subtraction takes us below 1 cycle back to 1
    if movementcop <= 0:
        movementcop = 1
    if movementrob >= 10:
        movementrob = 9
    if movementrob <= 0:
        movementrob = 1
#Updates The values of robber and cop
    robber = movementrob
    cop = movementcop
    print("Robber", robber)
    print("Cop", cop)
    print("Round One")
    if robber == movementcop:
        print("Cop Win")
    elif robber != movementcop:
        print("Robber Safe")
        
#Movement can go 1-9 integers Around Because every node is Connected
copup = cop + random.randint(1,9)
copdown = cop- random.randint(1,9)
robup = robber + random.randint(1,9)
robdown = robber - random.randint(1,9)
#list for Movement
movecop = [copup,copdown]
moverob = [robup,robdown]

if cop != robber:
    movementcop = movecop[random.randint(0,1)]
    movementrob = moverob[random.randint(0,1)]
    if  movementcop >= 10 :
        movementcop = 9
    if movementcop <= 0:
        movementcop = 1
    if movementrob >= 10:
        movementrob = 9
    if movementrob <= 0:
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
        
#Movement can go 1-9 integers Around Because every node is Connected
copup = cop + random.randint(1,9)
copdown = cop- random.randint(1,9)
robup = robber + random.randint(1,9)
robdown = robber - random.randint(1,9)
#list for Movement
movecop = [copup,copdown]
moverob = [robup,robdown]

if cop != robber:
    movementcop = movecop[random.randint(0,1)]
    movementrob = moverob[random.randint(0,1)]
    if  movementcop >= 10 :
        movementcop = 9
    if movementcop <= 0:
        movementcop = 1
    if movementrob >= 10:
        movementrob = 9
    if movementrob <= 0:
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
        
#Prints Time
print("--- %s seconds ---" % (time.time() - start_time))
