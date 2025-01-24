def calculate_total_difficulty(M, N, difficulties):
    MOD = 10**9 + 7
    
    #calculating XOR of all difficulties
    X = 0
    for d in difficulties:
        X ^= d
    
    #if M is even, total difficulty is 0
    if M % 2 == 0:
        return 0
    else:
        return X % MOD


M, N = map(int, input().strip().split())
difficulties = list(map(int, input().strip().split()))

print(calculate_total_difficulty(M, N, difficulties))
