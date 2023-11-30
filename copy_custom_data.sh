
rm custom_cfg/custom.names
rm custom_cfg/train.txt custom_cfg/valid.txt custom_cfg/test.txt
cp custom_dataset/train/_darknet.labels custom_cfg/custom.names
rm -rf custom_cfg/obj
mkdir custom_cfg/obj
#copy image and labels
cp custom_dataset/train/*.jpg custom_cfg/obj/
cp custom_dataset/valid/*.jpg custom_cfg/obj/

cp custom_dataset/train/*.txt custom_cfg/obj/
cp custom_dataset/valid/*.txt custom_cfg/obj/