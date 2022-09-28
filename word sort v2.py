array = ['job', 'jam', 'orange', 'apple', 'java',
         'oregano', 'box', 'card', 'camera']


def sort(arr):
    no_of_pass = 0
    arr = arr.copy()  # make a deep copy of mutable list

    for i in range(1, len(arr)):  # iteration of each item in arr

        j = i  # index of the str item

        k = 0  # index of char in str

        # check for -ve arr index and str index greater than the len of the smallest str
        while j > 0 and k < min(len(arr[j - 1][k]), len(arr[j][k])):    # insertion sort method
            print(0, arr[j - 1], arr[j], k, j)
            if arr[j - 1][k] > arr[j][k]:   # if prev item lst is greater than the successive
                print(1, arr[j - 1], arr[j])
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # swap
                k = 0
                j -= 1      # next iteration
            else:  # if the str at index k is same

                print(arr[j-1][k], arr[j][k])
                k += 1  # next iteration
            no_of_pass += 1

    return arr, no_of_pass


print(sort(array))
