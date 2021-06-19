from fibonacci_04 import create_seq
def check_for_number_in_seq(sequence, number):
    if number in sequence:
        print(f"The number - {number} is at index {sequence.index(number)}")
    else:
        print(f"The number {number} is not in the sequence")


