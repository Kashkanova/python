tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Борис', 'Маша' ]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9A']
new_list = []

def new_list(tutors,klasses):
    for i,item in enumerate(tutors):
        if i < len(klasses):
            yield (tutors[i], klasses[i])
        else:
            yield (tutors[i], None)

g = new_list(tutors,klasses)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
