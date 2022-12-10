def remove_and_strip(string,word):
    newStr = string.replace(word, '')
    return newStr.strip()

this = '     sam is good     '
n= remove_and_strip(this, 'sam')
print(n)
#print(this)
#print(this.strip())