import sys
import math
from collections import defaultdict

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
gateways = set()
links = defaultdict(list)

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links[n1].append(n2)
    links[n2].append(n1)
    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.add(ei)

while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    visited_positions = set()
    current_positions = set()
    
    current_positions.add(si)
    gateway_not_found = True
    
    while gateway_not_found:
        planned_positions = set()
        for current_position in current_positions:
            for i in links[current_position]:
                if i not in visited_positions:
                    planned_positions.add(i)
        
        if len(gateways.intersection(planned_positions)) != 0:
            a = gateways.intersection(planned_positions).pop()
            for link in links[a]:
                if link in current_positions:
                    b = link
                    links[a].remove(b)
                    links[b].remove(a)
                    print(a, b)
                    gateway_not_found = False
                    break
        else:
            visited_positions.update(current_positions)
            current_positions = planned_positions