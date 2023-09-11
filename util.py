import numpy as np
import cv2


def preprocess_pres_pd(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )
    return processed_image


def preprocess_vr(img):
    gray = cv2.cvtColor(np.array(img),  cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    processed_img = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 75, 31)
    return processed_img


def thresh_global(img):
    _, result_image = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY_INV)
    return result_image


def thresh_adaptive(img):
    result_image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 13, 2)
    return result_image


def preprocess_mh(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (608, 800))
    img1 = resized[157:217, 34:531]  # (34,157) (531,217)
    img2 = resized[231:287, 42:531]  # (42,231) (531,287)
    img3 = resized[296:348, 43:360]  # (43,296) (360,348)
    img4 = resized[358:419, 39:278]  # (39,358) (278,419)
    img5 = resized[428:482, 40:265]  # (40,428) (265,482)
    img6 = resized[494:548, 32:343]  # (32,494) (343,548)
    img7 = resized[559:610, 34:371]  # (34,559) (371,610)
    img8 = resized[628:687, 26:261]  # (26,628) (261,687)

    img_1 = thresh_adaptive(img1)
    img_2 = thresh_adaptive(img2)
    img_3 = cv2.adaptiveThreshold(img3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 6)
    img_4 = thresh_adaptive(img4)
    img_5 = thresh_global(img5)
    img_6 = thresh_global(img6)
    img_7 = thresh_adaptive(img7)
    img_8 = cv2.adaptiveThreshold(img8, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 23, 24)

    return img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8



