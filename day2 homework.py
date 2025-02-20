def decrease_front_rear():
    """
    front와 rear는 숫자가 감소하지 않고 계속 증가한다.
    이 때 front와 rear가 동시에 size보다 크거나 같으면 %연산을 통해 수를 감소시킴
    :return: x
    """
    global size, front, rear
    if front >= size and rear >= size:
        front = front % size
        rear = rear % size


def is_queue_full() :
    global size, queue, front, rear
    if rear - front == size:
        return True
    else:
        return False


def is_queue_empty() :
    global size, queue, front, rear
    if front == rear:
        return True
    else :
        return False

def en_queue(data) :
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    queue[rear % size] = data
    rear += 1
    decrease_front_rear()

def de_queue() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    data = queue[front % size]
    queue[front % size] = None
    front += 1
    decrease_front_rear()
    return data

def peek() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front % size]

def printqueue(queue):
    """
    queue에 들어가고 나오는 것이 더 잘 보이도록 printqueue함수 정의
    front부터 rear까지 출력하는 방식
    :param queue: queue
    :return: x
    """
    global size, front, rear
    print("[", end = '')
    for i in range(front,rear):
        print(queue[i % size], end = '')
        if i != rear - 1:
            print(end = ', ')
    print("]")

size = int(input("큐의 크기를 입력 : "))
queue = [None for _ in range(size)]
front = rear = 0

if __name__ == "__main__" :
    while True:
        menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
        if menu == 'X' or menu == 'x':
            break
        elif menu== 'E' or menu == 'e' :
            data = input("입력할 데이터 : ")
            en_queue(data)
            printqueue(queue)
        elif menu== 'D' or menu == 'd' :
            print("삭제된 데이터 : ", de_queue())
            printqueue(queue)
        elif menu== 'P' or menu == 'p' :
            print("확인된 데이터 : ", peek())
            printqueue(queue)
        else:
            print("입력이 잘못됨")
    print("프로그램 종료!")