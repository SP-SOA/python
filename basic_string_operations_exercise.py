# Starting with the base string
s = "Hey there! what should this string be?"

# Length should be 20
# Shortening s to 20 characters including the period
s = "Hey there!1234567890"  
print("Length of s = %d" % len(s))  # Prints: Length of s = 20

# First occurrence of "a" should be at index 8
# Positioning "a" at the 9th position (index 8)
s = "Hey thera!123456"  
print("The first occurrence of the letter a = %d" % s.index("a"))  # Prints: The first occurrence of the letter a = 8

# Number of a's should be 2
# Adding another "a" to the string while keeping the first "a" at index 8
s = "Hey thera!123a456"  
print("a occurs %d times" % s.count("a"))  # Prints: a occurs 2 times

# Slicing the string into bits
# This s will be used for various slicing operations
print("The first five characters are '%s'" % s[:5])  # Prints: The first five characters are 'Hey t'
print("The next five characters are '%s'" % s[5:10])  # Prints: The next five characters are 'hera!'
print("The thirteenth character is '%s'" % s[12])  # Prints: The thirteenth character is '3'
print("The characters with odd index are '%s'" % s[1::2])  # Prints: The characters with odd index are 'e hr!2 a5'
print("The last five characters are '%s'" % s[-5:])  # Prints: The last five characters are '3a456'

# Convert everything to uppercase
# The string s will be converted to uppercase by the upper() method
print("String in uppercase: %s" % s.upper())  # Prints: String in uppercase: HEY THERA!123A456

# Convert everything to lowercase
# The string s will be converted to lowercase by the lower() method
print("String in lowercase: %s" % s.lower())  # Prints: String in lowercase: hey thera!123a456

# Check how a string starts
# Ensuring s starts with 'Str' for the startswith method
s = "Str should start like this"  
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")  # Prints: String starts with 'Str'. Good!

# Check how a string ends
# Ensuring s ends with 'ome!' for the endswith method
s = "End with some!"  
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")  # Prints: String ends with 'ome!'. Good!

# Split the string into three separate strings, each containing only a word
# Adjusting s to split it into exactly three words
s = "Split into three"  
print("Split the words of the string: %s" % s.split(" "))  # Prints: Split the words of the string: ['Split', 'into', 'three']
