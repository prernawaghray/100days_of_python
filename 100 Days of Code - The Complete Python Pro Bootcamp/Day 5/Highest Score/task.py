student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
total_score = sum(student_scores)
print(total_score)

new_scores = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for i in new_scores:
    if i > max_score:
        max_score = i
print(max_score)