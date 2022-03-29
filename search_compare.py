import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return found, end-start


def ordered_sequential_search(a_list, item):
    start_A = time.time()

    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end_A = time.time()
    return found, end_A-start_A


def binary_search_iterative(a_list, item):
    start_B = time.time()

    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
       midpoint = (first + last) // 2
       if a_list[midpoint] == item:
         found = True
       else:
           if item < a_list[midpoint]:
               last = midpoint - 1
           else:
               first = midpoint + 1
    end_B = time.time()
    return found, end_B-start_B
    
    
def binary_search_recursive(a_list, item):
    
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

def test_wrapper(a_list, item):
    """Calls the function binary_search_recursive and computes the time of the aforemetioned function."""
    start_C = time.time()
    result = binary_search_recursive(a_list, item)
    end_C = time.time()
    return result, end_C-start_C

def main():
    """This function prints how long it takes for the sequential_search,
    ordered_sequential_search, binary_search_iterative,
    and binary_search_recursive functions to run on average"""
    for k in [500, 1000, 10000]:
        print('For List Sizes: %d' %k)
        Seq_Search = 0
        Ordered_Seq_Search = 0
        Binary_Search_Iter = 0
        Binary_Search_Recur = 0

        for x in range(0,100):
            random_list = random.sample(range(1, 100000), k)
            tempresult, temptime = sequential_search(random_list, -1)
            Seq_Search += temptime

            random_list.sort()
            tempresult, temptime = ordered_sequential_search(random_list, -1)
            Ordered_Seq_Search += temptime

            tempresult, temptime = binary_search_iterative(random_list, -1)
            Binary_Search_Iter += temptime

            tempresult, temptime = test_wrapper(random_list, -1)
            Binary_Search_Recur += temptime

        print("Sequential Search took %10.7f seconds to run, on average" %(Seq_Search/100))
        print("Ordered Sequential Search took %10.7f seconds to run, on average" %(Ordered_Seq_Search/100))
        print("Binary Search Iterative took %10.7f seconds to run, on average" %(Binary_Search_Iter/100))
        print("Binary Search Recursive took %10.7f seconds to run, on average" %(Binary_Search_Recur/100))

main()

if __name__ == "__main__":
    """Main entry point"""
    pass
