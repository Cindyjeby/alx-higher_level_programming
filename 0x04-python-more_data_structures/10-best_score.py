#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    if a_dictionary == {}:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > score:
                score = value
            else:
                continue
            best = list({k for k in a_dictionary if a_dictionary[k] == score})
            return best[0]
