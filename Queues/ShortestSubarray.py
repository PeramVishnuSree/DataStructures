# Given a list nums and k, return the length of the shortest sub array whose sum is at least k

# soulution 1
def ShortestSubarray(nums,k):
    subarrays = []
    mn = len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            ar = nums[i:j]
            subarrays.append(ar)

    for a in subarrays:
        print(a)
        if sum(a) >= k and len(a) < mn:
            mn = len(a)

    if mn == len(nums) and sum(nums) < k:
        mn = -1

    return mn

# solution 2 (only positive integers)

def shortestSubarray(nums, k):

        i = 0
        j = 1

        mn = len(nums)

        if len(nums) == 1:
            if sum(nums) >= k:
                mn = 1

        while j <= len(nums) and i <= len(nums) - 1:
            print(nums[i:j])
            if sum(nums[i:j]) == k:
                if len(nums[i:j]) < mn:
                    mn = len(nums[i:j])
                j += 1

            elif sum(nums[i:j]) > k:
                if len(nums[i:j]) < mn:
                    mn = len(nums[i:j])
                i += 1

            elif sum(nums[i:j]) < k:
                if j == len(nums) and i < len(nums):
                    i += 1
                else:
                    j += 1

        if mn == len(nums) and sum(nums) < k:
            mn = -1

        return mn