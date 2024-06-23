import unittest
from unittest.mock import patch, mock_open
from url_images_caption import *

class TestUrlImagesCaption(unittest.TestCase):
    
    @patch("url_images_caption.requests.get")
    def test_url_image_captioning(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = '<html><img src="https://example.com/image.jpg"></html>'
        mock_get.return_value.content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00'

        with patch("builtins.open", mock_open()) as mocked_file:
            caption_image_from_url("https://en.wikipedia.org/wiki/IBM")
            mocked_file.assert_called_once_with("captions.txt", "w")
    
if __name__ == '__main__':
    unittest.main()
