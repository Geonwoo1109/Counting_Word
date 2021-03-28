import json
import pandas as pd

a = "The quick brown fox jumps over the lazy dog dog"
a_ = a.split(" ")

File_location = "/content/TestFile.cell"

myFile = pd.read_excel(File_location,
                       header = 1,
                       usecols = "c")

print(myFile)


for i in myFile:
  print("가", i)



print("\n\n\n\n\n")

json = {}
#print(json)

print("a의 길이: ", len(a))
print(a_, "\n --> ", len(a_), "개")




for i in range(0, len(a_)):
  print (i,a_[i])
  try:
    json[a_[i]] = int(json[a_[i]]) + 1
  except KeyError:
    json[a_[i]] = 1

print(json)
