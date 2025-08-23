'''nums = [1, 2, 3, 4]
Output = [24, 12, 8, 6]

Explanation:
answer[0] = 2 * 3 * 4 = 24
answer[1] = 1 * 3 * 4 = 12
answer[2] = 1 * 2 * 4 = 8
answer[3] = 1 * 2 * 3 = 6
'''
'''approach 1: Approaches
1️⃣ Brute Force Approach (O(n²))

For each element i, loop through the array and multiply all except nums[i].

Very slow if n is large.

'''
def productExceptSelf(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result
# Example usage
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
'''2️⃣ Optimal Approach (O(n))
Prefix & Suffix Arrays (O(n), extra space)

Make two arrays:

prefix[i] = product of nums[0..i-1]

suffix[i] = product of nums[i+1..n-1]

Then answer[i] = prefix[i] * suffix[i]'''
def product(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n
    for i in range(1,n):
        prefix [i] = prefix[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1] * nums[j+1]
            for i in range(n):
                answer[i] = prefix[i] * suffix[i]
    return answer
# Example usage
nums = [1, 2, 3, 4]
print(product(nums))  # Output: [24, 12, 8, 6