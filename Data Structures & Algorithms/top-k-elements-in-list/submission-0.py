class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frq = {}
        arr = []

        for i in nums:
            frq[i] = frq.get(i, 0) + 1

        for i, j in frq.items():
            arr.append((j, i))

        arr.sort(reverse=True)

        answer = []

        for i in range(k):
            answer.append(arr[i][1])

        return answer