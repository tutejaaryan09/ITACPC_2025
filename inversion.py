def merge_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = merge_count_inversions(arr[:mid])
    right, right_inv = merge_count_inversions(arr[mid:])
    
    merged = []
    inv = left_inv + right_inv
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv

def count_inversions(arr):
    _, inv = merge_count_inversions(arr[:])
    return inv

def compose(p, r):
    return [p[r[i] - 1] for i in range(len(p))]

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pos_p = [0] * (n + 1)
pos_q = [0] * (n + 1)

for i in range(n):
    pos_p[p[i]] = i
    pos_q[q[i]] = i

values = list(range(1, n + 1))
values.sort(key=lambda x: (pos_p[x] + pos_q[x], pos_p[x]))

r = [0] * n
for i in range(n):
    r[i] = values[i]

p_r = compose(p, r)
q_r = compose(q, r)

inv_p = count_inversions(p_r)
inv_q = count_inversions(q_r)
print(inv_p)

print(min(inv_p, inv_q))
print(' '.join(map(str, r)))
