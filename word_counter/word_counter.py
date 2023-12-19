def total_word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        total_word_count = len(words)

    return total_word_count

file_path = 'text_file.txt'
total_count = total_word_count(file_path)
print(f'Total number of words in the file: {total_count}')
