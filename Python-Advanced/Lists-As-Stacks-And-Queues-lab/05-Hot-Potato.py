from collections import deque

my_queue = deque(input().split())
steps = int(input())

# we set counter to show us how many steps me made
counter = 1

# while loop to iterate until we have only one person left(our winner)
while len(my_queue) > 1:

    # When our counter reach the steps we have from user input we have ro remove the fir kid in our queue
    # this way we make sure that the first kid in the queue is tyhe one that we have to remove
    while not counter == steps:
        my_queue.append(my_queue.popleft())
        counter += 1

    # after we exit our second while loop we have to set the counter to 1 again
    counter = 1

    # we print the kid's name that we removed from our queue
    print(f"Removed {my_queue.popleft()}")

# The last one in our queue is the winner of the game Hot potato
print(f"Last is {my_queue.popleft()}")
