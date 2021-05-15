import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add():
    cellnumber = input("Write the cellphone number: ")
    # print(number)
    queue.enqueue(cellnumber)
    print("The cellphone number added was: "+cellnumber)

def dequeue():
    # print(queue.get_queue())
    number = queue.dequeue()
    # print(number)
    send(body="Go to your place, thank you!", to=str(number))
    # print(queue.get_queue())
    print("Confirmation! Deleted: "+number)

def save():
    # print(queue.get_queue())
    _queue = queue.get_queue()
    with open('queue.json', 'w') as json_file:
        json.dump(_queue, json_file)
    json_file.close()
    print("List saved:")
    print(_queue)

def load():
    global queue
    with open('queue.json', 'r') as json_file:
        json_object = json.load(json_file)
    json_file.close()
    print("List loaded:")
    print(json_object)
    queue = Queue(mode="FIFO",current_queue=json_object)
    # print(queue)

print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number: "))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
