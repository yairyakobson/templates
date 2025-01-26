# max & min functions

# big = max(1,2,3,4)
# print(big)

# small = min(1,2,3,4)
# print(small)
# ----------------------------------
# Function parameters

# def languages(lang):
#     if lang == "jp":
#         print("Konichiwa")
#     elif lang == "en":
#         print("Hello")
#     else:
#         print("שלום")

# languages("jp")
# languages("en")
# languages("he")
# ----------------------------------
# Repeated steps loop

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print("Finished")
# print(n)
# ----------------------------------
# iteration loop

# largest_so_far = -1
# print("Before", largest_so_far) # Output: -1

# for current_num in [9, 41, 12, 3, 74, 15] :
#     if current_num > largest_so_far:
#         largest_so_far = current_num # changes the current_num value
#     print(largest_so_far, current_num)
# ----------------------------------
# counter loop

# count = 0
# sum = 0
# print("Before", count) # Output: 0
# for value in [9, 41, 12, 3, 74, 15] :
#     count = count + 1 # changes the value of count with each iteration
#     sum = sum + value
#     print(count, sum, value)
# print("After", count, sum, sum / count)
# ----------------------------------
# boolean loop

# found = False
# # print("Before", found) # Output: False
# for value in [9, 41, 12, 3, 74, 15] :
#     if value == 3:
#         found = True # Iterates the loop until it matches the condition of the if statement
#     print(found, value)
# print("After", found)

# The None keyword
# The None keyword defines a null value, or no value at all.
# It's the equivalent to the null value in JavaScript

# The is and is not operators
# The is operator is used in logical expressions (checks is the same as)
# It's the same as the == operator, but stronger

# The is not operator is another logical operator which functions like the less than (<) and the less than or equal (<=) comarison operators

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')