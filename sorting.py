
from operator import index
from traceback import print_tb
from turtle import position


def sorting(boxes):
    n = len(boxes)

    for i in range(n):
        for j in range(n - i - 1):
            if boxes[j] > boxes[j + 1]:
                temp = boxes[j]
                boxes[j] = boxes[j+1]
                boxes[j+1] = temp


print('Enter the size of box')
size = int(input())

print('Enter the distance from the office')
High_wight = int(input())

boxes = []
print('Inser the weight of boxes')
for i in range(0, size, 1):
    boxes.append(int(input()))

effort = 2*boxes[High_wight-1]*min(boxes) + max(boxes)*min(boxes)
sorting(boxes)
print('Sorted list: ', boxes)
max_weight = max(boxes)
print('Max value: ', max_weight)
boxes.insert(High_wight-1, max_weight)
boxes.pop()
print(boxes)
print(effort)
