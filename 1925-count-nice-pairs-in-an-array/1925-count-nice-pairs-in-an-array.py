class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        result = []
        
        for i in range(len(nums)):
            # Reverse the digits of the current number
            rev = int(str(nums[i])[::-1])
            # Compute the difference (this will be our "key" to find nice pairs)
            result.append(nums[i] - rev)
        
        hsh = {}
        count = 0
        
        # Count the number of pairs with the same key
        for diff in result:
            if diff in hsh:
                count = (count + hsh[diff]) % MOD  # Update count and take modulo
                hsh[diff] += 1
            else:
                hsh[diff] = 1
        
        return count
