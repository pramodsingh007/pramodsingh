


morse_list = {
    " ": "/",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}
word_list = {}

for key,value in morse_list.items():
    word_list[value] = key

method = input("what do you want choose e  to encode d for decode: ").lower()
message = input("enter your message here: ").lower()


if method == "e":
    encoded_msg = ""
    for msg in message:
        word = morse_list[msg]
        encoded_msg+=word
    print(f"your incoded msg is {encoded_msg}")

elif method == "d":
    decoded_msg = ""
    for msg in message:
        word = word_list[msg]
        decoded_msg+=word
    print(f"your decode msg is {decoded_msg}")
