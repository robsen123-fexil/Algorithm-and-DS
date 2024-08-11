class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        def generatesubarray(arr, start, end):
            def appendallsubarrays(arr, start, end, result):
                if end == len(arr):
                    return
                elif start > end:
                    return appendallsubarrays(arr, 0, end + 1, result)
                else:
                    result.append(arr[start:end + 1])
                    return appendallsubarrays(arr, start + 1, end, result)
            result = []
            appendallsubarrays(arr, 0, 0, result)
            return result
        all_subarrays = generatesubarray(arr, 0, 0)
        total_sum = 0
        for subarray in all_subarrays:
            if len(subarray) % 2 != 0:
                total_sum += sum(subarray)
        return total_sum
