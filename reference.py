############# Command line argument parser
argument_parser = argparse.ArgumentParser("Script. ")
argument_parser.add_argument('-m', '--model', help='help message', required=True)
args = argument_parser.parse_args()

model_dir = args.model

##############
array = [1, 2, 3, 4, 5]
s = "\n".join([str(x) for x in array]) # Separate the array value with "\n" and output a string
print(s)

##############
str = "Hello World!\n"
str = str.rstrip("\n") 	# To get rid of \n
str = str.split("\n")

############## enumerate to have index and values at the same time
dict = {'a':1, 'b':2, 'c':3}
list = ['a', 'b', 'c']
for index, key in enumerate(dict.keys()):
	print(index, key)
for index, key in enumerate(list):
	print(index, key)

############# Looping through multiple lists
a = ['a', 'b', 'c']
b = [1, 2, 3]

# List Comprehensions
for x, y in [(x, y) for x in a for y in b]:
  print x, y

# Map Function
for x, y in map(None, a, b):
    print x, y
   
# Zip Function    
for x, y in zip(a, b):
    print x, y

############## Using pickle
import pickle

data = {'a':1, 'b':12, 'c':4}
file = open("tttt.pkl", "wb")
pickle.dump(data, file)
file.close()

file = open("tttt.pkl", "rb")
b = pickle.load(file)
print(data==b)


############# File writing and reading
with open("testing1.txt", "w") as f:
	f.writelines("Hello\n")
	f.writelines("World")

with open("testing2.txt", "w") as f:
	f.write("Hello\n")
	f.write("World")

with open("testing2.txt", "r") as f:
	str = f.readline().rstrip("\n")
	print(str)
