from glob import glob

file_list_train_pos = [f for f in glob("./data/train/pos/*.txt")]
file_list_train_neg = [f for f in glob("./data/train/neg/*.txt")]
file_list_test_pos = [f for f in glob("./data/test/pos/*.txt")]
file_list_test_neg = [f for f in glob("./data/test/neg/*.txt")]

reviews = []

for review in file_list_train_pos:
    with open(review) as f:
        reviews.append(['pos', 'train', f.read()])

for review in file_list_train_neg:
    with open(review) as f:
        reviews.append(['neg', 'train', f.read()])

for review in file_list_test_pos:
    with open(review) as f:
        reviews.append(['pos', 'test', f.read()])

for review in file_list_test_neg:
    with open(review) as f:
        reviews.append(['neg', 'test', f.read()])

with open('reviews.csv', 'w') as f:
    counter = 0
    for review in reviews:
        f.write(f'{review[0]}¿¿{review[1]}¿¿{review[2]}\n')
