
import pandas


code=pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict={row.letter:row.code for (index,row) in code.iterrows()}
user_input=input("what's your name").upper()
list=[code_dict[n] for n in user_input]


print(list)



