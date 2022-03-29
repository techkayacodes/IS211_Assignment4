import argparse
import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        print("After increments of size", sublistcount, "The list is",alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):

    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return sorted(a_list)

list_sizes = [500, 1000, 5000]

the_size = list_sizes[0]


def main():
    for n in [500, 1000, 10000]:
        print('For List Sizes: %d' %n)
        Insertion_Sort = 0
        Shell_Sort = 0
        Python_Sort = 0

        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            sorted_list = shellSort(mylist500)
            time_spent = time.time() - start
            Shell_Sort += time_spent
            avg_time = Shell_Sort / 100
            print(f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            sorted_list = python_sort(mylist500)
            time_spent = time.time() - start
            Python_Sort += time_spent
            avg_time = Python_Sort / 100
            print(f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            insertion_sort(mylist500)
            time_spent = time.time() - start
            Insertion_Sort += time_spent
            avg_time = Insertion_Sort / 100
            print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
    
    
    """
    for n in [500, 1000, 10000]:
        print('For List Sizes: %d' %n)
        Insertion_Sort = 0
        Shell_Sort = 0
        Python_Sort = 0

        for x in range(0,100): 
            begin = time.time()
            insertion_sort(arr)
            end = time.time()
            
            begin = time.time()
            shellSort(arr,10)
            end = time.time()
            
            begin = time.time()
            arr.sort()
            end = time.time()
                
        print("Insertion Sort took %10.7f seconds to run, on average" %(Insertion_Sort/100))
        print("Shell Sort took %10.7f seconds to run, on average" %(Shell_Sort/100))
        print("Python Sort took %10.7f seconds to run, on average" %(Python_Sort/100))
"""

if __name__ == "__main__":
    main()

