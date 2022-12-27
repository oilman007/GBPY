# 3)Вводится слово. Переменной msg присвоить строку "палиндром", 
# если введенное слово является палиндромом (одинаково читается и вперед и назад), 
# а иначе присвоить строку "не палиндром". Проверку проводить без учета регистра. 
# Программу реализовать с помощью тернарного условного оператора. Значение переменной msg отобразить на экране.

# Sample Input:
# Казак
# Sample Output:
# палиндром


data = input("enter text: ").upper()

def is_palindrome(data):
    size = len(data)
    for i in range(size//2):
        if data[i] != data[size - i - 1]:
            return "not palindrome"
    return "palindrome"

print(is_palindrome(data))