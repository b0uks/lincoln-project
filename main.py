# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


try:
    from PIL import Image
except ImportError:
    import Image
import argparse
import pytesseract
from ocr import *
from get_addr import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess1", type=str, default="thresh",
                    help="type of preprocessing to be done")
    ap.add_argument("-b", "--preprocess2", type=str, default="",
                    help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    filename, img = load_process_image(args)

    text = img_to_string(filename, img)

    print(text)

    address = get_addy(text)



    show_img(filename, img)




