while(1):
  p = input("p: ")
  if (p == "a" or p == "k"):
    print("\n")
  else:
    print("입력 값이 잘못되었습니다.")
    continue
    
  w = input("w: ")
  
  if (p == "a"):
    a = w * 0.5
  else:
    a = w * 0.3
    
  a (p, w)
  
  break
  
def a (p, w):
  print("환자가 " + p + "인 사람에게 " + a + "만큼 투여함")
