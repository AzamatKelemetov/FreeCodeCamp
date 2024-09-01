def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line, second_line, dashes, results = [], [], [], []

    for problem in problems:
        parts = problem.split()
        first_operand, operator, second_operand = parts
        '''Input Validation'''
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(first_operand) > 4 and len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        '''Format the output'''
        width = max(len(first_operand), len(second_operand)) + 2
        first_line.append(first_operand.rjust(width))
        second_line.append(operator + second_operand.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))
            else:
                result = str(int(first_operand) - int(second_operand))
            results.append(result.rjust(width))

    problems = '\n'.join(['    '.join(first_line), '    '.join(second_line), '    '.join(dashes),])

    if show_answers:
        problems += '\n' + '    '.join(results)

    return problems


print(repr(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}'))


