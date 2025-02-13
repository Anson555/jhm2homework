size = int(input("Input Addition Table Size smaller 10: "))

print("Addition Table")
print("-------------------------------------------------------")
for i in range(1, size + 1):
    for j in range(1, size + 1):
        sum_ij = i + j
        if sum_ij < 10:
            print(f"{i} + {j} = {sum_ij}  ", end=" ")
        else:
            print(f"{i} + {j} = {sum_ij} ", end=" ")
    print()

print("-------------------------------------------------------")
