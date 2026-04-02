def fast_pow(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
    return result

# Находим остаток от деления 3^4567 на 193
remainder = fast_pow(3, 4567, 193)
print(remainder)
