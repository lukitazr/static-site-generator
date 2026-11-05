import os
import shutil


def copy_files_recursive(source_dir_path, dest_dir_path, is_root=True):
    if not os.path.exists(source_dir_path):
        raise ValueError(f"Source directory does not exist: {source_dir_path}")

    if is_root:
        if os.path.exists(dest_dir_path):
            print(f"Deleting existing destination directory: {dest_dir_path}")
            shutil.rmtree(dest_dir_path)
        print(f"Creating destination directory: {dest_dir_path}")
        os.mkdir(dest_dir_path)
    elif not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(from_path):
            print(f"Copying file: {from_path} -> {dest_path}")
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path, is_root=False)


copy_directory = copy_files_recursive
copy_directory_recursive = copy_files_recursive

