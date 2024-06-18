alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift=int(input("Enter the number you want to shift"))

word=input("Enter the word")


def encode(w, num):
    encoded_word = ""
    for letter in w:
       n=alphabets.index(letter) + num
       n=n%26
       new_letter=alphabets[n]
       encoded_word+=new_letter
    print(encoded_word)

def decode(w, num):
    decoded_word = ""
    for letter in w:
        n=alphabets.index(letter) - num
        n=n%26
        decoded_letter=alphabets[n]
        decoded_word+=decoded_letter
    print(decoded_word)



decode(w=word,num=shift)
