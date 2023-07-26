# Python101

This Python script, organize_files.py, is designed to help you organize files in a specified folder based on their file types. It uses a predefined dictionary file_types to map file extensions to their corresponding folder names. If a file type is not found in the dictionary, the script will move the file to an "Others" folder.

## Usage:

Ensure you have Python installed on your system.
Download the organize_files.py script to your desired location.
Open the script in a text editor and update the folder_path variable with the path of the folder you want to organize.

```
folder_path = "/Users/your_username/Downloads"
```
Save the changes.
Open a terminal or command prompt, navigate to the directory where the organize_files.py script is located.
Run the script by executing the following command:
```
python organize_files.py
```
The script will organize the files in the specified folder based on their file types.
Caution:

Before running the script, make sure you understand its functionality and verify the folder_path to avoid unintended consequences.
It is recommended to create a backup of your files before organizing them with this script.
Customization:
You can customize the file_types dictionary in the script to include additional file extensions and their corresponding folder names. For example, if you want to add support for GIF files, you can modify the dictionary like this:

```
file_types = {
    'pdf': 'PDF',
    'csv': 'CSV',
    'gif': 'GIF',  # Add support for GIF files
    # ... other file types ...
    'zip': 'ZIP'
}
```
Note:

This script is provided as-is without any warranty. Use it at your own risk.
The script assumes that the specified folder exists. If the folder does not exist, the script will raise an error.
## Contributors

- [Fernando](https://github.com/refnando)

