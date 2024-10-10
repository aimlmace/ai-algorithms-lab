import numpy as np
import pandas as pd
def getInvCount(arr, goal_arr):
    inv_count = 0
    empty_value = 0
    goal_position = {value: idx for idx, value in enumerate(goal_arr)}
    mapped_arr = [goal_position[value] for value in arr if value != empty_value]
    for i in range(len(mapped_arr)):
        for j in range(i + 1, len(mapped_arr)):
            if mapped_arr[i] > mapped_arr[j]:
                inv_count += 1
    
    return inv_count

def isSolvable(puzzle, goal_state):
    flat_puzzle = [j for sub in puzzle for j in sub]
    flat_goal = [j for sub in goal_state for j in sub]
    inv_count = getInvCount(flat_puzzle, flat_goal)
    return (inv_count % 2 == 0)
def up(row,col,state):
    global frontier
    state[row][col]=state[row-1][col]
    state[row-1][col]=0
    if not any([np.array_equal(state,j) for j in explored]):
        frontier.append(state)
def down(row,col,state):
    global frontier
    state[row][col]=state[row+1][col]
    state[row+1][col]=0
    if not any([np.array_equal(state,j) for j in explored]):
        frontier.append(state)
def left(row,col,state):
    global frontier
    state[row][col]=state[row][col-1]
    state[row][col-1]=0
    if not any([np.array_equal(state,j) for j in explored]):
        frontier.append(state)
def right(row,col,state):
    global frontier
    state[row][col]=state[row][col+1]
    state[row][col+1]=0
    if not any([np.array_equal(state,j) for j in explored]):
        frontier.append(state)
def Possible_state(state):
    row,col=find_blank(state.tolist())
    if row==0 :
        if col==0:
            right(row,col,state.copy())
            down(row,col,state.copy())
        elif col==1:
            left(row,col,state.copy())
            right(row,col,state.copy())
            down(row,col,state.copy())
        elif col==2:
            left(row,col,state.copy())
            down(row,col,state.copy())
    elif row==1 :
        if col==0:
            up(row,col,state.copy())
            right(row,col,state.copy())
            down(row,col,state.copy())
        elif col==1:
            up(row,col,state.copy())
            left(row,col,state.copy())
            right(row,col,state.copy())
            down(row,col,state.copy())
        elif col==2:
            up(row,col,state.copy())
            left(row,col,state.copy())
            down(row,col,state.copy())
    elif row==2 :
        if col==0:
            up(row,col,state.copy())
            right(row,col,state.copy())
        elif col==1:
            up(row,col,state.copy())
            left(row,col,state.copy())
            right(row,col,state.copy())
        elif col==2:
            up(row,col,state.copy())
            left(row,col,state.copy())
    frontier.sort(key=lambda x: Heuristic(x))

def Heuristic(initial):
    return 9-sum(sum(np.equal(initial,o)))
def find_blank(state):
    for i in range(len(state)):
        if 0 in state[i]:
            return (i,state[i].index(0))
print("Enter the puzzle state")
initial=[[int(x) for x in input().split()]for j in range(3)]
a=np.array(initial)
print("Enter the puzzle goal state")
goal=[[int(x) for x in input().split()]for j in range(3)]
o=np.array(goal)
temp=a.copy()
v=temp
print(v)
frontier=[]
explored=[temp]
Possible_state(temp)
if(isSolvable(temp,o)) :
    print("Solvable")
    while(Heuristic(v)!=0):  
        v=frontier.pop(0)
        print(v)
        explored.append(v)
        Possible_state(v)
else :
    print("Not Solvable")

