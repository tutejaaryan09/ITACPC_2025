n = int(input())
cor = []
for _ in range(n):
    x, y = map(int, input().split())
    cor.append((x, y))

cor_set = set(cor)
cor.sort()

count = 0
for x, y in cor:
    d = 1
    while (x + d, y + d) in cor_set:
        count += 1
        d += 1

print(count)


