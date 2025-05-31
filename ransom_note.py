def can_construct(ransomNote: str, magazine: str) -> bool:
    # Create a hash table (dictionary) to store letter counts from magazine
    letter_counts = {}

    # Populate the dictionary with frequencies from magazine
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # Check if the ransom note can be formed
    for char in ransomNote:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1  # Use the letter

    return True  # Successfully constructed the ransom note