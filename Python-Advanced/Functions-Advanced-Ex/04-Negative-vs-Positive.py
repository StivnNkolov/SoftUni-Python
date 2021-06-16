input_seq = [int(el) for el in input().split()]

positive_nums = sum(filter(lambda x: x >= 0, input_seq))
negative_nums = sum(filter(lambda x: x < 0, input_seq))

print(negative_nums)
print(positive_nums)
if positive_nums > abs(negative_nums):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
