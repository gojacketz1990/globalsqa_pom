import time

def calculate(iterations, param1, param2):
    result = 1.0
    for i in range(1, iterations+1):
        j = i * param1 - param2
        result -= (1/j)
        j = i * param1 + param2
        result += (1/j)
    return result

start_time = time.time()
#result = calculate(100_000_000, 4, 1) * 4
result = calculate(100, 4, 1) * 4
end_time = time.time()

print(f"Result: {result:.12f}")
print(f"Execution Time: {(end_time - start_time):.6f} seconds")

def calculate_pairs(num_list, sum_total):
    return_array = []
    sorted_list = sorted(set(num_list))
    for i in range(len(sorted_list)):
        for j in range(i+1,len(sorted_list)):
            if (sorted_list[i] + sorted_list[j] == sum_total):
                return_array.append([sorted_list[i],sorted_list[j]])
    return return_array

print(calculate_pairs([4, 4, 4, 31, 2, 5, 6, 3, 3, 1,7,3,5,4, 2, 7, 4, 1, 6, 5, 3, 9, 11],8))

