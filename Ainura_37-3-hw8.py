min= 1
max=100
attempts=0
guesses= []
while True:
    guess= (min+max) //2
    print (f'Вы загадали {guess}? (>,<,=)')
    attempts +=1
    guesses.append(guess)
    answer = input ("Answer: ")
    if answer ==">":
        min=guess+1
    elif answer =="<":
        max=guess-1
    elif answer == '=':
        print("Я угадал!")
        with open ("results.txt", "w",encoding= "utf-8") as file:
            file.write(f'Количество попыток {attempts}\ ,f'Список попыток:
            {guesses}\n',  f'Загаданное
            число : {guess}')
            break
    else:
        print("Некоректный ответ. Ответом должен быть только знаки > < или =")



