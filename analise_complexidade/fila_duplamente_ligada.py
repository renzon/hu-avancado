from collections import deque

dq = deque(range(1000))
dq.append(1)  # O(1)
print(dq[1])  # O(n)
dq.sort()  # O(n*log(n))
dq.pop()  # O(1)
dq.popleft()  # O(1)
dq.insert(0, 1)  # O(n)
print(1 in dq)  # O(n)
del dq[0]  # O(1)
