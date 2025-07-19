from spellchecker import SpellChecker

spell = SpellChecker()


def correct_text(text):
    words = text.split()
    corrected_words = []

    for word in words:
        corrected = spell.correction(word)
        corrected_words.append(corrected)

    return ' '.join(corrected_words)


def run():
    print("\n----- Spell Checker -----")

    while True:
        text = input('Enter text to check (or type "exit" to quit): ')
        if text.lower() == 'exit':
            print('Closing the program...')
            break

        corrected = correct_text(text)
        print(f'Corrected text: {corrected}')


if __name__ == "__main__":
    run()
