def productExceptSelf(nums):
    map = {}
    results = [];

    for i, _ in enumerate(nums):
        running = None;
        for j, value in enumerate(nums):
            if i == j:
                continue;
            if running == None:
                running = value;
                continue;
            if i != j:
                running = running * value;
        results.append(running);

    return (results);


# print(productExceptSelf([1,2,4,6]));
print(productExceptSelf([-1, 0, 1, 2, 3]));
