def solution(nums: list):
    nums = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in nums:
            return i

    if not nums:
        return 1

    return i + 1
