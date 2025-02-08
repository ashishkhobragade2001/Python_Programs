def longest_unique_substring(s):
    # Dictionary to store the last seen position of characters
    char_index_map = {}
    
    # Variables to keep track of the current and maximum length
    start = 0  # Start index of the current window
    max_length = 0  # Length of the longest substring
    longest_substring = ""  # The actual longest substring

    for end in range(len(s)):
        current_char = s[end]

        # If the character is already in the window, adjust the start
        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1

        # Update the character's last seen position
        char_index_map[current_char] = end

        # Calculate the current window size
        current_length = end - start + 1
        
        # Update the maximum length and longest substring if needed
        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:end + 1]

    return max_length, longest_substring

# Test the function
input_string = "abcabcbb"
length, substring = longest_unique_substring(input_string)
print(f"The length of the longest substring without repeating characters is {length}.")
print(f"The longest substring without repeating characters is '{substring}'.")
