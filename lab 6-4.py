#Author: EAF 11/8/22
subjects = ['government', 'programming', 'literature']
#creates a variable of the list
subjects.append('spanish')

value = subjects.index('spanish')
print(value)

subjects.sort()
print(subjects)
subjectcopy = subjects[:]
subjectcopy.reverse()
print(subjectcopy)