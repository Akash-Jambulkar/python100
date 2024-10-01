# Given : TWO SUMS
# nums as an array 
# target as an integer
# return indices of the two digits whose sum is target
# :: no repeatition of the numbers
# :: inputs have only one solution

def TwoSums(nums : list[int], target : int):
    #creating a dict to store the diff : 
    seen =  {} 

    for i in range (len(nums)):
        #if x + y = target ---> y = target - x
        diff = target - nums[i]
        #if diff is in seen dict then return the indices of diff and nums[i]
        if diff in seen : 
            return [seen[diff],i]
        #else add nums[i] to seen dict with its index
        else: 
            seen[nums[i]]=i

    