import sys
import heapq

def guess_data_structure(operations):
    stack = []
    queue = []
    priority_queue = []
    
    is_stack = True
    is_queue = True
    is_priority_queue = True
    
    for operation in operations:
        if operation[0] == 1:
            x = operation[1]
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)
        elif operation[0] == 2:
            x = operation[1]
            if is_stack:
                if not stack or stack.pop() != x:
                    is_stack = False
            if is_queue:
                if not queue or queue.pop(0) != x:
                    is_queue = False
            if is_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    is_priority_queue = False
    
    if is_stack and not is_queue and not is_priority_queue:
        return "stack"
    if not is_stack and is_queue and not is_priority_queue:
        return "queue"
    if not is_stack and not is_queue and is_priority_queue:
        return "priority queue"
    if not is_stack and not is_queue and not is_priority_queue:
        return "impossible"
    return "not sure"

input_data = sys.stdin.read().strip().split()
index = 0
results = []

while index < len(input_data):
    n = int(input_data[index])
    index += 1
    operations = []
    
    for _ in range(n):
        operation = list(map(int, input_data[index:index + 2]))
        operations.append(operation)
        index += 2
    
    result = guess_data_structure(operations)
    results.append(result)

for result in results:
    print(result)

