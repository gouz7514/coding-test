import heapq

def solution(operations):
    heap = []
    heapq.heapify(heap)
    answer = []

    for operation in operations:
        i, number = operation.split(' ')
        number = int(number)

        if i == 'I':
            heapq.heappush(heap, number)
        elif i == 'D':
            if len(heap) == 0: continue
            if number == 1:
                heap = list(heap)[:-1]
                heapq.heapify(heap)
            elif number == -1:
                heapq.heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        smallest = heap[0]
        largest = sorted(heap)[-1]
        answer = [largest, smallest]
    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))