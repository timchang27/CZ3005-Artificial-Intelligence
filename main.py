from os import path, listdir
from pathlib import Path
import json
from re import L
from stat import UF_COMPRESSED
import time
import json
from task1 import UCS_r
from task2 import UCS
from task3 import AStar


class Main():
    def __init__(self):
        base_path = Path(__file__).parent
        folder_path = (base_path / "../data").resolve()
        with open(f"{folder_path}/Coord.json") as f:
            self.Coord = json.load(f)
        with open(f"{folder_path}/Cost.json") as f:
            self.Cost = json.load(f)
        with open(f"{folder_path}/Dist.json") as f:
            self.Dist = json.load(f)
        with open(f"{folder_path}/G.json") as f:
            self.G = json.load(f)
        self.START = '1'
        self.END = '50'
        self.BUDGET = 287932

    def task1(self):
        print("========================Task 1: UCS Relaxed:========================\n")
        pi, nodesExpand = UCS_r(
            self.G, self.Dist, self.START, self.END)
        self.outputShortestPath(pi, 1, 50)
        print("Shortest distance:", self.outputShortestDistance(
            pi, self.Dist, 1, 50))
        print("Total energy cost: ", self.outputEnergyCost(
            pi, self.Cost, 1, 50))
        print("Number of nodes expanded: ", nodesExpand)
        print("\n")

    def task2(self):
        print("============================Task 2: UCS:============================\n")
        pi, nodesExpand = UCS(
            self.G, self.Dist, self.START, self.END, self.BUDGET, self.Cost)
        self.outputShortestPath(pi, 1, 50)
        print("Shortest distance:", self.outputShortestDistance(
            pi, self.Dist, 1, 50))
        print("Total energy cost: ", self.outputEnergyCost(
            pi, self.Cost, 1, 50))
        print("Number of nodes expanded: ", nodesExpand)
        print("\n")

    def task3(self):
        print("=========================Task 3: A* Search:=========================\n")
        path, dist, cost = AStar(
            self.G, self.Dist, self.Cost, self.Coord, self.START, self.END, self.BUDGET)
        path_str = "S->" + "->".join([node for node in path[:-1]]) + "->T"
        print("Shortest path:\n" + path_str)
        print("Shortest distance:", dist)
        print("Total energy cost:", cost)

    def createEdgeString(self, node1, node2):
        return node1 + ',' + node2

    def outputShortestPath(self, pi, source, destination):
        nodesInShortestPath = []
        previous = pi[destination-1]  # previous node in shortest path
        nodesInShortestPath.append(int(previous))
        # while loop to keep appending previous node until reach source
        while(pi[int(previous)-1] != str(source)):
            previous = pi[int(previous)-1]
            nodesInShortestPath.append(int(previous))
        output = "S"
        for node in reversed(nodesInShortestPath):
            output = output + "->" + str(node)
        output = output + "->T"
        print("Shortest path:\n" + output)

    def outputShortestDistance(self, pi, dist, source, destination):
        totalDist = 0
        previous = pi[destination-1]  # previous node in shortest path
        key = self.createEdgeString(previous, str(destination))
        totalDist += dist[key]
        while(int(previous) != source):  # while loop to keep appending previous node until reach source
            key = self.createEdgeString(pi[int(previous)-1], previous)
            totalDist += dist[key]
            previous = pi[int(previous)-1]
        return totalDist

    def outputEnergyCost(self, pi, cost, source, destination):
        totalCost = 0
        previous = pi[destination-1]
        key = self.createEdgeString(previous, str(destination))  # 1,2
        totalCost += cost[key]
        while(int(previous) != source):
            key = self.createEdgeString(pi[int(previous)-1], previous)
            totalCost += cost[key]
            previous = pi[int(previous)-1]
        return totalCost

    def execute(self):
        Main.task1(self)
        Main.task2(self)
        Main.task3(self)


if __name__ == "__main__":
    main = Main()
    main.execute()
