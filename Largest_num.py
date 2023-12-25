input_numbers = ["1234", "2356", "5479", "25412"]
min_digit=0
output_numbers = []
for i in input_numbers:
   min_digit=i[0]
   for j in range(1,len(i)):
       if min_digit > i[j]:
           min_digit=i[j]
   output_numbers.append(i.replace(min_digit,""))
for i in output_numbers:
   print(i)