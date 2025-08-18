from collections import Counter   # ✅ Correct import

def topKFrequent(arr, k):
    # Step 1: Count frequencies
    freq = Counter(arr)   # Example: Counter({1:3, 2:2, 3:1})

    # Step 2: Sort by frequency in descending order
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # Example: [(1,3), (2,2), (3,1)]

    # Step 3: Pick top k numbers
    return [item[0] for item in sorted_items[:k]]

# Example usage
arr = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(arr, k))  # ✅ Output: [1, 2]

import heapq
from collections import Counter

def topkFrequent(arr, k):
    # Step 1: Count frequencies
    freq = Counter(arr)   # Example: {1:3, 2:2, 3:1}

    # Step 2: Use heapq.nlargest to get top k frequent
    return heapq.nlargest(k, freq.keys(), key=freq.get)

# Example usage
arr = [1, 1, 1, 2, 2, 3]
k = 2
print(topkFrequent(arr, k))  # ✅ Output: [1, 2]
 #bucket sort
def topKFrequent(arr, k):
    # Step 1: Count frequencies
    freq = Counter(arr)   # Example: Counter({1:3, 2:2, 3:1})

    # Step 2: Create buckets
    max_freq = max(freq.values())
    buckets = [[] for _ in range(max_freq + 1)]
    
    for num, count in freq.items():
        buckets[count].append(num)

    # Step 3: Collect top k frequent elements
    result = []
    for i in range(max_freq, 0, -1):
        if buckets[i]:
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]