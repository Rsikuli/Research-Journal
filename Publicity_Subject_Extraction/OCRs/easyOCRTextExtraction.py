import cv2
import easyocr #type : ignore

# Initialize EasyOCR
reader = easyocr.Reader(['fr', 'en'])

def easyOCR_extract(IMAGE_PATH):
    """
    Extracts text from an image using EasyOCR model.
    Args:
        IMAGE_PATH (str): The file path to the image from which text is to be extracted.
    Returns:
        str: The extracted text from the image.
    Raises:
        FileNotFoundError: If the image at the specified path cannot be loaded.
    """
    # Image Threshold
    img_bgr = cv2.imread(IMAGE_PATH)
    
    # Check if the image was loaded successfully
    if img_bgr is None:
        raise FileNotFoundError(f"Error: Unable to load image at {IMAGE_PATH}")
    
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Text Extraction
    result = reader.readtext(img_rgb, detail=0, paragraph=True)
    result = " ".join(result)
    return result
