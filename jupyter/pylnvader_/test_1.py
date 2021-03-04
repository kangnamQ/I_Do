score = 96
grade = []

if score > 100:
    print("다시 설정해 주시기 바랍니다.")
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)