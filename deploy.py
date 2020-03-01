import os
import shutil
from subprocess import check_output
import subprocess


def create_folder(folder):
    if folder not in os.listdir():
        os.mkdir(folder)


def install_requirements():
    check_output("pip install -r requirements.txt -t lib/", shell=True)


def delete_dist_info_folders():
    lib = os.listdir("lib")

    folders_to_delete = [x for x in lib if "dist-info" in x]

    for x in folders_to_delete:
        shutil.rmtree("lib/" + x)


def move_dependencies():
    lib = os.listdir("lib")
    library_folders = [x for x in lib if "dist-info" not in x]

    for x in library_folders:
        src = os.getcwd() + "\\lib\\" + x
        dst = os.getcwd() + "\\target"
        shutil.move(src, dst)


def copy_source_files():
    for x in os.listdir("src"):
        if x not in ["__init__.py", "__pycache__", "lambda_function.py"]:
            src = os.getcwd() + "\\src\\" + x
            dst = os.getcwd() + "\\target\\src\\" + x
            shutil.copy(src, dst)

    src = os.getcwd() + "\\src\\lambda_function.py"
    dst = os.getcwd() + "\\target\\lambda_function.py"
    shutil.copy(src, dst)


def remove_dependencies():
    lib = os.listdir("lib")
    library_folders = [x for x in lib if "dist-info" not in x]

    for x in library_folders:
        path = os.getcwd() + "\\" + x
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def create_zip():
    os.chdir("target")
    subprocess.call([
        'C:\\Program Files\\7-Zip\\7z.exe',
        'a',
        '-tzip',
        'code.zip',
        '*.py',
        '*/*.py'
    ])
    os.chdir("..")


def upload_zip_to_aws():
    os.chdir("target")

    check_output(
        "aws lambda update-function-code --profile personal --function-name tfl_status --zip-file fileb://code.zip",
        shell=True)

    os.chdir("..")


def main():
    create_folder("lib")
    create_folder("target")
    create_folder("target/src")
    install_requirements()
    delete_dist_info_folders()
    move_dependencies()
    copy_source_files()
    create_zip()
    upload_zip_to_aws()
    delete_folder("lib")
    delete_folder("target")


if __name__ == '__main__':
    main()
