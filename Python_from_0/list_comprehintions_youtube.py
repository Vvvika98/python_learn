# labelled_numbers = []
numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num % 2 == 0:
#         labelled_numbers.append("even")
#     else:
#         labelled_numbers.append("odd")


#можно все это запихнуть в ЛК 

labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]

print(labelled_numbers)

#------------------------------------------------------------------------------------

#ЛК для словаей 

square_dict = {x : x ** 2 for x in range(10)}

print(square_dict)


#------------------------------------------------------------------------------------

#ТРАНСПОНИРОВАНИЕ МАТРИЦЫ (столбцы сделать строками, а строки столбцами)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpose_matrix = [] #создаем пустой список, куда засунем транспонированную матрицу 

#вариант с циклом for
for i in range(len(matrix)):  #0,1,2
    transpose_row = []   #ряд
    for row in matrix:
        transpose_row.append(row[i]) #1,4,7,2,5,8,3,6,9
    transpose_matrix.append(transpose_row)

#вариант с Лист компрехеншенс

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix)