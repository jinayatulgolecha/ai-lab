# Magic Square - Simple Version (only odd n)

n = int(input("Enter odd n: "))
magic = [[0]*n for _ in range(n)]

i, j = 0, n//2

for num in range(1, n*n + 1):
    magic[i][j] = num
    ni, nj = (i-1) % n, (j+1) % n
    
    if magic[ni][nj]:
        i = (i+1) % n
    else:
        i, j = ni, nj

for row in magic:
    print(row)