""" Декартово произведение это когда вы каждый элемент 
из одного множества группируете с
 каждым элементом другого множества
"""

colors = ['red', 'green']
sizes = ['S', 'M', 'L']

result = [(i,j) for i in colors for j in sizes ]


print(result)

