list_of_nums = [1, 5, 8, 9, 4, 6]


def bubble_sort(nums):
    swapped = True
    count = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
                swapped = True
    print(count)


# bubble_sort(list_of_nums)
print(list_of_nums)


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        print(nums[i], nums[i + 1:])
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                print(nums[j], nums[i])
                lowest_value_index = j
                nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


selection_sort(list_of_nums)
print(list_of_nums)
# TODO разобраться с пузырьковой сортировкой, написать функиюб которая сортирует список строк.
