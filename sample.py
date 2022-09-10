import cv2 
import numpy as np

img = cv2.imread("image.png")

# 全体をhsv化
# ほしい色領域をinRangeで抽出して白に変換
# ある座標範囲の部分（box)内に白(1)の数をカウント
# 全体の画素数で白のカウントを割った値が60％以上ならpub

# y, x
img1 = img[100:500, 10:450]

cv2.imshow("img", img)
cv2.imshow("img1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()