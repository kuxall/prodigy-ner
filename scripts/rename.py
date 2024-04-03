import os

def rename_files(path):
    i = 1
    for filename in os.listdir(path):
        file_basename, file_extension = os.path.splitext(filename)
        new_filename = f"{i}_{file_basename}{file_extension}"
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        i += 2

if __name__ == "__main__":
    directory_path = "/home/kushal/Documents/spacyprodigy/outputfiles"
    rename_files(directory_path)
