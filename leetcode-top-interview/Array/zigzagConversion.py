# 6. ZigZag Conversion
# 23ms, Beats 31.31%
# Correct, but the performance issue mainly comes from
# 1. Styling concatenation in loop
# 2. TOo many condition checks per character
class Solution(object):
    def convert(self, s, numRows):
        a = [''] * numRows
        # current locaiton
        c = 0
        # direction (left = True, right = False)
        d = True
        for i in range(len(s)):
            # 일단 현재 위치에 문자 추가
            a[c] += s[i]
            # 정방향인 경우 그냥 진행
            if numRows == 1:
                continue
            if c == 0:
                if not d:
                    d = True
                c += 1
            elif c == numRows - 1:
                if d:
                    d = False
                c -= 1
            else:
                if d:
                    c += 1
                else:
                    c -= 1
        return ('').join(a)
    
# more improved version - same concept, but escape condition is declared at the begining
class Solution(object):
    def convert(self, s, numRows):
        # escape unnecessary operation
        if len(s) == 1 or numRows == 1:
            return s
        
        a = [''] * numRows
        # current locaiton
        c = 0
        # direction (left = True, right = False)
        d = True
        for i in range(len(s)):
            # 일단 현재 위치에 문자 추가
            a[c] += s[i]
            # 정방향인 경우 그냥 진행
            if c == 0:
                if not d:
                    d = True
                c += 1
            elif c == numRows - 1:
                if d:
                    d = False
                c -= 1
            else:
                if d:
                    c += 1
                else:
                    c -= 1
        return ('').join(a)

# BY gpt
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        curRow, step = 0, 1

        for ch in s:
            rows[curRow].append(ch)
            if curRow == 0:
                step = 1
            elif curRow == numRows-1:
                step = -1
            curRow += step

        return ''.join([''.join(row) for row in rows])

# I want more
# Avoid repeated string concatenation
# Use lists to build strings, then join at the end
# Minimize condition checks
# ↓ by claude (Amazing.....)
class Solution(object):
    def convert(self, s, numRows):
        # Handle edge cases
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Create result array
        rows = [''] * numRows
        
        # Calculate cycle length: down + up (excluding corners counted twice)
        cycle_len = 2 * numRows - 2
        
        # Process each character
        for i, char in enumerate(s):
            # Find position within current cycle
            cycle_pos = i % cycle_len
            
            # Determine which row this character belongs to
            if cycle_pos < numRows:
                # Going down: row index = cycle position
                row = cycle_pos
            else:
                # Going up: row index = total rows - (position - numRows) - 2
                row = numRows - (cycle_pos - numRows + 1) - 1
            
            rows[row] += char
        
        return ''.join(rows)

if __name__ == "__main__":
    solution = Solution()

    s = "PAYPALISHIRING"
    numRows = 4
    result = solution.convert(s, numRows)
    print(result)