def bank(X, Y):
    
    total = X
    
    percent = 0.10  # 5% годовых
    
    for _ in range(Y):
        total += total * percent
    
    return total

X = 1000  # Размер вклада в рублях
Y = 5     # Срок вклада в годах
result = bank(X, Y)
print("Сумма на счету пользователя через", Y, "года:", result, "рублей")
