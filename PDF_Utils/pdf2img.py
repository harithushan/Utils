# converting pdf to images
import os
import shutil
from PyPDF2 import PdfReader
from pdf2image import convert_from_path

def split_pdf_to_images(pdf_path, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract PDF file name without extension
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.join(output_dir, pdf_filename)
    os.makedirs(output_folder, exist_ok=True)

    # Read the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Convert each page to an image
        for page_num in range(num_pages):
            # Convert page to image
            images = convert_from_path(pdf_path, first_page=page_num+1, last_page=page_num+1)

            # Save the image
            image_path = os.path.join(output_folder, f'{pdf_filename}_page{page_num + 1}.jpg')
            images[0].save(image_path, 'JPEG')

    print(f'PDF pages successfully converted to images. Saved in: {output_folder}')



pdf_path = 'docs/pdfs/BANK.pdf'
output_directory = 'images/'

split_pdf_to_images(pdf_path, output_directory)
