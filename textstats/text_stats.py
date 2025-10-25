import re
from collections import Counter

def text_content(filename:str):
    with open(filename, "r", encoding="utf-8") as file_in:
        text_content = file_in.read()
    return text_content

def character_count(text_content:str):
    characters_with_spaces = len(text_content)
    characters_no_spaces = 0
    char_index = 0
    while char_index < len(text_content):
        current_char = text_content[char_index]
        if not current_char.isspace():
            characters_no_spaces += 1
        char_index += 1
    return characters_with_spaces,characters_no_spaces

def word_extraction(text_content:str):
    lowered_text = text_content.lower()
    word_list = re.findall(r"[a-zA-Z]+", lowered_text)
    return word_list

def wrd_unq_wrd_cnt(word_list:list):
    word_count = len(word_list)
    unique_word_count = len(set(word_list))
    return word_count,unique_word_count

def avg_wrd_lenght(word_list:list,word_count):
    total_letter_count = 0
    word_index = 0
    while word_index < len(word_list):
        total_letter_count += len(word_list[word_index])
        word_index += 1
    average_word_length = (total_letter_count / word_count) if word_count != 0 else 0.0
    average_word_length_str = f"{average_word_length:.1f}"
    return average_word_length_str
def chr_spaces (text_content:str):
    characters_with_spaces = len(text_content)
    characters_no_spaces = 0
    char_index = 0
    while char_index < len(text_content):
        current_char = text_content[char_index]
        if not current_char.isspace():
            characters_no_spaces += 1
        char_index += 1
def freq_cmn_wrds(word_list:list,word_count):
    if word_count == 0:
        most_common_line = "Most common word(s): (0)"
    else:
        word_counts = Counter(word_list)
        highest_frequency = 0
        for word in word_counts:
            if word_counts[word] > highest_frequency:
                highest_frequency = word_counts[word]
        most_frequent_words = []
        for word in word_counts:
            if word_counts[word] == highest_frequency:
                most_frequent_words.append(word)
        most_frequent_words.sort()
        if len(most_frequent_words) == 1:
            most_common_line = f"Most common word(s): {most_frequent_words[0]} ({highest_frequency})"
        else:
            most_common_line = f"Most common word(s): {', '.join(most_frequent_words)} ({highest_frequency})"
    return most_common_line

def write_file(word_count,unique_word_count,characters_with_spaces,characters_no_spaces,average_word_length_str,most_common_line):
    output_lines = [
    f"Word count: {word_count}",
    f"Unique words: {unique_word_count}",
    f"Characters (with spaces): {characters_with_spaces}",
    f"Characters (no spaces): {characters_no_spaces}",
    f"Average word length: {average_word_length_str}",
    most_common_line,
]
    # --- Print to console ---
    line_index = 0
    while line_index < len(output_lines):
        print(output_lines[line_index])
        line_index += 1

    # --- Write to output.txt ---
    with open("output.txt", "w", encoding="utf-8") as file_out:
        line_index = 0
        while line_index < len(output_lines):
            file_out.write(output_lines[line_index] + ("\n" if line_index < len(output_lines) - 1 else ""))
            line_index += 1
