# Daily programmer #380
def smorse(inp):
    raw_morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
    raw_letters = 'abcdefghijklmnopqrstuvwxyz'
    morse = {}
 
    # Create dictionary with letter to morse mapping
    for num, letter in enumerate(raw_morse.split(' ')):
        morse[raw_letters[num]] = letter
 
    result = ''
    for letter in inp: # For each letter in the inputed sequence
        result += morse[letter] + ' ' # Added whitespace padding for clarity
    print(result)
 
smorse(input('word:'))

print(smorse('manish'))