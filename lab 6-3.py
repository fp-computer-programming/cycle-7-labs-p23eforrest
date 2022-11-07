# Author: EAF 11/7/22
from re import A


colors = ['green', 'blue', 'orange', 'red']
colors.extend(["yellow", 'purple', 'pink'])
colors.append("gold")
colors.insert(3, 'brown')
a = colors[:]
a.remove('pink')
print(a)