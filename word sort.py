word_lst = ['job', 'jam', 'orange', 'apple', 'java',
            'oregano', 'box', 'card', 'camera']
no_of_pass = 0
length = len(word_lst)
print('og', word_lst)

for j in range(1, length):
    i = 0
    while i < min(len(word_lst[j-1]), len(word_lst[j])) and j > 0:
        print('pass')
        if word_lst[j-1][i] > word_lst[j][i]:
            while word_lst[j-1][i] > word_lst[j][i] and j > 0:
                word_lst[j-1], word_lst[j] = word_lst[j], word_lst[j-1]
                j -= 1
        else:
            i += 1
        no_of_pass += 1
print('new', word_lst)
for each_word in word_lst:
    print(each_word+'-', end='')
print('no of pass', no_of_pass)
