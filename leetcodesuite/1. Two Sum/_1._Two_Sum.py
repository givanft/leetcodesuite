def two_sum(nums, target):
    
    dict_nums = {}
    
    for i, num in enumerate(nums):
        if dict_nums.get(num) == None:
            dict_nums[num] = i
        else:
            if num * 2 == target:
                return [dict_nums[num], i]

    for k, v in dict_nums.items():
        remainder = target - k
        try:
            rem_value = dict_nums[remainder]

            if v == rem_value: 
                continue
            else:
                return [v, rem_value]
        except:
            continue

nums = [2,7,11,15] #
target = 9

#nums = [3,3]
#target = 6
#
#nums = [3,2,4]
#target = 6

print(two_sum(nums, target))
