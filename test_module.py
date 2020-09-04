from palindrome import  palindrome

def test_palindrome():
    assert palindrome("eye") == True
    assert palindrome("_eye") == True
    assert palindrome("race car") == True
    assert palindrome("not a palindrome") == False
    assert palindrome("A man, a plan, a canal. Panama") == True
    assert palindrome("never odd or even") == True
    assert palindrome("nope") == False
    assert palindrome("almostomla") == False
    assert palindrome("My age is 0, 0 si ega ym.") == True
    assert palindrome("1 eye for of 1 eye.") == False
    assert palindrome("0_0 (: /-\ :) 0-0") == True
    assert palindrome("five|\_/|four") == False

    print("YOUR CODE IS CORRECT!")
