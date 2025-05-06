def leftRightDifference(nums: list[int]) -> list[int]:
    totalSum = sum(nums)
    leftSum = 0
    answ = []

    for i in range(len(nums)):
        rightSum = totalSum - leftSum - nums[i]
        answ.append(abs(leftSum - rightSum))
        leftSum += nums[i]

    return answ


print(leftRightDifference([10, 4, 8, 3]))
