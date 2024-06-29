import sys

input_lines = sys.stdin.read().split()

current_line = 0
while current_line < len(input_lines):
    num_sections = int(input_lines[current_line])
    current_line += 1
    sections_strength = {}
    
    for section_number in range(1, num_sections + 1):
        sections_strength[section_number] = int(input_lines[current_line])
        current_line += 1
    
    while current_line < len(input_lines):
        student_order = [0] * (num_sections + 1)
        lis = [0] * (num_sections + 1)
        first_student = int(input_lines[current_line])
        
        if 1 <= first_student <= num_sections:
            student_order[first_student] = 1
            current_line += 1
        else:
            break
        
        for section_order in range(2, num_sections + 1):
            student = int(input_lines[current_line])
            if 1 <= student <= num_sections:
                student_order[student] = section_order
                current_line += 1
            else:
                break
        
        for i in range(1, num_sections + 1):
            student_order[i] = sections_strength.get(student_order[i], 0)
        
        lis[1] = 1
        max_length = 1
        for i in range(2, num_sections + 1):
            lis[i] = 1
            for j in range(1, i):
                if student_order[i] > student_order[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
            max_length = max(max_length, lis[i])
        
        print(max_length)