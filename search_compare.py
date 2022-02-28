import argparse
import time
import random

def sequential_search(arr,ele):
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True     
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos  = pos+1   
    return found

def ordered_sequential_search(ordered_list, term): 
    ordered_list_size = len(ordered_list) 
    for i in range(ordered_list_size): 
        if term == ordered_list[i]: 
            return i 
        elif ordered_list[i] > term: 
            return None 
    return None

def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def binary_search_recursive(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid if arr[mid] == target else None
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = binary_search_recursive((arr[mid:]), target)
            return mid + callback_response if callback_response is not None else None
        else:
            return binary_search_recursive((arr[:mid]), target)


main_list=[]

for i in range(100):
  main_list.append(random.sample(range(1,1000),500))


for arr in main_list:
  ele = random.randint(1000,2000)

  begin = time.time()
  sequential_search(arr,ele)
  end = time.time()
  print(f"Total runtime of the sequential search is {end - begin}")

  begin = time.time()
  ordered_sequential_search(arr,ele)
  end = time.time()
  print(f"Total runtime of the ordered sequential search is {end - begin}")

  begin = time.time()
  binary_search_iterative(arr,ele)
  end = time.time()
  print(f"Total runtime of the binary search iterative is {end - begin}")

  begin = time.time()
  binary_search_recursive(arr,ele)
  end = time.time()
  print(f"Total runtime of the binary search recursive is {end - begin}")

if __name__ == "__main__":
    """Main entry point"""
    pass


#Comment