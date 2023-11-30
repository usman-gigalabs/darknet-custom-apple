import os

#write train file (just the image list)
with open('custom_cfg/train.txt', 'w') as out:
  for img in [f for f in os.listdir('custom_dataset/train') if f.endswith('jpg')]:
    out.write('custom_cfg/obj/' + img + '\n')

#write the valid file (just the image list)
with open('custom_cfg/valid.txt', 'w') as out:
  for img in [f for f in os.listdir('custom_dataset/valid') if f.endswith('jpg')]:
    out.write('custom_cfg/obj/' + img + '\n')

#write the test file (just the image list)
with open('custom_cfg/test.txt', 'w') as out:
  for img in [f for f in os.listdir('custom_dataset/test') if f.endswith('jpg')]:
    out.write('custom_cfg/obj/' + img + '\n')