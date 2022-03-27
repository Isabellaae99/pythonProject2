""")Write a function count_integer(numbers, integer) that accepts an integer list and an
integer as arguments. It counts the occurrence of the integer in the list. It returns the count as
an integer. If no occurrence is found, the function returns the integer 42. Do not use-built-in
functions! The use of enumerate() or range() is allowed. Use loops to solve the problem.
"""


def count_integer(numbers: list, integer: int):
    count = 0
    for i in numbers:
        if i == integer:
            count += 1
            return int(count)
        else:
            return 42


print(count_integer([1, 1, 1, 3], 1))

"""(2)Write a function list_func(numbers, integer) that accepts an integer list and an integer as 
arguments. Use the built-in list functions to achieve the following:
- Replace the given Integer by the number 6 in the list, reverse the list, print it on 
the console and return the un-reversed list
- If the given integer is not in the list, return an empty list
Don’t forget that lists are mutable. You have to do a copy if you want the original list left 
untouched."""


def list_func(numbers: list, integer: int):
    if integer in numbers:
        copynumbers = numbers.copy()
        x = copynumbers.index(integer)
        list1 = copynumbers.pop(x)
        list2 = copynumbers.insert(x,6)
        new_list = copynumbers.reverse()
        print(new_list)
        return numbers
    else:
        empty_list = []
        return empty_list



print(list_func([1, 2, 3, 4], 2))

"""3) Write a function compare_lists(list1, list2) that accepts two list as arguments. The 
function compares if the list have one or multiple common elements and returns a new list with 
the elements that are in both list. It returns an empty list if no common element is found."""


def compare_lists(list1: list, list2: list):
    for i in list1:
        if i in list1 == True and i in list2 == True:
            new_list = [i for i in list1 if i in list2]
            return new_list
    else:
        empty_list = []
        return empty_list


print(compare_lists([1, 2, 3, 4], [1, 2, 5, 6]))

"""4. (1)Write a function remove_duplicates(lst) that accepts a list as argument and removes all 
duplicates from the list. There is a very easy way to do this. The function returns a list without 
duplicates or just the given list if no duplicates were present."""


def remove_duplicates(lst:list):
    res =[]
    for i in lst:
        if i not in res:
            res.append(i)
    return res

lst = [1,2,2,3]

print(remove_duplicates(lst))

"""Write a function dict_func(dictionary) that accepts a dictionary as argument. The given 
dictionary contains the keys “Type”, “Brand” and “Price”. The function prints out the values of 
the dictionary in following format on the console:
“You have a TYPE from BRAND that costs PRICE.”
Where the capitalized words represent the values assigned to the keys. The function adds the 
key “OS” to the dictionary and defaults its value to “Linux”. Afterwards it prints the dictionary to 
the console"""


def dict_func(dictionary: dict):
    dictionary = {"Type": str(input("What Type: "), "Brand": str(input("What Brand:")), "Price": str(input("Enter Prize: ")), "OS": str("Linux")}
        if len(dictionary ["Type"]) == 0:
            print("You have an unknown type from ", dictionary ["Brand"], "that costs ", dictionary [prize], ".",
                  "Your operating system is", dictionary["OS"], ".")
        elif len(dictionary["Brand"]) == 0:
            print("You have a ", dictionary["Type"], "from an unknown brand that costs ", dictionary["Prize"], ".",
                  "Your operating system is", dictionary["OS"], ".")
        elif len(dictonary["Prize"]) == 0:
            print("You have a", dictionary[Type], "from", dictionary [Brand], "that costs an unknown amount of money.",
                  "Your operating system is", dictionary["OS"], ".")
        else:
            print("You have a", dictionary["Type"], "from", dictionary ["Brand"], "that costs ", dictionary [prize], ".",
                  "Your operating system is", dictionary["OS"], ".") )
    return dictionary

