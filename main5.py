def replace_and_insert(input_list, index):
    if index >= 0 and index < len(input_list):
        input_list[index] = 'changed'
    return input_list

# Example usage:
input_list = ["Bran", 11, 22, 33, 'Stark', 22,] 
