from zipfile import ZipFile 
import os 
folder_to_zip = "/content/dslim/bert-base-NER/checkpoint-3000/"

# Name of the output zip file
zip_filename = "model_bert_new_1.zip"

# Create a zip file
with ZipFile(zip_filename, "w") as zf:
    # Walk through the folder
    for dirname, subdirs, files in os.walk(folder_to_zip):
        # Calculate the relative path for the directory inside the zip
        arc_dirname = os.path.relpath(dirname, start=os.path.dirname(folder_to_zip))
        zf.write(dirname, arcname=arc_dirname)
        
        # Add files to the zip with their relative paths
        for filename in files:
            file_path = os.path.join(dirname, filename)
            arc_filepath = os.path.join(arc_dirname, filename)
            zf.write(file_path, arcname=arc_filepath)

print(f"Zipped {folder_to_zip} into {zip_filename}")