def solution(n, times):
    answer = 0
    times.sort()
    low, high = 0, times[-1] * n
    
    if len(times) == 1:
        answer = n * times[0]
    else:
        while low <= high:
            mid = (low + high) // 2
            cnt = 0
            
            for time in times:
                cnt += mid // time
            print('mid, cnt : ', mid, cnt)
                
            if cnt >= n:
                high = mid - 1
                answer = mid
            else:
                low = mid + 1
                answer = max(answer, mid)
            # answer = mid
    return answer

n = 6
times = [7, 10]
print(solution(n, times))