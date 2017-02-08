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
