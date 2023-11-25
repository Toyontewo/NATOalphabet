import pandas as pd
nato = pd.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
phonetic_dict = {row.letter:row.code for (index, row) in nato.iterrows()}


word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letters] for letters in word]
print(output_list)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

