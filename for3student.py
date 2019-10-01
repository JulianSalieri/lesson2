school_students = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '3b', 'scores': [4, 5, 5, 2, 3]},
    {'school_class': '5g', 'scores': [2, 3, 3, 4, 5]}
]

scores_sum = 0
for s_school in school_students:
    scores_sum  = scores_sum + sum(s_school['scores']) / len(s_school['scores'])
    s_school = scores_sum / len(school_students)
print(s_school)
for s_klass in school_students:
	s_klass = sum(s_klass['scores']) / len(s_klass['scores'])
	print (s_klass)