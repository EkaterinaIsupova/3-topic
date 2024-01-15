def count_letters(text):
    text1 = text.lower()
    dictionary = {}
    for letter in text1:
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary


def calculate_frequency(dictionary):
    sum_ = sum(dictionary.values())
    dictionary1 = {}
    for letter, count in dictionary.items():
        dictionary1[letter] = count/sum_
    return dictionary1


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dict1 = count_letters(main_str)
frequency = calculate_frequency(dict1)
# TODO Распечатайте в столбик букву и её частоту в тексте
for key, value in frequency.items():
    print(f"{key}: {value:.2f}")
