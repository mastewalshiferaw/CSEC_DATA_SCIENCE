"""Counts the number of vowels in a given string."""
def count_vowels(text: str) -> int:
    
    vowels = set("aeiouAEIOU")
    #vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    return count

#Example
print(count_vowels("Hello world"))