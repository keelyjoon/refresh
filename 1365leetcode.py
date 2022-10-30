"""
input: nums = [8, 1, 2, 2, 3]
output: [4, 0, 1, 1, 3]
"""

# time complexitiy of O(n^2)
def solution(nums):
# create a list to store the output of the count
    output = []
    # for the length of the list
    for i in range(len(nums)):
        # create count variable  
        count = 0
        # for the length of the list
        for j in range(len(nums)):
            # if j does not equal i AND the number at index j is less than the number at index i
            if j != i and nums[j] < nums[i]:
                # add one to count
                count += 1
        # add the count varaible on to the output list
        output.append(count)
    # print the output list to the terminal
    print(output)

#solution([4, 0, 1, 1, 3])




