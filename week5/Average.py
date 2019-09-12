def average(nums):
    length = len(nums)
    if (length == 0):
        print("The average doesn't exist!")
        return
    else:
        all_sum = sum(nums)
        average = all_sum/length
        print(average)
        answer_tuple = []
        result = []
        i = 0
        while i < length:
            answer_tuple.append(abs(nums[i] - average))
            i += 1
        max_difference = answer_tuple[0]
        j = 0

        while j < length:
            if (answer_tuple[j] >= max_difference):
                max_difference = answer_tuple[j]
                max_index = j
            j += 1

        result.append(max_index)
        result.append(nums[max_index])
        return result

ls = [5, 3, 2, 4, 10]
tup = average(ls)
print(tup[0], tup[1])
