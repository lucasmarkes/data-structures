def majorityElement(nums: list[int]) -> int:
  medium = len(nums) / 2
  viewed = {}

  for i in range(0, len(nums)):
    if nums[i] in viewed:
      viewed[nums[i]] += 1
    else:
      viewed[nums[i]] = 1
      
    if viewed[nums[i]] > medium:
      return nums[i]

print(majorityElement([2,2,1,1,1,2,2]))