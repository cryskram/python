def unique_in_order(sequence: list | str) -> list:
    if len(sequence) == 0:
        return []
    # since we will be getting the topmost element of the list
    # we will have to initialize the dummy list with the first
    # character of the sequence
    dummy = [sequence[0]]
    for i in sequence:
        if dummy[-1] != i:
            dummy.append(i)

    return dummy


print(unique_in_order("AAAABBBCCDAABBB"))
