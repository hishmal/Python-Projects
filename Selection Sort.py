def sort(nums):
    for i in range(len(nums)):
        min_position = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_position]:
                min_position = j
                nums[i], nums[min_position] = nums[min_position], nums[i]
nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)
