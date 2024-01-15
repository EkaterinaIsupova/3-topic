# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separation=","):
    first_group_ = first_group.split(separation)
    second_group_ = second_group.split(separation)
    intersection_ = list(set(first_group_).intersection(second_group_))
    intersection_.sort()
    return intersection_


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
