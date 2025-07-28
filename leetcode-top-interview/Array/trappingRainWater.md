# 42. Trapping Rain Water

## 나의 풀이
- 힌트 보고 풀음
  - 왼쪽 최대 배열, 오른쪽 최대 배열 구하기
- 시간 복잡도 O(n)
- 공간 복잡도 O(n)

## 베스트 솔루션은?
- 투 포인터 방식을 이용해 공간을 O(1)으로 줄이기
```python
class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        answer = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    answer += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    answer += right_max - height[right]
                right -= 1
        return answer
```