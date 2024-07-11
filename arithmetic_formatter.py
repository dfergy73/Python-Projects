'''This program contains a function that receives a list of strings
   which are arithmetic problems, and returns the problems arranged
   vertically and side-by-side. The function takes an optional second
   argument, which, when set to True, displays the answers.'''

def arithmetic_arranger(problems, show_answers=False):
    # Create lists to hold the formatted rows of the problems.
    top = []
    bottom = []
    dashes = []
    answers = []

    # Check to make sure there aren't more than 5 problems.
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Loop through each arithmetic problem.
    for prob in problems:
        # Make sure only addition or subtraction are being used.
        operands = ('+', '-')
        if not any(x in prob for x in operands):
            return "Error: Operator must be '+' or '-'."

        # Split the problems into the operator and two operands.
        pieces = prob.split()

        # Make sure only digits are being used.
        try:
            num1 = int(pieces[0])
            num2 = int(pieces[2])
        except:
            return 'Error: Numbers must only contain digits.'
        
        # Make sure the numbers aren't longer than 4 digits.
        if len(pieces[0]) > 4 or len(pieces[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Formatting for when the first number is longer than the second.
        if len(pieces[0]) > len(pieces[2]):
            length = ' ' * (len(pieces[0]) - len(pieces[2]))
            top_piece = f'  {pieces[0]}'
            botm_piece = f'{pieces[1]} {length}{pieces[2]}'
            dash = '-' * len(top_piece)
            top.append(top_piece)
            bottom.append(botm_piece)
            dashes.append(dash)
            
        # Formatting for when the numbers are of equal length.
        elif len(pieces[0]) == len(pieces[2]):
            top_piece = f'  {pieces[0]}'
            botm_piece = f'{pieces[1]} {pieces[2]}'
            dash = '-' * len(top_piece)
            top.append(top_piece)
            bottom.append(botm_piece)
            dashes.append(dash)
        
        # Formatting for when the second number is longer than the first.
        else:
            length = ' ' * (len(pieces[2]) - len(pieces[0]))
            top_piece = f'  {length}{pieces[0]}'
            botm_piece = f'{pieces[1]} {pieces[2]}'
            dash = '-' * len(botm_piece)
            top.append(top_piece)
            bottom.append(botm_piece)
            dashes.append(dash)

        # Compute and format the answer if it's an addition problem.
        if pieces[1] == '+':
            answer = num1 + num2
            spaces = ' ' * (len(dash) - len(str(answer)))
            string = f'{spaces}{answer}'
            answers.append(string)

        # Compute and format the answer if it's a subtraction problem.
        elif pieces[1] == '-':
            answer = num1 - num2
            spaces = ' ' * (len(dash) - len(str(answer)))
            string = f'{spaces}{answer}'
            answers.append(string)

    # Join the formatted strings together to make the rows.
    fin_top = "    ".join(top)
    fin_bottom = "    ".join(bottom)
    fin_dashes = "    ".join(dashes)
    fin_answers = '    '.join(answers)

    # Check to see if answers should be displayed.
    # Join the rows together into one formatted string and return the string.
    if show_answers:
        arranged_problems = f'{fin_top}\n{fin_bottom}\n{fin_dashes}\n{fin_answers}'
        return arranged_problems
    else:
        arranged_problems = f'{fin_top}\n{fin_bottom}\n{fin_dashes}'
        return arranged_problems
    
print('Without answers:') 
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('\nWith answers:')
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))