i=range(1,10)
even_count, odd_count = 0, 0
for num in i:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("number of even numbers:", even_count)
print("number of odd numbers: ", odd_count)