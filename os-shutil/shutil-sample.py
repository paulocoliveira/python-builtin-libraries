import shutil

# Move a file to a different location
shutil.move('my-file.txt', 'test_directory/my-file.txt')

# Copy a directory to a new location
shutil.copytree('test_directory', 'backup_directory')