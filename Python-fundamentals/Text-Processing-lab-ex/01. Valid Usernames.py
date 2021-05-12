# input_data = input().split(", ")
#
# is_valid = False
#
# for word in input_data:
#     if not 3 <= len(word) <= 16:
#         continue
#     else:
#         is_valid = True
#     for char in word:
#         if not char.isalnum():
#             if char != chr(45) and char != chr(95):
#                 is_valid = False
#             else:
#                 is_valid = True
#     if is_valid:
#         print(word)
#         is_valid = False
#


input_data = input().split(", ")

is_valid = False

for username in input_data:
    if 3 <= len(username) <= 16:
        if username.isalnum() or "-" in username or "_" in username:
            print(username)

