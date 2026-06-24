with open('./data/classes.txt') as f:
    classes = [line.strip() for line in f]

with open('./data.yaml', 'w') as f:
    f.write('path: /content/dataset\n')
    f.write('train: train/images\n')
    f.write('val: val/images\n')
    f.write('\n')
    f.write('names:\n')
    for i, c in enumerate(classes):
        f.write(f'  {i}: {c}\n')

print("data.yaml created")