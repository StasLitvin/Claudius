def rezult_test_lic(answers):
    int = 0
    ext = 0
    mas_rez = ["Да", "Нет", "Нет", "Нет", "Да", "Да", "Да", "Да"]
    for i in range(8):
        if answers[i]==mas_rez[i]:
            int+=1
        else:
            ext+=1
    if int>4:
        return "Интроверт"
    elif ext>4:
        return "Экстраверт"
    else:
        return "Амбиверт"