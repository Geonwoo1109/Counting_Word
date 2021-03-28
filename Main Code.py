import json

a = "The quick brown fox jumps over the lazy dog dog"
a_ = a.split(" ")

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
