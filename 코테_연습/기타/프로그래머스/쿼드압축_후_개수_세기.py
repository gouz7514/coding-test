# 나의 풀이
def solution(arr):
    answer = [0, 0]

    initial_total = 0
    for row in arr:
        for value in row:
            initial_total += value

    if initial_total == 0:
        return answer
    elif initial_total == len(arr[0]) ** 2:
        return [0, 1]

    def compress(arr):
        total = 0
        for row in arr:
            for value in row:
                total += value

        if total == 0:
            return [0]
        elif total == len(arr[0]) ** 2:
            return [1]
        else:
            if len(arr[0]) == 2:
                return arr
            else:
                return divide_array(arr)
            
    def divide_array(arr):
        rows = len(arr)
        cols = len(arr[0])

        half_rows = rows // 2
        half_cols = cols // 2

        subarrays = []
        for i in range(0, rows, half_rows):
            for j in range(0, cols, half_cols):
                subarray = [row[j:j+half_cols] for row in arr[i:i+half_rows]]
                subarrays.append(subarray)

        for subarray in subarrays:
            result = compress(subarray)
            if result is not None:
                if type(result[0]) is int:
                    answer[result[0]] += 1
                else:
                    flat_array = [e for l in result for e in l]
                    for i in flat_array:
                        answer[i] += 1
        
    divide_array(arr)

    return answer

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
arr = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(solution(arr))

# 다른 사람의 풀이
def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer