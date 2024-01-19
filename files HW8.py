# 1. Даний текстовий файл. 
# Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, 
# що складаються не менше ніж з семи літер.

print("====Ex. 1====")

FILENAME = "test.txt"
OUTPUTFILE = "output.txt"

def filter_words(FILENAME, OUTPUTFILE):
    with open(FILENAME, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()
    filtered_words = [word for word in words if len(word) >= 7]
    result_text = ' '.join(filtered_words)

    with open(OUTPUTFILE, 'w', encoding='utf-8') as output_file:
        output_file.write(result_text)

    total_word_count = len(words)
    filtered_word_count = len(filtered_words)

    return total_word_count, filtered_word_count


total_words, filtered_words = filter_words(FILENAME, OUTPUTFILE)
print(f"Кількість слів із семи або більше літер: {filtered_words}")

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
print("====Ex. 2====")
print(f"Загальна кількість слів: {total_words}")

# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.
print("====Ex. 3====")

TEXT = "test2.txt"

def check_and_censor(text, forbidden_words):
    words = text.split()
    replaced_words_count = 0

    for i in range(len(words)):
        word = words[i].strip(".,!?;:")
        if word.lower() in forbidden_words:
            words[i] = '*' * len(word)
            replaced_words_count += 1

    censored_text = ' '.join(words)
    return censored_text, replaced_words_count

if __name__ == "__main__":
    forbidden_words = {"die"}  
    
    input_filename = TEXT
    with open(input_filename, 'r', encoding='utf-8') as file:
        input_text = file.read()

    censored_text, replaced_count = check_and_censor(input_text, forbidden_words)

    
    print("\nЗамінений текст:")
    print(censored_text)

    print("\nСтатистика:")
    print(f"Кількість замінених слів: {replaced_count}")