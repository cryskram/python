def solution(s: str) -> str:
    wordList = []
    dummy = ""
    for i in s:
        if i.islower():
            dummy = dummy + i
        else:
            wordList.append(dummy)
            dummy = i

    wordList.append(dummy)

    return " ".join(wordList)


print(solution("helloWorld"))
