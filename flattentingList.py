def function(nested_list):
    b = []
    for sub_list in nested_list:
             for i in sub_list:
                b.append(i)
    return b
nested_list = [[1, 3, 4], [1], [6, 7],[ 5, 8]]
single_list = function(nested_list)
print("Single list:", single_list)
