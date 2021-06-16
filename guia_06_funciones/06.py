def es_primo(num):
    count = 0
    for i in range(2, num+1):
        if num % i == 0:
            count = count + 1
    if count > 1:
        return 0
    else:
        return 1

print(es_primo(4))