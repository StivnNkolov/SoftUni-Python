input_string = input().split()

input_data = input()

while not input_data == "Stop":
    current_command = input_data.split()
    if current_command[0] == "Delete":
        index_to_remove = int(current_command[1]) + 1
        if index_to_remove in range(len(input_string)):
            input_string.pop(index_to_remove)
    elif current_command[0] == "Swap":
        first_word = current_command[1]
        second_word = current_command[2]
        if first_word in input_string and second_word in input_string:
            first_word_index = input_string.index(first_word)
            second_word_index = input_string.index(second_word)
            input_string[first_word_index], input_string[second_word_index] = input_string[second_word_index], input_string[first_word_index]
    elif current_command[0] == "Put":
        word_to_add = current_command[1]
        index_to_use = int(current_command[2]) - 1
        if index_to_use in range(len(input_string)):
            if index_to_use - 1 in range(len(input_string)):
                last_element = input_string[-1]
                last_element_index = input_string.index(last_element)
                if index_to_use == last_element_index:
                    input_string.append(word_to_add)
                else:
                    input_string.insert(index_to_use, word_to_add)
        else:
            input_data = input()
            continue
    elif current_command[0] == "Sort":
        input_string.sort(reverse=True)
    elif current_command[0] == "Replace":
        first_word = current_command[1]
        second_word = current_command[2]
        if second_word in input_string:
            index_to_usee = input_string.index(second_word)
            input_string[index_to_usee] = first_word
    input_data = input()
print(" ".join(input_string))
