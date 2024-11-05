count = 0
while count < 100_000:
    count+= 1


PI = 3.14
GF = 9.8

print("The Constant Value of Pi is {}".format(PI))
print("The Constant Value of Gravitational Force is {}".format(GF))


for num in range(1,21):
 string = " "
 if num % 3 == 0:
  string = string + "Fizz"
 if num % 5 == 0:
  string = string + "Buzz"
 if num % 5 != 0 and num % 3 != 0:
  string = string + str(num)
 print(string)

