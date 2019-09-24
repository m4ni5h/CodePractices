# Daily programmer #380
def smorse(inp):
    raw_morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
    raw_letters = 'abcdefghijklmnopqrstuvwxyz'
    morse = {}

    # Using Dictionary
    morse_dict = dict(zip(raw_letters, raw_morse.split()))
 
    # Create dictionary with letter to morse mapping
    for num, letter in enumerate(raw_morse.split(' ')):
        morse[raw_letters[num]] = letter
 
    result = ''
    for letter in inp: # For each letter in the inputed sequence
        result += morse_dict[letter] + ' ' # Added whitespace padding for clarity
    print(result)
 
print(smorse('manish'))