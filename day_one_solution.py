STRING_TO_INT_ENUM: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

def is_written_num(string: str) -> str | int:
    for k in STRING_TO_INT_ENUM.keys():
        if k in string:
            return STRING_TO_INT_ENUM[k]
    return -1
def parse_calibration_values(file_path: str) -> list[int]:
    
    first_digit: str = ""
    last_digit: str = ""
    string_buffer: str = ""
    return_digit: int = -1
    
    line_buffer: str = ""
    results: list = []
    
    with open(file_path, "r") as f:
        while True:
            line_buffer = f.readline()

            if line_buffer == "":
                break
            
            for char in line_buffer:
                
                if not char.isdigit():
                    
                    string_buffer = "".join([string_buffer, char])
                    return_digit = is_written_num(string_buffer)
                    
                    if return_digit == -1:
                        continue
                    
                    if first_digit == "":
                        first_digit = return_digit
                    
                    last_digit = return_digit
                    string_buffer = ""
                    
                    continue
                
                if first_digit == "":
                    first_digit = char
                
                last_digit = char
        
            resulting_digit: int = int("".join([first_digit, last_digit]))
            results.append(resulting_digit)
    
            first_digit = ""
            last_digit = ""
            string_buffer = ""
            return_digit = -1
    
    return results

results = parse_calibration_values("day_one_input.txt")
sum_of_results = sum(results)

print(results, sum_of_results)
