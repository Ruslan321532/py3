while True:
    word = input(
        "Введите слово на латинице(что-бы завершить работу напишите команду: 'exit'): ")
    if word == "exit":
        break

    vowels = 0
    consonants = 0
    total_letters = 0

    for letter in word:
        if letter.isalpha():
            total_letters += 1
            if letter.lower() in "aeiouyаеёиоуыэюя":
                vowels += 1
            else:
                consonants += 1

    print(f"Общее количество букв: {total_letters}")
    print(f"Количество гласных букв: {vowels}")
    print(f"Количество согласных букв: {consonants}")

    if vowels == 0 or consonants == 0:
        print("Невозможно вычислить процентное соотношение гласных и согласных букв")
    else:
        vowels_percent = round(vowels / total_letters * 100, 2)
        consonants_percent = round(consonants / total_letters * 100, 2)
        print(f"процентное соотношение, гласных букв: {vowels_percent}%")
        print(f"процентное соотношение, согласных букв: {consonants_percent}%")
