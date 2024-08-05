#import textwrap

def wrap(string, max_width):
    cadret=''
    for i in range((len(string)//max_width)+1):
        cadret=cadret+string[i*max_width:(i*max_width+max_width)]+'\n'
    return cadret

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)