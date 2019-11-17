import os
for filename in os.listdir('/home/deeplearning/Documents/CodePractices/goodreads/'):
    with open('/home/deeplearning/Documents/CodePractices/goodreads/'+filename) as oldfile, open('/home/deeplearning/Documents/CodePractices/goodreads/clean'+filename, 'w') as newfile:
        for line in oldfile:
            line = line.split('title=', 1)[-1]
            newfile.write(line)