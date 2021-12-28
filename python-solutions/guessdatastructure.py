import sys

def check_stack(input_list, ret):
    if len(input_list) == 0:
        return False, input_list
    if ret == input_list.pop():
        return True, input_list
    return False, input_list


def check_queue(input_list, ret):
    if len(input_list) == 0:
        return False, input_list
    if ret == input_list.pop(0):
        return True, input_list
    return False, input_list


def check_pri_q(input_list, ret):
    if len(input_list) == 0:
        return False, input_list
    m = max(input_list)
    input_list.remove(m)
    if ret == m:
        return True, input_list
    return False, input_list


def main():
    inp = 0
    while True:
        stack_list = []
        pri_q_list = []
        queue_list  = []
        stack = True
        pri_q = True
        queue = True
        try:
            inp = int(input())
        except EOFError:
            break
        for i in range(inp):
            func, val= map(int, input().split())
            if func == 1:
                stack_list.append(val)
                pri_q_list.append(val)
                queue_list.append(val)
            else:
                if stack:
                    stack, stack_list = check_stack(stack_list, val)
                if pri_q:
                    pri_q, pri_q_list = check_pri_q(pri_q_list, val)
                if queue:
                    queue, queue_list = check_queue(queue_list, val)
        if (stack and pri_q) or (stack and queue) or (queue and pri_q):
            print('not sure')
        elif stack:
            print('stack')
        elif queue:
            print('queue')
        elif pri_q:
            print('priority queue')
        else:
            print('impossible')



if __name__ == '__main__':
    main()