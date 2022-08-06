def main():
    nums = [1,2,3,1]
    nums = [1,2,3,4]
    print(check_duplicate(nums))


def check_duplicate(nums):
    dict_nums = {}
    for num in nums:
        try:
            k = dict_nums[num]
            return True
        except:
            dict_nums[num] = 1
    return False

main()