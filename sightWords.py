
week2 = ['new', 'barn', 'shark', 'hold', 'art', 'only', 'eyes']
week5 = ['subtract', 'add']
week10 = ['girl', 'house', 'best', 'thing', 'easy', 'wrong', 'right', 'again', 'above']
week13 = ['question']
week17 = []

def createSentence(week2):
    if len(week2) == 7:
        return week2[0] + ' , ' + week2[1] + ' , ' + week2[2]  + ' , ' + week2[3] + ' , ' + week2[4] + ' , ' + week2[5]+ ' and ' + week2[6]

print('The 7 sight words for this week are', createSentence(week2) + '.')
# Program Name: sightwords.py
# Program Description: This program outputs a list of info in array
# Programmer Name: Devin Brown

def createSentence(week5):
    if len(week5) == 2:
        return week5[0] + ' and ' + week5[1]
print('The 2 sight words for this week are', createSentence(week5) + '.')

week10 = ['girl', 'house', 'best', 'thing', 'easy', 'wrong', 'right', 'again', 'above']

def createSentence(week10):
    if len(week10) == 9:
        return week10[0] + ' , ' + week10[1] + ' , ' + week10[2]  + ' , ' + week10[3] + ' , ' + week10[4] + ' , ' + week10[5]+ ' , ' + week10[6] + ' , ' + week10[7] + ' and ' + week10[8]
print('The 9 sight words for this week are', createSentence(week10) + '.')


def createSentence(week13):
    if len(week13) == 1:
        return week13[0]
print('The sight words for this week is', createSentence(week13) + '.')


def createSentence(week17):
    if len(week17) == 0:
        return week13[0]
print('There are no sight words for this week.')