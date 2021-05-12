# words = input().split()
# searched_palindrome = input()
#
# palindrome_list = [palindrome for palindrome in words if palindrome == palindrome[::-1]]
# # searched_palindrome_list = [searched for searched in palindrome_list if searched == searched_palindrome]
# print(palindrome_list)
# print(f"Found palindrome {words.count(searched_palindrome)} times")

words = input().split()
searched_palindrome = input()

palindrome_list = []
for palindrome in words:
    if palindrome == palindrome[::-1]:
        palindrome_list.append(palindrome)
print(palindrome_list)
print(f"Found palindrome {words.count(searched_palindrome)} times")
