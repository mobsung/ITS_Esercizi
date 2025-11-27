'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
'''


def singleNumber(nums: list[int]) -> int:
        
        left, rigth = 0, len(nums) - 1
        result: int = nums[0]

        while left < rigth:
            if result == nums[left + 1]:
                result = nums[left + 1]
            else:
                result = nums[-1]
            left += 1
            #rigth -= 1
    
        
        return result


print(singleNumber([4,1,2,1,2]))