bad_words = ['bookCover']

with open('/home/deeplearning/Documents/CodePractices/goodreads.xml') as oldfile, open('/home/deeplearning/Documents/CodePractices/picturebook.xml', 'w') as newfile:
    for line in oldfile:
        if any(bad_word in line for bad_word in bad_words):
            newfile.write(line)