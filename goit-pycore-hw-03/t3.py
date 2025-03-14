import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num: str)-> str:
    formatted_num = re.sub(r'[^\d+]', '', num.strip())
    if(formatted_num.startswith('380') and len(formatted_num) == 12):
        return '+' + formatted_num
    if(not formatted_num.startswith('+38') and len(formatted_num) == 10 ):
        return '+38' + formatted_num 
    if(formatted_num.startswith('+380') and len(formatted_num) == 13 ):
        return formatted_num
    print(f'Incorrect phone number: {num}')
    return 
sanitized_numbers = list(filter(None,[normalize_phone(num) for num in raw_numbers]))
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)