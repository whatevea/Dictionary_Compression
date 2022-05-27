import re
import json
array_file=open ("word_array.json","r")
dictwords=json.load(array_file)["words"]
array_file.close()
file_to_decode=open("compressed.txt","r").read()
save_file=open("uncompressed.txt","w")
for items in re.findall(r"`\d*", file_to_decode):
	items_num=int(items.split("`")[1])
	# print(items_num)
	file_to_decode=file_to_decode.replace(str(items),dictwords[items_num])
# print (file_to_decode)
save_file.write(file_to_decode)
