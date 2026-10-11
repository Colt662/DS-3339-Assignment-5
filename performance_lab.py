import random
import time

# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if len(numbers) == 0:
        return 

    freq_dict = dict() #fast operations, key:value for number:frequency, space complexity depends on how unique the list is, more unique lists will have higher space complexity
    for number in numbers: #Whole loop: O(n) on average, O(n^2) worst case if every hash collides and every insertion triggers resize
        if number in freq_dict: #O(1) avg, O(n) worst if hash collision
            freq_dict[number] = freq_dict[number] + 1 

        else:
            freq_dict[number] = 1 #O(1) avg, O(n) worst if resize


    most_frequent = numbers[0]
    highest_frequency = 1

    for number, frequency in freq_dict.items(): #Whole loop is O(n) where n is the size of the frequency dictionairy, so for n as size or original list it is O(1) best case or O(n) worst case depending on # of unique items
        if frequency > highest_frequency: 
            most_frequent = number
            highest_frequency = frequency

    return most_frequent

    

"""
Info sourced from https://pythoncomplexity.com/builtins/dict/#complexity-reference
Time and Space Analysis for problem 1:
- Best-case: O(n) for no hash collisions or resizes
- Worst-case: O(n^2) for every number causing hash collisions or resizes
- Average-case: O(n) since hash collisions should be infrequent for most lists and operations that could involve resizing are amoritized to O(1)
- Space complexity: O(n) if all items are unique, O(1) if all items are the same
- Why this approach? Dictionaries have fast operations, integers in a similar range should have few hash collisions.
- Could it be optimized? It could be optimized if the number with the highest frequency was determined in the first loop, although it would still average O(n) time since every element of the list will always need to be accessed. Testing has now shown that for highly unique lists, it would be at most ~5x faster if it was done in the first loop, so still O(n).
"""

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    unqiues_list = set() 
    output_list = list()

    for num in nums:
        if num not in unqiues_list:
            unqiues_list.add(num)
            output_list.append(num)

    return output_list
    
"""
Time and Space Analysis for problem 2:
- Best-case: O(n) for a list with 1 unique element
- Worst-case: O(n) for a list with n unique elements
- Average-case: O(n) for lists with between 1 and n unique elements
- Space complexity: O(n) since if the list is 100% unqiue a full list and set copy will be created
- Why this approach? Sets have no ordering so they cannot be used by themselves. To preserve order a set is used for fast comparisons and a seperate list is used to preserve the order of the output
- Could it be optimized? The uniques_list could possibly be created as a set from the list, instead of being added on to in the loop, but it would still be O(n)
"""

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    nums = set(nums) #no order wanted, no duplicates present/only unqiue pairs wanted, fast lookup
    result = []
    already_used = set()
    for num in nums:
        if num not in already_used: 
            if (target - num) in nums:
                result.append((num, target - num))
                already_used.add(target - num)
    return result


"""
Time and Space Analysis for problem 3:
- Best-case: O(n) with no hash collisions
- Worst-case: O(n^2) with consistent hash collisions
- Average-case: O(n) Since hash collisions should be infrequent
- Space complexity:
- Why this approach? The input was assumed to have no duplicates, lists with duplicates also work since it only asks for unique pairings, and sets have O(1) lookup with no hash collisions
- Could it be optimized? If the list could be sorted quickly, or came sorted, then there could be 2 indexes inserted at the highest and lowest values that could possibly add up to the target, then working towards the middle until no more values that could add up to the target. This would still likely end up with O(n) complexity, but could potentially run faster in scenarios where the list did not contain many pairs that could add to the target. It could possibly also achieve O(log(n)) complexity for lists with no pairs, since the 2 indexes could use binary search to eliminate most possible pairings.  
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    pass

"""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


def list_populator(size,value_range):
    value_range = max(value_range, 10)#no use in smaller range
    test_list = []
    for i in range(size):
        test_list.append(random.randint(1,value_range))
    return test_list

def most_frequent_test(list, range_name):
    start = time.time()
    value = most_frequent(list)
    end = time.time()
    print(f'Time taken for list with {range_name:5} range of numbers:   {end - start} ')
    print(f'Most frequent value: {value}')

