N, K = map(int, input().split())

weights = []
values = []
weights_n_values = []

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)
    weights_n_values.append([W, V])