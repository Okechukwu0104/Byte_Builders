def is_valid(credit_card_no):
    number = int(credit_card_no)
    card_no = []
    while number != 0:
        extract = number % 10
        card_no.append(extract)
        number //= 10

    sum = 0
    for count, value in enumerate(card_no):
        if count % 2 != 0:
            value *= 2
            if value > 9:
                value = (value // 10) + (value % 10)
        sum += value

    return "valid" if sum % 10 == 0 else "invalid"
