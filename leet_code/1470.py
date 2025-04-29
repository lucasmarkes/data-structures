def shuffle(nums: list[int], n: int) -> list[int]:
  x = nums[0:n]
  y = nums[n:]
  l = []
  
  for i in range(n):
    l.append(x[i])
    l.append(y[i])
    
  return l
      
shuffle([2,5,1,3,4,7], 3)