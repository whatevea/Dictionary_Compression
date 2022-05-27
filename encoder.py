import os
# load the array file content into variable
import json
array_file=open ("word_array.json","r")
dictwords=json.load(array_file)["words"]

array_file.close()

# load the target file to be encoded
target_file_size = os.path.getsize('targetfile.txt') 
target_file=open("targetfile.txt","r").read()
trimmed=target_file.split()
# print(trimmed)
# lowercase all and check in dict
dump=[]
for word in trimmed:
	if word.lower() in dictwords and len(word)>len(str(dictwords.index(word.lower()))):
		# print(f'{word} in {dictwords.index(word.lower())}')
		dump.append(f'`{dictwords.index(word.lower())}')
	else:
		dump.append(word)
dumps=" ".join(dump)
# save in another file
open("compressed.txt","w").write(dumps)
compressed_file_size= os.path.getsize('compressed.txt') 
print(f"Total bytes removed :: {target_file_size-compressed_file_size}")
print(f"Compression ratio   :: {round(compressed_file_size/target_file_size*100)}%")