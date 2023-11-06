def even_numbers(arr,n):
    even_list = [x for x in arr if x % 2 == 0]
    print(even_list)
    return even_list[len(even_list)-n::]