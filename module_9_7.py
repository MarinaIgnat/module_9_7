#Задание: Декораторы в Python

#Напишите 2 функции:


#Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        sum_ = sum(args)
        n = 0
        for i in range(2, sum_):
            if sum_ % i == 0:
                n += 1
        if n <= 0:
            print('Простое')
        else:
            print("Составное")
        return result
    return wrapper

#Функция, которая складывает 3 числа (sum_three)

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)




