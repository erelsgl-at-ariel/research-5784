"""
Attempt to construct a DFS algorithm that lazily generates the neighbors of each node.

Author: Erel Segal-Halevi
Since : 2022-06
"""

from typing import Tuple, Callable
from types import GeneratorType
Node = Tuple[int,int]


def standard_dfs(start: Node, neighbor_generator: Callable, end: Node):
    print("\nSTANDARD DFS")
    stack = []
    stack.append(start)
    visited = set()
    num_generated = 1
    while len(stack)>0:
        current = stack.pop()
        print(f"Popped {current}")
        visited.add(current)
        if current==end:
            print(f"Standard DFS done! Generated {num_generated} nodes and visited {len(visited)} nodes.")
            break
        for neighbor in neighbor_generator(current):
            if neighbor in visited: continue
            print (f"   Generated {neighbor}")
            num_generated += 1
            stack.append(neighbor)


def lazy_dfs(start: Node, neighbor_generator: Callable, end: Node):
    print("\nLAZY DFS")
    stack = []
    stack.append(start)
    visited = set()
    num_generated = 1
    while len(stack)>0:
        current = stack.pop()
        if type(current) == type(start):    # current is a Node
            print(f"Popped {current}")
            visited.add(current)
            if current==end:
                print(f"Lazy DFS done! Generated {num_generated} nodes and visited {len(visited)} nodes.")
                break
            stack.append(neighbor_generator(current))
        elif isinstance(current, GeneratorType):   # current is a neighbor generator
            try:
                while True:
                    neighbor = next(current)
                    if neighbor in visited: continue
                    print (f"   Generated {neighbor}")
                    num_generated += 1
                    stack.append(current)             # Push the generator, in its new state, onto the stack.
                    stack.append(neighbor)            # Push the next neighbor onto the stack
                    break                             # Push only one neighbor each time
            except StopIteration:
                pass
        else: 
            raise TypeError(f"'current' is of the wrong type: {type(current)}")




if __name__=="__main__":
    def four_neighbor_generator(node: Node):
        (x,y) = node
        if x+1 <= 5: yield (x+1,y)
        if x-1 >= -5: yield (x-1,y)
        if y+1 <= 5: yield (x,y+1)
        if y-1 >= -5: yield (x,y-1)

    def four_neighbor_generator_reverse(node: Node):
        (x,y) = node
        if y-1 >= -5: yield (x,y-1)
        if y+1 <= 5: yield (x,y+1)
        if x-1 >= -5: yield (x-1,y)
        if x+1 <= 5: yield (x+1,y)

    standard_dfs( start=(0,0), neighbor_generator=four_neighbor_generator, end=(3,3))
    lazy_dfs( start=(0,0), neighbor_generator=four_neighbor_generator_reverse, end=(3,3))
