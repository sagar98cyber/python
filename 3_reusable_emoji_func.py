#creating a reusable function for this code
#https://github.com/sagar98cyber/python/blob/seventeenth-branch/4_emoji_converter.py

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)' : '😃',
        ':(' : '😥'
    }

    output = ''
    for word in words:
        output += emojis.get(word,word) + ' '
    return output
    
message = input('>')
output = emoji_converter(message)
print(output)