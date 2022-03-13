str = input()
def stc(text):
        import re
        return ''.join(x.capitalize() or '_' for x in text.split('_'))

print(stc(str))