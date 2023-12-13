def remove_vowels(s):
    stack = []
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(s)):
        if s[i].lower() not in vowels:
            stack.append(s[i])
    return "".join(stack)


print(remove_vowels("Hello, World!"))
