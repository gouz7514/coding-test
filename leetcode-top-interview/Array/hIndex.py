# 274. H-Index
# class Solution(object):
#     def hIndex(self, citations):
#         citations.sort()
#         if sum(citations) == 0:
#             return 0
#         arr = [0] * (len(citations) + 1)
#         h = 0
#         for i in range(1, len(arr), 1):
#             for j in range(len(citations)):
#                 if citations[j]:
#                     if citations[j] >= i and len(citations) - j >= i:
#                         arr[i] = len(citations) - j
#                         h = arr[i]
#         return h   

class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            # 지금까지 본 갯수
            view = i + 1
            if citations[i] >= view:
                h = view
            else:
                break
        return h

if __name__ == "__main__":
    solution = Solution()
    citations = [1,3,1]
    result = solution.hIndex(citations)
    print(result)