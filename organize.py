import os
import shutil

def organize_files(folder_path):
    file_types = {
        'pdf': 'PDF',
        'csv': 'CSV',
        'dmg': 'DMG',
        'mobi': 'MOBI',
        'ics': 'ICS',
        'pkg': 'PKG',
        'jpg': 'JPG',
        'jpeg': 'JPEG',
        'xlsx': 'XLSX',
        'ppt': 'PPT',
        'pptx': 'PPTX',
        'doc': 'DOC',
        'docx': 'DOCX',
        'mp4': 'MP4',
        'txt': 'TXT',
        'png': 'PNG',
        'xml': 'XML',
        'zip': 'ZIP'
    }

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            file_extension = os.path.splitext(file)[1][1:].lower()  # Get the file extension in lowercase

            # Get the corresponding file type or 'Others' if not found in the list
            file_type = file_types.get(file_extension, 'Others')

            # Create the folder if it does not exist
            if not os.path.exists(os.path.join(folder_path, file_type)):
                os.makedirs(os.path.join(folder_path, file_type))

            # Move the file to the appropriate folder
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, file_type, file))

    print("Files organized successfully.")

# Path of the folder you want to organize
folder_path = "/your/path/ToBeOrganized"

# Call the function to organize the files
organize_files(folder_path)
