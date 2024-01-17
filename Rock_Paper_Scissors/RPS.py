def player(prev_play, opponent_history=[], play_order={}):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

   # we assume the first opponent`s move is rock, hence 'P'. Then we save it in the opponent's history.
    if not prev_play:
        prev_play = 'P'

    opponent_history.append(prev_play)

    # While we want to keep track of the last five moves of our opponents, we should keep playing until we have enough data. So, until then, assume that the opponent would throw paper, hence 'P'
    prediction = 'P'

    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1

    potential_plays = [
        "".join([*opponent_history[-4:], v]) for v in ['R', 'P', 'S']
    ]

    sub_order = {
        k: play_order[k] for k in potential_plays if k in play_order
    }

    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1:]

    return ideal_response[prediction]
