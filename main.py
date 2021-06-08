# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    # print(letter_contents)

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    # print(names_list)
    for each_name in names_list:
        name = each_name.strip("\n")
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(str(letter_contents.replace("[name]", name)))
