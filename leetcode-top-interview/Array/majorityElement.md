# 169. Majority Element

## Hint
- How you could "icnrease" or "decrease" a count as you go
- linear time complexity means you can only iterate through the array once
- `O(1)` space complexity means you can only use a constant amount of extra space

## Solution
- Boyer-Moore majority vote algorithm
- Initialize two variables: `candidate` and `count`
- Iterate through the array
- If the current element is the same as the `candidate`, increment the `count`
- If the current element is different from the `candidate`, decrement the `count`
- If the `count` is 0, update the `candidate` to the current element and set the `count` to 1
- Return the `candidate`

## Code
```python
class Solution(object):
    def majorityElement(self, nums):
        candidate, count = 0, 0
        
        for i in range(len(nums)):
            if not count:
                candidate = nums[i]
                count += 1
                continue
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate
```

## Little Tweak
- What if it's not guaranteed that the majority element exists?
- We can use a hashmap to count the occurrences of each element
- Then we can iterate through the hashmap and return the element with the highest count
- This will give us the majority element if it exists, otherwise it will return the element with the highest count

```python
class Solution(object):
    def majorityElement(self, nums):
        count = {}
```

OR

```python
class Solution(object):
    def majorityElement(self, nums):
        # Step 1: Find candidate using Boyer-Moore
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify the candidate
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return None  # No majority element
```