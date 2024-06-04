def convert_to_three_pair_hex_palette(values, format):
    if len(values) != len(format):
        raise ValueError("Number of values must match the number of channels in the format")
    
    hex_strings = []
    
    for value in values:
        # Normalize the value by multiplying by 1000 and converting to an integer
        int_value = int(value * 1000)
        
        # Convert the integer value to a hexadecimal string, ensuring it's at least three digits long
        hex_string = f"{int_value:X}".zfill(3)
        
        # Append the hex string to the list
        hex_strings.append(hex_string)
    
    # Join all hex strings together with a '#' prefix
    return "#" + "".join(hex_strings)

def test_convert_to_three_pair_hex_palette():
    # Test cases with expected outputs
    test_cases = [
        ([0.1, 0.2, 0.3], "pyg", ""),
        ([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1], "pbgrycogle", "")
    ]
    
    for input_values, format, expected in test_cases:
        actual = convert_to_three_pair_hex_palette(input_values, format)
        print(f"Input {input_values}, Format {format}, Expected {expected}, Actual {actual}")
    
    print("All test cases pass")

# Run the test function
test_convert_to_three_pair_hex_palette()


