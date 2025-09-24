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

    max_area = 0
    lenght: int = 0
    
    for i in range(len(heights)):
        for j in range(lenght + 1, len(heights)):
            if i != j:
                lenght = j - i
                
                if min(heights[i], heights[j]) * lenght > max_area:
                    max_area = min(heights[i], heights[j]) * lenght
        lenght = i
    return max_area

if __name__ == '__main__':

    print(maxArea(heights = [1,8,6,2,5,4,8,3,7]))



