from __future__ import annotations



# def divide(a: float, b : float) -> float | str:
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return ' На ноль делить нельзя'

# print(divide(1, 0))

# while True:
#     try: 
#         a = int(input(' Введите число'))
#         break
#     except ValueError:
#       print('введите число')

# c = lambda a, b : a + b 
# print(c(2,5)) 


# num = int(input(' введите число : '))
# a = ' положительное' if num >= 0 else 'ноль' if num ==0 else  ' Отрицательное'
# print(a)


# num = int(input(' введите число : '))
# a = '  не четное' if  num % 2 else  '  четное'
# print(a)


# words = [ 'погода', 'ночь', ' усталость']
# a = [len(word) for word in words] 
# print(a)

arr = [1, 2, 3, 5, 6, 4, 2]
arr1 =[value **2 for value in arr if value % 2 == 0]
print(arr1)