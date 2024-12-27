def hasDuplicate(nums) -> bool:
    dict = {};

    for num in nums:
        if num in dict:
            return True;
        dict[num] = 1;

    return False;


print(hasDuplicate([1, 2, 3, 2]));