def remove_duplicates_test(list, range_name):
    
    start = time.time()
    new_list = remove_duplicates(list)
    end = time.time()
    if len(list) == 0:
        print(f'Time taken for list with a {range_name:16} list of numbers:   {end - start} ')
    
    elif len(list) > 30:
        print(f'Time taken for list with a {range_name:16} list of numbers:   {end - start} ')

    else:
        print(f'Old list = {list}')
        print(f'New list = {new_list}')

def find_pairs_test(list, target, range_name):
    start = time.time()
    pairs_list = find_pairs(list, target)
    end = time.time()

    if len(list) == 0:
        print(f'Time taken for list with a {range_name:16} pairing of numbers:   {end - start} ')
    
    elif len(list) > 30:
        print(f'Time taken for list with a {range_name:16} pairing of numbers:   {end - start} ')

    else:
        print(f'Original list: {list}')
        print(f'Target: {target}   Pairs: {pairs_list}')

if __name__ == "__main__":
    test_consent = input("Would you like to test the most_frequent function? Y/N: ")
    if test_consent.lower() == "y":
        print("Now testing most_frequent function")
        print("**********")
        print("")
        test_size = 1000
        for i in range(4):
            baseline_start = time.time()

            test_list_short_range = list_populator(test_size, test_size // 1000 )
            test_list_mid_range = list_populator(test_size, test_size // 100)
            test_list_long_range = list_populator(test_size, test_size // 10)
            test_list_full_range = list_populator(test_size, test_size)

            baseline_end = time.time()
            print(f'Baseline time to populate 4 lists with {test_size:,} elements each: {baseline_end - baseline_start}')

            most_frequent_test([], "empty")
            most_frequent_test(test_list_short_range, "short")
            most_frequent_test(test_list_mid_range, "mid")
            most_frequent_test(test_list_long_range, "long")
            most_frequent_test(test_list_full_range, "full")

            test_size = test_size * 10

        print("")
        print("**********")
        print("End of most_frequent function tests")


    test_consent = input("Would you like to test the remove_duplicates function? Y/N: ")
    if test_consent.lower() == "y":
        print("Now testing remove_duplicates function")
        print("**********")
        print("")
        test_size = 30
        for i in range(4):
            baseline_start = time.time()

            highly_similar_list = list_populator(test_size, test_size // 1000)
            somewhat_similar_list = list_populator(test_size, test_size // 100)
            somewhat_unique_list = list_populator(test_size, test_size // 10)
            highly_unique_list = list_populator(test_size, test_size)

            baseline_end = time.time()
            print(f'Baseline time to populate 4 lists with {test_size:,} elements each: {baseline_end - baseline_start}')

            remove_duplicates_test([], "empty")
            remove_duplicates_test(highly_similar_list, "highy similar")
            remove_duplicates_test(somewhat_similar_list, "somewhat similar")
            remove_duplicates_test(somewhat_unique_list, "somewhat unique")
            remove_duplicates_test(highly_unique_list, "highly unique")
            test_size = test_size * 10

        print("")
        print("**********")
        print("End of remove_duplicates function tests")


    test_consent = input("Would you like to test the find_pairs function? Y/N: ")
    if test_consent.lower() == "y":
            print("Now testing find_pairs function")
            print("**********")
            print("")
            test_size = 30
            for i in range(6):
                baseline_start = time.time()
    
                highly_likely_list = list_populator(test_size, test_size // 1000)
                somewhat_likely_list = list_populator(test_size, test_size // 100)
                somewhat_unlikely_list = list_populator(test_size, test_size // 10)
                highly_unlikely_list = list_populator(test_size, test_size)
    
                baseline_end = time.time()
                print(f'Baseline time to populate 4 lists with {test_size:,} elements each: {baseline_end - baseline_start}')
    
                find_pairs_test([], 0, "empty")
                find_pairs_test(highly_likely_list, max((test_size // 1000) + 1, 11), "highy likely")
                find_pairs_test(somewhat_likely_list, max((test_size // 100) / 2 , 5),  "somewhat likely")
                find_pairs_test(somewhat_unlikely_list, max((test_size // 100) / 4, 3), "somewhat unlikely")
                find_pairs_test(highly_unlikely_list, 2, "highly unlikely")
                test_size = test_size * 10
    
            print("")
            print("**********")
            print("End of find_pairs function tests")
