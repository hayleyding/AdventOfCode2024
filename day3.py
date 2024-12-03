#Day3
#Part1
import re

def calculate_sum_from_mul(file_path):
    pattern = r"mul\((\d+),(\d+)\)"
    
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            for num1, num2 in matches:
                total_sum += int(num1) * int(num2)
    
    return total_sum

file_path = 'day3.txt'

result = calculate_sum_from_mul(file_path)
print(f"The total sum is: {result}")

#Part2
import re

def calculate_sum_with_control_char_by_char(file_path):
    total_sum = 0
    include = True  

    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = "do()"
    dont_pattern = "don't()"

    with open(file_path, 'r') as file:
        for line in file:
            i = 0
            while i < len(line):
                if line[i:i+len(do_pattern)] == do_pattern:
                    include = True
                    i += len(do_pattern)
                elif line[i:i+len(dont_pattern)] == dont_pattern:
                    include = False
                    i += len(dont_pattern)
                elif line[i:i+4] == "mul(":
                    match = mul_pattern.match(line[i:])
                    if match:
                        num1, num2 = map(int, match.groups())
                        if include:
                            total_sum += num1 * num2
                        i += match.end() 
                    else:
                        i += 1  
                    i += 1  
    return total_sum


file_path = 'day3.txt'
result = calculate_sum_with_control_char_by_char(file_path)
print(f"The total sum is: {result}")
