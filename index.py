####
# notas = [6,7,8,9,10]
# b10 = []

# for nota in notas:
#     b10.append(nota * 10)

# b10
####
n=5

def factorial(n):
    last, next = 1, 1
    while next <= n:
        last, next = next*last, next + 1
    return last


print(factorial(5), n)
####