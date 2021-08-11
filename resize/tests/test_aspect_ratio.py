import unittest
import cv2
from resize import resize_with_aspect


class ResizeTestCase(unittest.TestCase):
    def _demo_image(self, img):
        cv2.imshow("Test", img)
        cv2.waitKey(0)

    def test_aspect_ratio(self):
        c_w, c_h = 300, 360  # 縦
        i_w, i_h = 150, 200  # 縦

        ori = cv2.imread("demo_w.jpg")
        img = resize_with_aspect(ori, 200, 200)
        self._demo_image(img)
        img = resize_with_aspect(ori, 300, 200,bg_color=(255,0,0))
        self._demo_image(img)
        img = resize_with_aspect(ori, 200, 300)
        self._demo_image(img)
        img = resize_with_aspect(ori, 100, 400)
        self._demo_image(img)
        img = resize_with_aspect(ori, 600, 600)
        self._demo_image(img)
        img = resize_with_aspect(ori, width=600)
        self._demo_image(img)
        img = resize_with_aspect(ori, scale=0.1)
        self._demo_image(img)

        ori = cv2.imread("demo_h.jpg")
        img = resize_with_aspect(ori, 200, 200)
        self._demo_image(img)
        img = resize_with_aspect(ori, 300, 200)
        self._demo_image(img)
        img = resize_with_aspect(ori, 200, 300)
        self._demo_image(img)
        img = resize_with_aspect(ori, 100, 400)
        self._demo_image(img)
        img = resize_with_aspect(ori, 10, 20)
        self._demo_image(img)




if __name__ == '__main__':
    unittest.main()
