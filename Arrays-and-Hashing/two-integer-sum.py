def twoSum(nums, target):
    start = 0;
    end = len(nums) -1;
    left = start;
    right = end;

    while end > left:
        if (right == left):
            right = end;
            left += 1;
            continue;

        if (nums[left] + nums[right] == target):
            return ([left, right]);

        right -= 1;


print(twoSum([3, 4, 5, 6], 7));