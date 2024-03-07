def f(n):
# se n=1, retorna 0 pq o primeiro termo é 0
# se n=2, retorna 1 pq o segundo termo é 1 
    if n == 1:
        return (0)
    if n == 2:
        return (1)
    if n > 2:
        return (f(n-1) + f(n-2))
    
n = int(input('Quantos elementos? '))

for i in range(1, n):
        print(f(i))
