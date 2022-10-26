values = []
        for card in list:
            values.append(card['value'])
        print("┌─────┐  " * n_cards)
        print(f"|{dict['value']:<2}   |  " * n_cards)
        print(f"|  {dict['suit']}  |  " * n_cards)
        print(f"|   {dict['value']:>2}|  " * n_cards)
        print("└─────┘  " * n_cards)