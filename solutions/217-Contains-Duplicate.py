class Solution:
	def hasDuplicate(self, nums: List[int]) -> bool:
		dup = []
		for num in nums: 
			if num in dup: #Checks if the number has already been in dup 
				return True #if it has, return True for dup
			dup.append(num) #if not, add the number to the set
		return False # if no duplicate were found, return False
