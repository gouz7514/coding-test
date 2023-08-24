# 해시맵
# 이전에 등장했거나 - 해시맵
# 단어가 연결 안되거나 - for 문 순회
def solution(n, words):
    word_dict = dict()
    answer = [0, 0]
    cur_word = ''

    for i in range(len(words)):
        if i == 0:
            cur_word = words[i]
            word_dict[cur_word] = 1
            continue
        
        # 이어지지 않는다면
        if cur_word[-1] != words[i][0]:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        
        # 이미 언급됐다면
        if words[i] in word_dict:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        
        cur_word = words[i]
        # word_dict[cur_word] = 1

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))