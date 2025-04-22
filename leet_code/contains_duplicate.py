def containsDuplicate( nums: list[int]) -> bool:
  viewed = set()
  for i in nums:
      if i in viewed:
          return True
      viewed.add(i)
  return False

print(containsDuplicate([1,2,3]))