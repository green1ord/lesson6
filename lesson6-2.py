"""
Task 2
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла 
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать 
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""
with open('nginx_logs.txt') as f:
    data = []
    spam_dict = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_dict.setdefault(splitted[0], 0)
        spam_dict[splitted[0]] += 1