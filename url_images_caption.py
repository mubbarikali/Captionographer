import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration
import gradio as gr

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_captions_from_url(url: str):
    try:
        # Download the page
        response = requests.get(url)
        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all img elements
        img_elements = soup.find_all('img')

        captions = []

        # Iterate over each img element
        for img_element in img_elements:
            img_url = img_element.get('src')

            # Skip if the image is an SVG or too small (likely an icon)
            if 'svg' in img_url or '1x1' in img_url:
                continue

            # Correct the URL if it's malformed
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif not img_url.startswith('http://') and not img_url.startswith('https://'):
                continue  # Skip URLs that don't start with http:// or https://

            try:
                # Download the image
                img_response = requests.get(img_url)
                # Convert the image data to a PIL Image
                raw_image = Image.open(BytesIO(img_response.content))
                if raw_image.size[0] * raw_image.size[1] < 400:  # Skip very small images
                    continue

                raw_image = raw_image.convert('RGB')

                # Process the image
                inputs = processor(raw_image, return_tensors="pt")
                # Generate a caption for the image
                out = model.generate(**inputs, max_new_tokens=50)
                # Decode the generated tokens to text
                caption = processor.decode(out[0], skip_special_tokens=True)

                captions.append(f"{img_url}: {caption}")
            except Exception as e:
                captions.append(f"Error processing image {img_url}: {e}")
                continue

        return "\n".join(captions)
    except Exception as e:
        return f"Error processing URL {url}: {e}"

# Gradio interface
iface = gr.Interface(
    fn=generate_captions_from_url, 
    inputs=gr.Textbox(lines=2, placeholder="Enter URL here..."), 
    outputs="text",
    title="URL Image Captioning",
    description="Enter a URL to generate captions for all images on the page."
)

if __name__ == "__main__":
    iface.launch()
