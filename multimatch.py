import cv2
import glob
import operator
import sys


def preprocess(img):
    img2 = img[:,:,2]
    img2 = img2 - cv2.erode(img2, None)
    return img2


def scale(img, scale):
    return cv2.resize(img, (0,0), fx=scale, fy=scale)


def show_wait(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread(sys.argv[1])
img = scale(img, 1.0/3)
img = preprocess(img)


def match_template(template_file):
    template = cv2.imread(template_file)
    template = preprocess(template)
    ccnorm = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
    return ccnorm.max()

directory = sys.argv[2]

res = [(tf, match_template(tf)) for tf in glob.glob(directory + "/*.png")]

res.sort(key=operator.itemgetter(1))

for x in res:
    print x
