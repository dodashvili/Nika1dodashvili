

#d eclaring variable workout targe

deadlift_target = 50
pushups_target = 100


# cimplited pushups and deadlifts

complited_deadlifts = int(input("how many deadlift you made?: "))
complited_pushups = int(input("how many pushups you made?: "))



print(deadlift_target <= complited_deadlifts and pushups_target <= complited_pushups)
print(deadlift_target == complited_deadlifts and pushups_target == complited_pushups)



i = complited_pushups
if i >= 100:
    print("you won chalenge!")