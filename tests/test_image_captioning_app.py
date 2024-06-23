import unittest
import numpy as np
from image_captioning_app import caption_image

class TestImageCaptioningApp(unittest.TestCase):
    
    def test_caption_image(self):
        img_array = np.zeros((100, 100, 3), dtype=np.uint8)
        caption = caption_image(img_array)
        self.assertIsInstance(caption, str)

if __name__ == '__main__':
    unittest.main()
