arguments = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
opt = True

#------------------------------ Using optional argument ------------------------------
def arithmetic_arranger(problems: list, has_answer= False):
    valid_operations = '+-'

    # --- Errors ---
    # Too many problems
    problems_n = len(problems)
    if problems_n > 5: 
        return "Error: Too many problems."

    for problem in problems:
        op = problem.split()

        # Wrong format
        if len(op) != 3:
            return "Error: Wrong problem format."
            
        # Wrong Operation
        if op[1] not in valid_operations:
            return "Error: Operator must be '+' or '-'."
        
        # Only Digits
        try:
            int(op[0])
            int(op[2])
        except:
            return "Error: Numbers must only contain digits."
        
        # Max of 4 Digits
        if len(op[0]) > 4 or len(op[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        

    # Solution
    line = ["", "", "", ""]
    spaces = 4 * " "

    i = 1
    for problem in problems:
        op = problem.split()
        len1 = len(op[0])
        len2 = len(op[2])
        max_len = max(len1, len2)

        dif1 = max_len - len1
        dif2 = max_len - len2

        if op[1] == '+': answer = str(int(op[0]) + int(op[2]))
        if op[1] == '-': answer = str(int(op[0]) - int(op[2]))

        str1 = 2 * " " + dif1 * " " + op[0]
        str2 = op[1] + " " + dif2 * " " + op[2]
        str3 = len(str1) * "-"

        dif4 = len(str1) - len(answer)
        str4 = dif4 * " " + answer

        line[0] += str1
        line[1] += str2
        line[2] += str3
        line[3] += str4

        if i < problems_n:
            line[0] += spaces
            line[1] += spaces
            line[2] += spaces
            line[3] += spaces
        i += 1

    if has_answer:
        arranged_problems = line[0] + '\n' + line[1] + '\n' + line[2] + '\n' + line[3]
    else:
        arranged_problems = line[0] + '\n' + line[1] + '\n' + line[2]

    return arranged_problems

print(arithmetic_arranger(arguments, opt))


# #------------------------------ Using *args ------------------------------
# def arithmetic_arranger(*problems):
#     print(problems)
#     valid_operations = '+-'
#     print_type = False

#     try:
#         print_type = problems[1]
#     except:
#         pass
    
#     print(print_type)
#     # --- Errors ---
#     # Too many problems
#     problems_n = len(problems[0])
#     if problems_n > 5: 
#         return "Error: Too many problems."

#     for problem in problems[0]:
#         op = problem.split()

#         # Wrong format
#         if len(op) != 3:
#             return "Error: Wrong problem format."
            
#         # Wrong Operation
#         if op[1] not in valid_operations:
#             return "Error: Operator must be '+' or '-'."
        
#         # Only Digits
#         try:
#             int(op[0])
#             int(op[2])
#         except:
#             return "Error: Numbers must only contain digits."
        
#         # Max of 4 Digits
#         if len(op[0]) > 4 or len(op[2]) > 4:
#             return "Error: Numbers cannot be more than four digits."
        

#     # Solution
#     line = ["", "", "", ""]
#     spaces = 4 * " "

#     i = 1
#     for problem in problems[0]:
#         op = problem.split()
#         len1 = len(op[0])
#         len2 = len(op[2])
#         max_len = max(len1, len2)

#         dif1 = max_len - len1
#         dif2 = max_len - len2

#         if op[1] == '+': answer = str(int(op[0]) + int(op[2]))
#         if op[1] == '-': answer = str(int(op[0]) - int(op[2]))

#         str1 = 2 * " " + dif1 * " " + op[0]
#         str2 = op[1] + " " + dif2 * " " + op[2]
#         str3 = len(str1) * "-"

#         dif4 = len(str1) - len(answer)
#         str4 = dif4 * " " + answer

#         line[0] += str1
#         line[1] += str2
#         line[2] += str3
#         line[3] += str4

#         if i < problems_n:
#             line[0] += spaces
#             line[1] += spaces
#             line[2] += spaces
#             line[3] += spaces
#         i += 1

#     if print_type:
#         arranged_problems = line[0] + '\n' + line[1] + '\n' + line[2] + '\n' + line[3]
#     else:
#         arranged_problems = line[0] + '\n' + line[1] + '\n' + line[2]

#     return arranged_problems

# print(arithmetic_arranger(arguments, opt))

# --------------------------------------------------------------------------------------------------------------