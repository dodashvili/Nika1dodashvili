# 1 შექმენით სია სადაც გადასცემთ 10 ინტეჯერს, შემდეგ გადაუარეთ ამ სიას და თტოეულ მათგანს გაამრავლეთ/გაყეთ/დაუმატეთ/გამოაკელით ერთმანეთს. (ექსპერიმენტებიც გააკეტეთ.)

num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] * 2)


num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] / 2)


num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] + 2)


num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] - 2)



# 2შექმენით სია,სადაც გამოიტანთ სათითაოდ მნიშვნელობებს და ასევე  ჩაანაცვლებთ სხვა მნიშვნელობით.

food_list = ["banani", "apple", "kefiri"]
print(food_list[0])
print(food_list[1])
print(food_list[2])
food_list[1] = "coffe"
print(food_list)



# 3 დავალება შექმენით სია და მომხმარებელს აარჩევინეთ სასურველი მნიშვნელობა.

movie_list  = ["american psicho", "fight club", "fast forious"]
choise = int(input("wich one is your favourite movie? "))
print(movie_list[choise])