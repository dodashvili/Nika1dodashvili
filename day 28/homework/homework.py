#CODEWARS

#8KYU
#1
def calculate_average(scores):
    total = sum(scores)  
    num_students = len(scores) 
    average = total / num_students 


print(calculate_average([85, 90, 92, 75, 88])) 

#2
def make_negative(number):
 
    if number >= 0:
        return -number  
    else:
        return number 


print(make_negative(1)) 
print(make_negative(-5))  
print(make_negative(0))  

#3
def str_count(string, char):
    count = 0 
    
   
    for ch in string:
      if ch == char:
            count += 1
    
    return count
     

print(str_count("Hello", "o")) 
print(str_count("Hello", "l")) 
print(str_count("", "z"))       

#7KYU

#1
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False  
        else:
            return True 
    else:
        return False 


years_to_test = [1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000]

for year in years_to_test:
    print(f"{year}: {'Leap year' if is_leap_year(year) else 'Not a leap year'}")






