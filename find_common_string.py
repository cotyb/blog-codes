def partition(suffix_array, start, end):
    if end <= start:
        return
    index1, index2 = start, end
    base = suffix_array[start]
    while index1 < index2 and suffix_array[index2] >= base:
        index2 -= 1
    suffix_array[index1] = suffix_array[index2]
    while index1 < index2 and suffix_array[index1] <= base:
        index1 += 1
    suffix_array[index2] = suffix_array[index1]
    suffix_array[index1] = base
    partition(suffix_array, start, index1 -  1)
    partition(suffix_array, index1 + 1, end)

def find_common_string(str1, str2):
    if not str1 or not str2:
        return 0, ''
    index1, index2 = 0, 0
    length, comm_substr = 0, ''
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] == str2[index2]:
            length += 1
            comm_substr += str1[index1]
        else:
            break
        index1 += 1
        index2 += 1
    return length, comm_substr

def find_longest_repeating_strings(string):
    if not string:
        return None, None
    suffix_array = []
    # first, get the suffix arrays
    length = len(string)
    for i in range(length):
        suffix_array.append(string[i:])
    # second, sort suffix array
    start, end = 0, len(suffix_array) - 1
    partition(suffix_array, start, end)
    # third, get the longest repeating substring
    print suffix_array
    max_length,  repeat_substring = 0, ''
    for i in range(len(suffix_array) - 1):
        common_len, common_substring = find_common_string(suffix_array[i], suffix_array[i+1])
        if common_len > max_length:
            max_length, repeat_substring = common_len, common_substring
    return max_length, repeat_substring








# if __name__ == "__main__":
#     string = "Ask not what your country can do for you, but what you can do for your country"
#     length, substr = find_longest_repeating_strings(string)
#     print length, substr

