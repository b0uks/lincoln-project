import pyap
import re

def get_addy(text):
    #typical text pattern:
    # 1 - 5 numbers
    # street name
    # street identifier
    # city name
    # state name

    # TODO add more states to the regex
    # TODO add specific street names: street/st, alley, drive/dr, loop... https://en.wikipedia.org/wiki/Types_of_road
    address = re.search(r"(\d{1,6})\s*([A-Za-z]\s*){9,}\s*(AL|AK|AZ|AR|CA|IL|TX|)", text, re.M)

    if address:
        # for a in address:
        #     print(a)
        print(address.group())
        # print("group0", address.group(0))
        # print("group1", address.group(1))
        # print("group2", address.group(2))
        # print("group3", address.group(3))
        return address.group(0)
    else:
        print('na')
        print('na')
        return ''
