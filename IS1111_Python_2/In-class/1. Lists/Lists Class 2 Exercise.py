# Client: "TechFix Solutions"
# Request: We need a system to manage our customer support line.
#
# BUSINESS RULES:
# 1. Standard customers join the BACK of the line.
# 2. VIP members (paying subscribers) skip to the FRONT of the line.
# 3. Our agents always serve the FIRST person in the line.
# 4. Sometimes customers get impatient and hang up; we need to 
#    remove them by name, no matter where they are in the line.
# 5. We need to print a numbered list of who is currently waiting.


# lists_class2_live_scaffold.py

# We need to Add, Serve (Remove), and Cancel customers.

def add_customer(queue, name, vip=False):
    """
    If vip insert at front 
    Otherwise, add to end.
    """
    if vip == True:
        queue.insert(0, name)
    else:
        queue.append(name)


def serve_next(queue):
    """
    Remove front customer and give their name.
    If empty, return None.
    """
    if queue == []:
        return None
    else:
        return queue.pop(0)


def cancel_customer(queue, name):
    """
    Remove a customer by VALUE.
    Must check first to avoid crashing.
    """
    if name in queue:
        queue.remove(name)


def show_queue(queue):
    """
    Print numbered list using a loop. If empty say it.
    """
    if queue == []:
        print("The queue is currently empty.")
    else:
        for i in range(len(queue)):
            print(f"{i+1}. {queue[i]}")


q = []

 
# 1. Add "Ben", "Amy", "Dan"
# 2. Add "VIP Owner" (vip=True)
# 3. show_queue(q)

# 4. Serve the next person (print who it was)
# 5. Cancel "Amy"
# 6. show_queue(q)

add_customer(q, "Ben")
add_customer(q, "Amy")
add_customer(q, "Dan")
add_customer(q, "VIP Owner", vip=True)
show_queue(q)

served = serve_next(q)
print(f"Served: {served}")
cancel_customer(q, "Amy")
show_queue(q)