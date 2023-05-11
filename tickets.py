num_of_tickets = int(input('Сколько билетов вы хотите купить? '))
total = 0
payment1 = 0
payment2 = 990
payment3 = 1390

for i in range(num_of_tickets):
    print('Билет ' + str(i+1))
    age = int(input('Укажите возраст посетителя: '))
    if age < 18:
        print('Стоимость билета: ' + str(payment1) + ' р.')
        total += payment1
    elif 18 <= age < 25:
        print('Стоимость билета: ' + str(payment2) + ' р.')
        total += payment2
    else:
        print('Стоимость билета: ' + str(payment3) + ' р.')
        total += payment3

if num_of_tickets > 3:
    total = total * 0.9

print('---')
print('Сумма к оплате: ' + str(total) + ' р.')







