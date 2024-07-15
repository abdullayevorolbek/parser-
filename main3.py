def check_empty_or_not(my_list):
    if not my_list:
        return "Ro'yhat bo'sh"
    else:
        return "Ro'yhat bo'sh emas"

list1 = []  
list2 = [1, 2, 3]  

print(check_empty_or_not(list1))  # Output: Ro'yhat bo'sh
print(check_empty_or_not(list2))  # Output: Ro'yhat bo'sh emas
