# While-Loop - More Exercises
# 03 - Stream Of Letters

new_latter = input()
cond_c = False
cond_o = False
cond_n = False
word = ""
temp_word = ''

while new_latter != "End":
    ch = ord(new_latter)
    if 65 <= ch <= 90 or 97 <= ch <= 122:
        if new_latter == "c" and cond_c:
            temp_word = temp_word + new_latter

        elif new_latter == "c" and not cond_c:
            cond_c = True

        elif new_latter == "o" and cond_o:
            temp_word = temp_word + new_latter

        elif new_latter == "o" and not cond_o:
            cond_o = True

        elif new_latter == "n" and cond_n:
            temp_word = temp_word + new_latter

        elif new_latter == "n" and not cond_n:
            cond_n = True

        else:
            temp_word = temp_word + new_latter

        if cond_c and cond_o and cond_n:
            word += temp_word + " "
            # print(word)
            temp_word = ""
            cond_c = False
            cond_o = False
            cond_n = False

    new_latter = input()

print(word)
