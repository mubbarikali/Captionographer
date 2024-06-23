import unittest
from unittest.mock import patch, mock_open
from PIL import Image
from local_images_caption import *

class TestLocalImagesCaptioner(unittest.TestCase):
    
    @patch("local_images_captioner.glob.glob")
    @patch("local_images_captioner.Image.open")
    @patch("builtins.open", new_callable=mock_open)
    def test_local_image_captioning(self, mocked_open, mocked_image_open, mocked_glob):
        mocked_glob.return_value = ["image1.jpg", "image2.png"]
        mocked_image_open.return_value = Image.new('RGB', (100, 100))
        
        caption_images_from_local("/path/to/your/images")
        mocked_open().write.assert_called()
    
if __name__ == '__main__':
    unittest.main()
