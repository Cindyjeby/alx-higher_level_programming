#!/usr/bin/python3
def best_score(a_dictionary):
    bets_int = 0
    if a_dictionary == {}:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > best_int:
                best_int = value
            else:
                continue
            besy_key = list({k for k in a_dictionary if a_dictionary[k] == best_int})
            return best_key[0]
