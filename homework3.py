# 1 power of a number
def pwr(x,y):
    # pwr is going to return product of x to the power of y
    prod = pow(x,y)
    return (prod)

print(pwr(2,3))

# 2 min and max
def min_max_values(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum,maximum
numbers = [1,2,3,4,5,10,7]
result = min_max_values(numbers)
print("minimum value:", result[0])
print("maximum value:", result[1])

# 3 check leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("enter a year: "))
print(is_leap_year(year))


#4 calculate BMI
def bmi(x,y):
    # bmi is going to return division of x and y
    prod = x/y**2
    return (prod)
print(bmi(59,2))


#5 rotating digits ASK AB THIS
def rotate_digit(n):
   last_digits = n % 10
   rotated_number = last_digits * (10 ** (len(str(n))-1)) + n//10
   return rotated_number
number = 12345
rotated_number = rotate_digit(number)
print("Rotated number", rotated_number)


#minimum and maximumm loop
def find_min_for(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def find_max_for(numbers):
    max_value = numbers [0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def find_min_while(numbers):
    min_value = numbers[0]
    i =1
    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1
    return min_value

def find_max_while(numbers):
    i = 1
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i += 1
    return max_value


#vowels
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    
    return count

input_string = "i love to code yup"
print("Number of vowels:", count_vowels(input_string))


#digital root
def digital_root(n):
    while n >= 10:
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10 
            n //= 10  
        n = digit_sum  
    return n

number = 16
print("Digital root of", number, "is:", digital_root(number))
