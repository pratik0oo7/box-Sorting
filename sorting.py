# def swap():
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

# swap(High_wig5ht-1,max_weight)

# array = []
# array1 = []
# array2 = []
# for k in range(0, array, 1):
#     array.append(int(input(k)))

# for k in range(0, k < array, 1):
#     array2[k] = array[k]

# for k in range(0, k < array, 1):
#     array1[k] = array[k]
# sort(array1)
# max = max(array1)
# print(prep())
# print()
