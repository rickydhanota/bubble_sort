#Bubble Sort

#Write a function that takes in an array of integers and returns a sorted version of that array. Use the bubble sort algo to sort the array

#array = [8,5,2,9,5,6,3]
#output = [2,3,5,5,6,8,9]

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]>array[j]:
                array[i], array[j] = array[j], array[i]
    return array

print(bubbleSort([8,5,2,9,5,6,3]))