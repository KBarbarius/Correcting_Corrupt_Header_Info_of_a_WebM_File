import os

def find_pattern(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        pattern = b'\x1a\x45\xdf'
        start_index = data.find(pattern)
        if start_index != -1:
            return data[start_index:]
        else:
            print("Pattern not found")
            return None

def copy_content(file_path, new_folder):
    filename = os.path.basename(file_path)
    new_path = os.path.join(new_folder, filename)
    content = find_pattern(file_path)
    if content is None:
        return

    with open(new_path, 'wb') as new_file:
        new_file.write(content)

def process_folder(folder_path):
    new_folder = 'C:\\Users\\USER\\OneDrive\\Downloads\\AllVideosRepaired'
    os.makedirs(new_folder, exist_ok=True)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            copy_content(file_path, new_folder)

# Replace 'your_folder_path' with the path to your folder containing webm files
folder_path = 'D:\\AllVideos'
process_folder(folder_path)
