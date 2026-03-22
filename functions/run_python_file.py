import os
import subprocess


def run_python_file(working_directory, file_path, args=None):

    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(abs_file_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'


        if file_path.split(".")[-1] != "py":
            return f'Error: "{file_path}" is not a Python file'
        

        command = ["python", abs_file_path]
        if args != None:
            command.extend(args)

        completedProcess = subprocess.run(command,timeout=30,capture_output=True,text=True)

        output = ""
        if completedProcess.returncode != 0:
            output += f"Process exited with code {completedProcess.returncode}"
        if completedProcess.stdout == None and completedProcess.stderr == None:
            output += f"No output produced"
        else:
            output += f"STDOUT: {completedProcess.stdout}\nSTDERR: {completedProcess.stderr}"

        return output


    except Exception as e:
        return f"Error when attempting to execute file {file_path}: {e}"
    

