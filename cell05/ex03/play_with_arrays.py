original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
order = [24, 10, 11, 50]
for num in original_array:
    if num > 5 and num + 2 in order:
        if num + 2 not in new_array:
            new_array.append(num + 2)

final_array = []
for num in order:
    if num in new_array:
        final_array.append(num)

print(original_array, "$")
print(final_array, "$")