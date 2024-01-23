def is_k_rising(numbers, k):
    for i in range(0, len(numbers)):
        if i + k > len(numbers) - 1: return True
        if numbers[i] >= numbers[i + k]: return False

def find_all_ks(numbers):
    result = [(k, is_k_rising(numbers, k)) for k in range(1, len(numbers))]
    result = [x[0] for x in result if x[1]]
    return result

print(find_all_ks([1, 2, 3, 4, 5, 6, 7, 0, 8, 9, 10, 0, 11, 45, 12, 13, 93, 14]))