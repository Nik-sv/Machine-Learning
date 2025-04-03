from collections import Counter

# 1. Find max and min
def find_max_min(arr):
    return max(arr), min(arr)

# 2. Reverse an array
def reverse_array(arr):
    return arr[::-1]

# 3. Check if array is palindrome
def is_palindrome(arr):
    return arr == arr[::-1]

# 4. Find second largest element
def second_largest(arr):
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# 5. Move all zeros to the end
def move_zeros(arr):
    return [num for num in arr if num != 0] + [0] * arr.count(0)

# 6. Find frequency of each element
def frequency_count(arr):
    return dict(Counter(arr))

# 7. Sum of all elements
def sum_of_elements(arr):
    return sum(arr)

# 8. Find the missing number in a sequence
def missing_number(arr, n):
    return sum(range(1, n+1)) - sum(arr)

# 9. Find common elements in two arrays
def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

# 10. Check for duplicates
def contains_duplicates(arr):
    return len(arr) != len(set(arr))

# 11. Find the largest sum of any two elements
def largest_pair_sum(arr):
    arr.sort()
    return arr[-1] + arr[-2]

# 12. Find index of first occurrence of element
def first_occurrence(arr, target):
    return arr.index(target) if target in arr else -1

# 13. Count even and odd numbers
def count_even_odd(arr):
    evens = sum(1 for num in arr if num % 2 == 0)
    return evens, len(arr) - evens

# 14. Sum of elements at odd indices
def sum_odd_indices(arr):
    return sum(arr[i] for i in range(1, len(arr), 2))

# 15. Check if all elements are positive
def all_positive(arr):
    return all(num > 0 for num in arr)

# 16. Find first non-repeating element
def first_non_repeating(arr):
    freq = Counter(arr)
    for num in arr:
        if freq[num] == 1:
            return num
    return -1

# Example test cases
arr = [3, 1, 4, 1, 5, 9, 2]
print("Max & Min:", find_max_min(arr))
print("Reversed Array:", reverse_array(arr))
print("Palindrome:", is_palindrome([1, 2, 3, 2, 1]))
print("Second Largest:", second_largest([10, 5, 30, 20, 15]))
print("Moved Zeros:", move_zeros([0, 1, 2, 0, 3, 0, 4]))
print("Frequency Count:", frequency_count([4, 5, 6, 4, 7, 6, 4]))
print("Sum of Elements:", sum_of_elements([10, 20, 30, 40, 50]))
print("Missing Number:", missing_number([1, 2, 4, 5], 5))
print("Common Elements:", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print("Contains Duplicates:", contains_duplicates([1, 2, 3, 4, 5, 1]))
print("Largest Sum of Two:", largest_pair_sum([1, 2, 3, 4, 5]))
print("First Occurrence Index:", first_occurrence([2, 4, 6, 8, 10], 6))
print("Even & Odd Count:", count_even_odd([1, 2, 3, 4, 5, 6]))
print("Sum of Odd Indices:", sum_odd_indices([1, 2, 3, 4, 5, 6]))
print("All Positive:", all_positive([1, 2, 3, 4, 5]))
print("First Non-Repeating:", first_non_repeating([4, 5, 6, 4, 5, 7]))
