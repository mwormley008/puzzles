import math
def adjacent_element_product(array):
    product_list = -math.inf
    print(array)
    for i,j in enumerate(array):
        if i < len(array)-1 and array[i] * array[i+1] > product_list:
            product_list = array[i] * array[i+1]
    return product_list