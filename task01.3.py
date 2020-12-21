n = int(input("Введите число n: "))  # Вычислить сумму в формате sum=n+nn+nnn
number = str(n)  # Числовой тип переводим к строковому и сохраняем в переменной
nn = number + number
nnn = number + number + number
sum = n + int(nn) + int(nnn)  # Перевод назат в числовой и сумма.
print(sum)
