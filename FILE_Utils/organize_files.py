import os
import shutil

def organize_files(source_path, output_path):
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            
            extension = os.path.splitext(filename)[1]
            new_dir = os.path.join(output_path, extension)

            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            src_file = os.path.join(dirpath, filename)
            dst_file = os.path.join(new_dir, filename)

            shutil.move(src_file, dst_file)
            print(f"Moved {filename} to {new_dir}")
            

# source_path= 'D:/Users/documens/input_path',
# output_path= 'D:/Users/documens/output_path'
# organize_files(source_path, output_path)
