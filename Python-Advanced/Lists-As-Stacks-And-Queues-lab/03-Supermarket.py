from collections import deque

# We create "constants" for the commands we can receive from the user's input
END_COMMAND = "End"
PAID_COMMAND = "Paid"

# We create our queue where we are about to store the workers name
workers_queue = deque()


while True:
    input_data = input()

    # if we receive End we print the count of people in our queue and break form the loop
    if input_data == END_COMMAND:
        print(f"{len(workers_queue)} people remaining.")
        break

    # If we receive Paid we create for loop to popleft the workers in the current queue (FIFO)
    elif input_data == PAID_COMMAND:
        for index in range(len(workers_queue)):
            print(workers_queue.popleft())

    # in every other case we have to append our queue with the name we receive from the user input
    else:
        workers_queue.append(input_data)
