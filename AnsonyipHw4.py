heights = []
total_students = 4
for i in range(1, total_students + 1):
    while True:
        height = float(input(f"Input the height of student {i} in cm: "))
        if height < 0:
            print("Height must be positive.")
        elif height > 200:
            print("Height is greater than 200cm.")
        else:
            heights.append(height)
            break

average_height = sum(heights) / total_students
max_height = max(heights)
print("End of input.")
print(f"The average height of these students is {average_height:.2f} cm.")
print(f"The maximum height of these students is {max_height:.2f} cm.")
