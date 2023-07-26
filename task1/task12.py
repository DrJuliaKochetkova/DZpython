
s = int(input("Задай сумму двух чисел \n"))

p = int(input("Задай произведение чисел \n"))

for x in range(s):

   for y in range(p):

      if s == x + y and p == x * y:
         print(f'первое число ="{x}", второе число ="{y}"')

