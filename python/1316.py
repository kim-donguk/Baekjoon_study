# 1316번
# 그룹 단어 체커
cnt = 0
count = int(input())

for i in range(count):
    word = raw_input()
    cnt += list(word) == sorted(word, key = word.find)

print(cnt)
