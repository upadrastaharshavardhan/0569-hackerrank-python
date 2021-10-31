def get_set():
    return set(map(int, input().split()))


queries = int(input())

for _ in range(queries):
    input()
    A = get_set()
    input()
    B = get_set()
    print(A.issubset(B))
