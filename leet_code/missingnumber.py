def missingNumber(nums: list[int]) -> int:
  for i in range(len(nums)+1):
    if i not in nums:
      print(i)
    
missingNumber([9,6,4,2,3,5,7,0,1])