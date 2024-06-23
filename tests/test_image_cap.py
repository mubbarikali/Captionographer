import unittest
from PIL import Image
from others.image_cap import generate_caption

class TestImageCap(unittest.TestCase):
    
    def test_generate_caption(self):
        img = Image.new('RGB', (100, 100))
        caption = generate_caption(img)
        self.assertIsInstance(caption, str)
    
if __name__ == '__main__':
    unittest.main()
