class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Convert to [frequency, number] pairs
        pairs = []

        for num in freq:
            pairs.append([freq[num], num])

        # Sort by frequency in descending order
        pairs.sort(reverse=True)

        # Get top k numbers
        result = []

        for i in range(k):
            result.append(pairs[i][1])

        return result
