# 134. Gas Station
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        ans = -1
        for i in range(len(gas)):
            if cost[i] > gas[i]:
                continue
            current_gas = gas[i]
            c = 0 if i == len(gas) - 1 else i + 1
            while True:
                current_gas -= cost[-1 if c == 0 else c - 1]
                if current_gas < 0:
                    break
                current_gas += gas[c]
                if c == i:
                    ans = c
                    break
                c = 0 if c == len(gas) - 1 else c + 1
            if ans != -1:
                break
        return ans

# by claude
# 일단 순회 가능한지 확인
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # 1. 전체 가스량이 전체 비용보다 적으면 불가능
        if sum(gas) < sum(cost):
            return -1
        
        # 2. 한 번의 순회로 시작점 찾기
        total_tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # 현재까지의 가스가 음수가 되면
            # i+1 지점을 새로운 시작점으로 설정
            if total_tank < 0:
                start = i + 1
                total_tank = 0
        
        return start

if __name__ == "__main__":
    solution = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = solution.canCompleteCircuit(gas, cost)
    print(result)