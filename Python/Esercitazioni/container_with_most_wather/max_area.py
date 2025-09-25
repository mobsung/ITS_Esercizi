'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

 

Example 1:

Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: heights = [1,1]
Output: 1

'''


def maxArea(heights: list[int]) -> int:

    left: int = 0
    right: int = len(heights) - 1

    max_area: int = 0
    
    while left < right:
        lenght: int = right - left
        if min(heights[left], heights[right]) * lenght > max_area:
            max_area = min(heights[left], heights[right]) * lenght
        else:
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        

    return max_area

if __name__ == '__main__':

    print(maxArea(heights = [1,8,6,2,5,4,8,3,7]))



