import argparse
import time
import random

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


main_list=[]

for i in range(100):
  main_list.append(random.sample(range(1,1000),500))


for arr in main_list:
  
  begin = time.time()
  insertionSort(arr)
  end = time.time()
  print(f"Total runtime of the insertiion sort is {end - begin}")

  begin = time.time()
  shellSort(arr,10)
  end = time.time()
  print(f"Total runtime of the shell sort is {end - begin}")

  begin = time.time()
  arr.sort()
  end = time.time()
  print(f"Total runtime of the python sort is {end - begin}")

  #Comment