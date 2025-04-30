def removeElement(nums: list[int], val: int) -> int:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.remove(nums[i])

    return len(nums)
