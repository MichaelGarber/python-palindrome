import re
def palindrome(str):
    str = re.sub('[\W\_]','',str)
    str = str.lower()
    reverseStr = str[::-1]
    return (reverseStr == str)