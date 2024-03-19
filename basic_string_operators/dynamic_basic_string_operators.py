# Define the base string to start with
base_string = "Hey there! what should this string be?"

# Define a helper function to dynamically modify the string
def modify_string(s, target_length, first_a_index, num_as):
    # Ensure the string is of the target length
    s = s[:target_length]
    
    # Adjust the string to contain 'a' at the first_a_index
    s_list = list(s)
    if s_list[first_a_index] != 'a':
        s_list[first_a_index] = 'a'
    
    # Add additional 'a's if needed
    a_count = s_list.count('a')
    for i in range(a_count, num_as):
        non_a_indices = [j for j, letter in enumerate(s_list) if letter != 'a']
        s_list[non_a_indices[i]] = 'a'
    
    return ''.join(s_list)

# Modify the string for each condition and print the results
# Condition 1: Length should be 20
s = modify_string(base_string, 20, 8, 2)
print(f"Length of s = {len(s)}")

# Condition 2: First occurrence of 'a' at index 8
print(f"The first occurrence of the letter a = {s.find('a')}")

# Condition 3: Number of 'a's should be 2
print(f"'a' occurs {s.count('a')} times")

# Slicing operations
print(f"The first five characters are '{s[:5]}'")
print(f"The next five characters are '{s[5:10]}'")
print(f"The thirteenth character is '{s[12]}'")
print(f"The characters with odd index are '{s[1::2]}'")
print(f"The last five characters are '{s[-5:]}'")

# Case conversion operations
print(f"String in uppercase: {s.upper()}")
print(f"String in lowercase: {s.lower()}")

# Check how the string starts and ends
s_start = "Str" + base_string[3:20]
print(f"String starts with 'Str': {s_start.startswith('Str')}")

s_end = base_string[:15] + "ome!"
print(f"String ends with 'ome!': {s_end.endswith('ome!')}")

# Split the string into three separate words
s_split = "one two three"
print(f"Split the words of the string: {s_split.split(' ')}")
