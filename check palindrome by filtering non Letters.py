def isAlphabeticPalindrome(code):
    n=len(code)
    code=code.lower()
    rev=n-1
    i=0
    ispalindrome=True
    while i<rev:
        
        charA,charB=code[i],code[rev]
        if not charA.isalpha():#compare next
            i+=1
            continue
        if not charB.isalpha():#compare next
            rev-=1
            continue
        if charA!=charB: 
            return False #ab if found any alphabet which is not equal to another
        i+=1
        rev-=1
    return ispalindrome
