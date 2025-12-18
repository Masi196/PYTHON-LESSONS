student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]


# total_s = sum(student_score)
# print(total_s)


# sum = 0
max = 0

# for score in student_score:
#     sum = sum + score

# print(sum)


for score in student_score:
    if score > max:
        max = score
print(max)