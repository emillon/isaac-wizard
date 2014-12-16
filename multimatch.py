import cv2
import glob
import numpy
import operator
import os.path
import sys


def preprocess(img):
    img2 = img[:,:,2]
    img2 = img2 - cv2.erode(img2, None)
    return img2


def scale(img, scale):
    return cv2.resize(img, (0,0), fx=scale, fy=scale)


def scale_point((x, y), scale):
    return (x*scale, y*scale)

def show_wait(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread(sys.argv[1])
img_orig = img
img = scale(img, 1.0/3)
img = preprocess(img)


def match_template(template_file):
    template = cv2.imread(template_file)
    template = preprocess(template)
    ccnorm = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
    return (tf, template, ccnorm, ccnorm.max())

directory = sys.argv[2]

res = [match_template(tf) for tf in glob.glob(directory + "/*.png")]

res.sort(key=operator.itemgetter(3))
res = res[-2:]

out = img_orig

for (tf, template, ccnorm, maxnorm) in res:
    name = os.path.splitext(os.path.basename(tf))[0]
    loc = numpy.where(ccnorm == maxnorm)
    threshold = 0.3
    th, tw = scale_point(template.shape[:2], 3)
    for pt in zip(*loc[::-1]):
        if ccnorm[pt[::-1]] < threshold:
            continue
        pt = scale_point(pt, 3)
        cv2.rectangle(out, pt, (pt[0] + tw, pt[1] + th),
                (0, 0, 255), 2)
        text_pt = (pt[0], pt[1] + th + 30)
        cv2.putText(out, name, text_pt, cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        print name

show_wait(out)
