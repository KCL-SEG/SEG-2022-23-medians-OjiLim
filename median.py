"""Median calculator."""
import math
def findMedian(numbers):
    numbers.sort()
    index = math.floor(len(numbers)/2)
    if (len(numbers)/2)%1 == 0:
        return (numbers[index-1] + numbers[index])/2
    else:
        return numbers[index]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(findMedian(numbers))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

