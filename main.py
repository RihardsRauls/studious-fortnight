def remover(input_text):
    text = ""
    vowels = ['a', 'i', 'o', 'e', 'u', 'A', 'E', 'I', 'U', 'O']
    special_character = ['!', '.', '?', '/']
    for letter in input_text:
        if letter not in vowels and letter not in special_character:
            text += letter
    return text

def length():
    ...

def main():
    tweet = str(input("Tweet!"))
    clean_tweet = remover(tweet)

    if len(clean_tweet) > 280:
        print("The tweet is too long")
    else:
        print(clean_tweet)

if __name__ == "__main__":
    main()