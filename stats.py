def get_num_words(text):
    words = text.split()  
    return len(words)


def get_char_counts(text):
    char_counts = {}  
    text = text.lower()  

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def get_sorted_char_counts(char_counts):
   
    sorted_list = [
        {"char": char, "count": count} 
        for char, count in char_counts.items() 
        if char.isalpha()  # Only include alphabetical characters
    ]
    
    sorted_list.sort(key=lambda x: x["count"], reverse=True)  # Sort by count in descending order
    return sorted_list
