import os
import math

from dotenv import load_dotenv
load_dotenv()


# only for 0+
def pad_num(n, len=3):
    if n == 0:
        return '0'*len

    digits = int(math.log10(n))+1
    return '0'*(len-digits) + str(n)


def get_urls():
    return [os.environ.get('POD_URL') + '/' + pad_num(i) for i in range(491)]


print(get_urls())
