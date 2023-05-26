def monobit_test(sequence):
    n = len(sequence)
    ones_count = sequence.count('1')
    zeros_count = sequence.count('0')
    ones_proportion = ones_count / n
    zeros_proportion = zeros_count / n

    # Перевірка балансу
    if ones_proportion != zeros_proportion:
        return False
    else:
        return True

# Приклад використання
sequence = '1110001'
result = monobit_test(sequence)
print(result)