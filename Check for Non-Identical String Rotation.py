
def isNonTrivialRotation(s1, s2):
    if s1==s2:
      return False
    elif len(s1)!=len(s2):
      return False
    else:
      s2=s2*2
      if s1 in s2:
        return True
      else:
        return False
        
