def pig_it(text: str) -> str:
    dummy = ""
    pig_list = []
    text_list = text.split()
    allowed = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    for t in text_list:
        for i in t:
            if i in allowed:
                dummy = t[1:] + t[0] + "ay"
            else:
                dummy = i

            pig_list.append(dummy)
            break

    return " ".join(pig_list)


print(pig_it("Hello world !"))
