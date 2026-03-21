import os

def get_files_info(working_directory, directory="."):
    
    working_dir_abs = os.path.abspath(working_directory)
    print(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory)) 
    print(target_dir)
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot list "{target_dir}" as it is outside the permitted working directory'
    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'

    dirItemList = os.listdir(target_dir)
    #print(dirItemList)


    result = "Results for the current directory:\n"
    for item in dirItemList:
        #print(item)
        itemPath = os.path.join(target_dir,item)
        #print(itemPath)
        is_dir = os.path.isdir(itemPath)
        file_size = os.path.getsize(itemPath)
        result += f"  - {item}: file_size={file_size} bytes, is_dir={is_dir}\n"
            
    return result



        


