import os
from PIL import Image
from PyPDF2 import PdfWriter, PdfFileReader
from PyPDF2 import PageObject
from PyPDF2.generic import BooleanObject

def images_to_pdf(input_directory, output_directory):
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through all folders in the input directory
    for foldername in os.listdir(input_directory):
        folder_path = os.path.join(input_directory, foldername)
        if os.path.isdir(folder_path):
            # Create a PDF writer
            pdf_writer = PdfWriter()

            # Iterate through all image files in the folder
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(folder_path, filename)
                    image = Image.open(image_path)

                    # Create a new page object and add the image to it
                    pdf_page = PageObject.create_blank_page(None, image.width, image.height)
                    pdf_page.add_transformation(PdfFileReader().create_page_formXObject(pdf_page), 1, 0, 0)
                    pdf_page.merge_page(PdfFileReader(image_path).getPage(0), expand=False)

                    # Add the page to the PDF writer
                    pdf_writer.addPage(pdf_page)

            # Save the PDF file
            pdf_filename = foldername + '.pdf'
            output_path = os.path.join(output_directory, pdf_filename)
            with open(output_path, 'wb') as file:
                pdf_writer.write(file)

            print(f'Images from folder {foldername} successfully converted to PDF. Saved as: {output_path}')


# # Example usage
# input_directory = 'imgs/'
# output_directory = 'imgs/'

# images_to_pdf(input_directory, output_directory)
