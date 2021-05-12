lower = 0
limit = int(input("Please enter a number: "))

print("Prime numbers from 0 to", limit)

for num in range(lower, limit + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
