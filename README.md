# Captionographer

#### Version 1.0

---

## Overview

**Captionographer** is a Python web application designed to generate captions for images using the BLIP2 model from HuggingFace's transformers library. With a user-friendly Gradio web UI, Captionographer supports various functionalities, including captioning single or multiple images from URLs, as well as uploading local images for captioning.

---

## Features

- **Single Image Captioning via URL**: Generate captions for a single image provided through a URL.
- **Multiple Image Captioning via URL**: Generate captions for multiple images on a webpage, such as a Wikipedia page.
- **Single Local Image Upload**: Upload and caption a single image from your local computer using the Gradio web UI.
- **Multiple Local Images Upload**: Upload and caption multiple images from your local computer using the Gradio web UI.

---

## Installation

To get started with Captionographer, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/captionographer.git
    cd captionographer
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Single Image Captioning via URL

Run the provided script to generate captions for single images from URLs.

### Multiple Image Captioning via URL

Run the `automate_url_captioner.py` script to generate captions for all images on a given webpage.

### Single Local Image Upload

Run the `image_cap.py` script to generate captions for a single local image.

### Multiple Local Images Upload

Run the `local_images_captioner.py` script to generate captions for multiple local images.

### Gradio Web UI

Run the `image_captioning_app.py` script to launch the Gradio web interface for easy image upload and captioning.

```bash
python image_captioning_app.py
```

---

## Technologies Used

- **Python**: The primary programming language used for development.
- **HuggingFace Transformers**: Used for the BLIP2 model implementation.
- **Gradio**: Provides the web UI for interacting with the application.
- **PIL**: Used for image processing.
- **BeautifulSoup**: Used for web scraping functionalities.

---

## Contributing

Contributions from the community are most welcome. If you have suggestions or find bugs, please create an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- Special thanks to [HuggingFace](https://huggingface.co/) for providing the BLIP2 model and transformers library.
- Thanks to [Gradio](https://gradio.app/) for the web UI framework.
- Thanks to [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping functionality.

---

## Contact

For any questions or support, please contact [https://www.linkedin.com/in/mubbarikali/](https://www.linkedin.com/in/mubbarikali/)
