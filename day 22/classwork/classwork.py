
#დავალება 1 შექმენით ფუნქცია სახელად manual_pop, რომელსაც გადაეცემა სია და ინდექსი. როდესაც გადაეცემა ინდექსი, სიიდან უნდა ამოიშალოს ამ ინდექსზე მყოფი ელემენტი და დაბრუნდეს სია ამ სახით. ამ დავალებისთვის გამოიყენეთ for ციკლი

def manual_pop(collection, delete_index):
     new_collection =[]

     for index in range(0, len(collection)):
         if index != delete_index:
            new_collection.append(collection[index])

     return new_collection
names = ["nika", "lasha", "ioane"]
print(manual_pop(names, 0))

# დავალება 2 შექმენით ფუნქცია სახელად manual_count: ფუნქციას გადაეცემა სია და ელემენტი. თქვენ უნდა დაითვალოთ სიაში ამ ელემენტის რაოდენობა. წინა დავალების მსგავსაც, აქაც for ციკლი გამოიყენეთ


def manual_count(collection, item_to_count):
    conut = 0

for item in "collection":
        if item == "item_to_count":
           conut = conut + 1

 conut

names = [True, True, False, True]
print(manual_count(names, True))

#Bonus: შექმენით ფუნქცია სახელად manual index, რომელსაც გადაეცემა სია და ერთი მნიშვნელობა. როდესაც გაიგებთ ამ ელემენტის ინდექსს, დააბრუნეთ ის. გამოიყენეთ for ციკლი, არ გამოიყენოთ .index

def manual_index(collection, value):
    for index in range(0, len(collection)):
        if collection[index] == value:
              return index
        
-1
names = ["nika", "lasha", "ioane"]
print(manual_index(names, "ioane"))





def greet(username = "Guest"):
    print("hello " + username)


