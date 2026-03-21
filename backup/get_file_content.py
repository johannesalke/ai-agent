import os


def get_file_content(working_directory, file_path):
    try:
        MAX_CHAR = 2000
        print(working_directory)
        print(file_path)
        
        #working_dir_abs = os.path.abspath(os.path.curdir)
        #dir_path = os.path.normpath(os.path.join(os.path.curdir, working_directory)) 
        #print(dir_path)
        #full_file_path = os.path.join(dir_path,file_path)

        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path)) 
        print(target_file)
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        print(valid_target_dir)
        print(os.path.commonpath([working_dir_abs,target_file]))
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        
        with open(target_file,"r") as f:
            content = f.read(MAX_CHAR)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'

        return content
    except:
        return f"Error reading file:{file_path}"