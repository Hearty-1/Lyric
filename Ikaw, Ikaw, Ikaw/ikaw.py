import time
import sys

lyrics = [
    "Masisisi pa ba natin ang tadhana?",
    "Kung masaya naman ang mga alaala",
    "Kung bibigyan ako ng tatlong kahilingan",
    "Ikaw, ikaw, ikaw",
    "Sa paggising at pagmulat sa umaga",
    "Ikaw lamang ang tinatanging nakikita",
    "Ngunit 'pag hinahanap-hanap ay nawawala",
    "Wala, wala, wala sa'king tabi"
]

delay_per_line = 1.5

delay_per_character = 0.05

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_per_character)
    print()
    time.sleep(delay_per_line)

