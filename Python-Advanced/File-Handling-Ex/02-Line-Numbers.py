with open("text.txt")as file:
    text = file.readlines()

with open("output.txt", "w") as file:
    for index in range(len(text)):
        current_line = text[index].rstrip()
        number_of_letters = len([el for el in current_line if el.isalnum() and not el.isspace()])
        number_of_punctuation = len([el for el in current_line if not el.isalnum() and not el.isspace()])
        file.writelines(f"Line {index + 1}: {current_line} ({number_of_letters})({number_of_punctuation}) \n")

