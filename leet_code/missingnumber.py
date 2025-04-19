def missingNumber(nums: list[int]) -> int:
  x = set(nums)
  
  for i in range(len(x)+1):
    if i not in x:
      print(i)

  # for i in range(len(nums)+1):
  #   if i not in nums:
  #     print(i)
    
missingNumber([0,1])