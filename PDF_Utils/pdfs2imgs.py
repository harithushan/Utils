import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path

def convert_pdfs_to_images(input_directory, output_directory):
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith('.pdf'):
            # Construct the input and output paths
            pdf_path = os.path.join(input_directory, filename)
            pdf_filename = os.path.splitext(filename)[0]
            output_folder = os.path.join(output_directory, pdf_filename)
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

            print(f'PDF pages from {filename} successfully converted to images. Saved in: {output_folder}')


# input_directory = 'docs/pdfs/' 
# output_directory = 'images/'

# convert_pdfs_to_images(input_directory, output_directory)
