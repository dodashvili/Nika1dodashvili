#8kyu

def change_light(current_state):
    if current_state == "green":
        return "yellow"
    elif current_state == "yellow":
        return "red"
    elif current_state == "red":
        return "green"
    else:
        return "invalid state"

# Example usage:
current_state = "green"
next_state = change_light(current_state)
print("Next state:", next_state)







def combine_strings(str1, str2, str3):
    combined = ""
    for i in range(len(str1)):
        combined += str1[i] + str2[i] + str3[i]
    return combined

# Example usage:
input1 = "aa"
input2 = "bb"
input3 = "cc"
output = combine_strings(input1, input2, input3)
print(output)  # Output: "abcabc"






#7KYU

