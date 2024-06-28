"""დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი."""


num = int(input("enter first number: "))

if num < -0:
     print("This number is negative")
if num == 0:
     print("This number is equal to zero")
if num > 0:
     print("This number is integer")


"""
დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი.
 მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა,
 რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა.
 თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision"."""

choice = input("if you want miles to kilometers type 1. if you want kilometers for mile type 2: ")

if choice == "1":
     amount1 = int(input("Enter number: "))
print(amount1, "miles to kilometers would be", amount1 * 1.6)
choice == "2"
amount2 = int(input("Enter number: "))
print(amount2, "kilometers to miles would be", amount2 * 0.62 )

print("Wrong decision") 


"""შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი,
 საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია."""




name = input("Enter youre name: ")
lastname = input("entrer youre lastname: ")
age = int(input("enter youre age: "))
email = input("entr youre email: ")

print("youre name is:",name, "  youre lastname is:",lastname, "  youre age is:",age, "  youre email is:", email)



"""მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული.

მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი.
 შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში."""\
 

sum = 0
for num in range(3):
  num = int(input("Enter first number: "))
sum = sum + num

sum = sum / 3
print(sum)


num = int(input("Write any number from one to nine: ")) #5



"""
მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის,
ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. ციკლში იტერაცია მოახდინეთ ერთით
 და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი)."""


num1 = int(input("Enter the first number >: "))
num2 = int(input("Enter the second number >: "))

if num1 < num2:
     for i in range(num1, num2, +1):
        print(i)
else:
     for i in range(num2, num1, +1):
         print(i)
print(i * i * i)




"""მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მისი ციფრთა ჯამი."""

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print(num1 + num2)


"""დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს
 და დაბეჭდავს მის გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10."""

   

# ვადეკლარირებთ int ტიის ცვლადას სადაც მომხმარებელს შეეძლება შემოიტანოს ინფორმაცია 
num = int(input("Enter the number of which the you want to print the multiplication table: "))

 # მომხმარებელს ვაცნობებთ თუ რა არის მისი რიცხვის გამრავლების ტაბულა
print("This is a number multiplication table:", num)

# i დიაპაზონში 1,10 
for i in range(1,11):
# დავბეჭდოთ მომხმარებლის მიერ შემოტანლი რიცხვი შემდეგ დიაპაზონი და ბოლოს რიცხვი გამრავლებული დიაპაზონზე
   print(num, "x", i, "=", num * i )



"""შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება). 
მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას."""




print ("Please select the operation.")    
print ("1 - Add")    
print ("2 - Subtract")
print ("3 - Divide")     
print ("4 - Multiply")    
operacion = input("please enter choice: ")


num1 = int(input("enter firs number for calculator: "))
num2 = int(input("enter second number for calcularote: "))


if operacion == "1" :
     print(num1,"+", num2, "=", num1 + num2)

if operacion == "2" :
     print(num1,"-",num2,"=",num1 - num2)

if operacion == "3" :
    print(num1,"/",num2,"=",num1 / num2)

if operacion == "4": 
     print(num1,"x",num2,"=",num1 * num2)


"""დაწერეთ პროგრამა, რომელიც იღებს სთრინგს,
 შემდეგ მომხმარებელს ეკითხება თუ რამდენჯერ განმეორდეს და for ციკლის გამოყენებით დაბეჭდეთ ის."""

num = input("enter first number: ")
interacion = int(input("how mant times you wont interacion: "))
for i in range(interacion):
    print(num)

"""დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის ინდექსს (BMI),
მომხმარებლისგან მიღებული წონის (კილოგრამებში) და სიმაღლის (მეტრებში) გათვალისწინებით"""


"""calculator BMI  

მაგალითად: სიმაღლე = 152სმ =1.52მ
            სიმაღლე x სიმაღლეზე = 1.52 x 1.52
            წონა = 60კგ
                      60
            bmi = ------------- = 25.96
                  1.52 x 1.52
             """


height = int(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kg: "))
weight = weight * weight
bmi = weight / height

print("youre bmi =",bmi)




"""მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა.

მომხმარებელს შეეკითხეთ სამი რიცხვი და შეამოწმეთ არიან თუ არა პითაგორას რიცხვები."""

leap_year = "29 tebervali"
user_info = input("enter your birtyday info")

if user_info == leap_year:
    print("You are in a lean year")
else:
     print("You are not in a lean year")



Pythagorean_triple = (3, 4, 5, 6, 8, 10, 7, 24, 25, 12, 13, 20, 21, 29, 15, 17, 99, 101, 48, 55, 73, 144, 145)

num = int(input("Write any number and find out if it is a Pythagorean number or not: "))

if num == Pythagorean_triple:
     print("These are Pythagorean numbers")
else:
     print("These are not Pythagorean numbers")



"""
დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით.
    თუ რიცხვი არის 1-ზე ნაკლები ან 5-ზე მეტი, დაბეჭდეთ "Invalid input".
   თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დაბეჭდეთ "Valid input"""

# ვადეკლარირებთ int ტიპის ცვლადს
num = int(input("Enter first numbe for in range (1, 5) : "))

if num < 1:
     print("invalid input")
elif num > 5:
    print("invalid input")
else:
   num == range(1, 5 + 1)
print("valid input")