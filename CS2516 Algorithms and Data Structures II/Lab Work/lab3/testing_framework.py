import time
from algos import *

class sorting_algorithm_tester():
    def __init__(self):
        self.powers = 6

    def test_algorithms(self, *args):
        for func in args:
            print("-"*15)
            print(func.__name__)
            print("-"*15)
            self.test_algorithm_for_lists(func)

    def test_algorithm_for_lists(self, sortfunc):
        time = 0
        for i in range(self.powers):
            for j in range(20):
                mylist = self.generate_random_list(10 ** i)
                time += self.test_algorithm_time(mylist, sortfunc)
            print(f"Time taken for list of length {10 ** i}: {time/20}")
        return time/20
    
    def test_algorithm_time(self, inlist, sortfunc):
        """Returns the time it took for the given algorithm to sort the given list
            Inputs:
            inlist - List
            sortfunc - function
        """
        start_time = time.perf_counter()
        sortfunc(inlist)
        end_time = time.perf_counter()
        if self.check_sorted(inlist):
            return end_time - start_time
        return "Failed to sort list"
    
    def generate_random_list(self, n):
        """Returns a random list with a input length N"""
        return [random.randint(1, n) for i in range(n)]
    
    def generate_random_list_with_duplicates(self, n, k):
        mylist = [random.randint(0, n) for i in range(n-k)]

        for i in range(k):
            mylist.append(mylist[random.randint(0, n-k)])

        return mylist

    
    def check_sorted(self, inlist):
        """Checks if the input list is sorted. Returns bool"""
        for i in range(len(inlist)):
            if i > 0:
                if inlist[i-1] > inlist[i]:
                    return False
        return True
    
b = sorting_algorithm_tester()
b.test_algorithms(quicksort_lomuto, 
                  quicksort_lomuto_random, 
                  quicksort_hoare, 
                  quicksort_hoare_random,
                  merge_sort, 
                  max_heap_sort)