def palindrome_or_not(list):
    for index in range(len(list)):
        if list[index] == list[index][::-1]:
            print("True")
        else:
            print("False")


list_of_integers_as_string = input().split(", ")
palindrome_or_not(list_of_integers_as_string)
