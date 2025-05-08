def reverseString(str: str) -> str:
    # Write your code from here.
    splitted = str.split()
    # print(" ".join(splitted[::-1]))
    str = ""
    for i in range(len(splitted) - 1, -1, -1):
        str += splitted[i] + " "

    return str


(reverseString("Welcome to Coding Ninjas"))


# Sample Input 1 :
# Welcome to Coding Ninjas

# Sample Output 1:
# Ninjas Coding to Welcome


# function reverseString(str) {
#     const splitted = str.split(" ");
#     let result = "";

#     for (let i = splitted.length - 1; i >= 0; i--) {
#         result += splitted[i] + " ";
#     }

#     return result.trim();
# }
