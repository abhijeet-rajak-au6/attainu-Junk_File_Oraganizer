import click
import os
import fnmatch
import shutil
# import re
import datetime
from pathlib import Path
# File Sorting and Organization


def organize_files_by_keyword(keyword, current_path):
    for file in os.listdir(current_path):
        # Matches the file containing the required substring
        if fnmatch.fnmatch(file, '*' + keyword + '*'):
            # print("Found:", file, os.path.isfile(file))
            if not os.path.isdir(current_path + keyword):
                os.makedirs(current_path + keyword)
            print("Moving File:", file)
            shutil.move(current_path + file, current_path + keyword + "/")


@click.group()
@click.version_option(version='0.02', prog_name='file_organizer')
def main():
    """ File Organizer is a simple tool to organize and sort files into folders

    1) eg. file_organizer.py organize [Path] -- keyword Date

    2) eg. file_organizer.py organize [Path] -- keyword Size

    3) eg. file_organizer.py organize_by_ext [Path] -- keyword Date
    """
    pass


@main.command()
@click.argument('current_path', default='./')
@click.option(
    '--keyword',
    '-k',
    help="Specify Keyword to Search Default is Date",
    default='Date')
def organize(current_path, keyword):
    # print("Hello World")
    """ Organize Files and Sort Them Into Folders By Keyword

        eg. python3 file_organizer organize [Path] --keyword Date

        eg. python3 file_organizer.py organize [Path] --keyword Size

        eg. python3 file_organizer.py organize [default Path]

    """
    """ Sorting by date """
    if (keyword == "Date"):
        # print("date",current_path)
        for file in os.listdir(current_path):
            # print(current_path + file)
            # print(os.path.getmtime(current_path + file))
            dirc = os.path.getmtime(current_path + file)
            sortByDate = str(
                datetime.datetime.fromtimestamp(dirc)).split(" ")[0]
            new_dir = current_path + sortByDate
            # print("new_dir",new_dir)

            if (not os.path.isdir(new_dir)):
                os.makedirs(new_dir)
            # print("Moving File",file)
            shutil.move(current_path + file, new_dir)
        click.secho(
            ('Finished Organizing by date:{}'.format(keyword)), fg='green')
    elif (keyword == "Size"):
        for file in os.listdir(current_path):
            # print(current_path+file)
            statInfo = os.stat(current_path + file)

            if (statInfo.st_size >= 0 and statInfo.st_size <= 10):
                # print(statInfo.st_size)
                if (not os.path.isdir(current_path + "SMALL")):
                    os.makedirs(current_path + "SMALL")
                print("Moving File", file)
                shutil.move(current_path + file, current_path + "/SMALL")

            elif (statInfo.st_size >= 10 and statInfo.st_size <= 100):
                if (not os.path.isdir(current_path + "MEDIUM")):
                    os.makedirs(current_path + "MEDIUM")
                print("Moving File", file)
                shutil.move(current_path + file, current_path + "/MEDIUM")

            elif (statInfo.st_size >= 100 and statInfo.st_size <= 1000):
                if (not os.path.isdir(current_path + "LARGE")):
                    os.makedirs(current_path + "LARGE")
                print("Moving File", file)
                shutil.move(current_path + file, current_path + "/LARGE")

            elif (statInfo.st_size >= 1001 and statInfo.st_size <= 16000):
                if (not os.path.isdir(current_path + "HUGE")):
                    os.makedirs(current_path + "HUGE")
                print("Moving File", file)
                shutil.move(current_path + file, current_path + "/HUGE")

            elif (statInfo.st_size >= 16000):
                if (not os.path.isdir(current_path + "GIGANTIC")):
                    os.makedirs(current_path + "GIGANTIC")
                print("Moving File", file)
                shutil.move(current_path + file, current_path + "/GIGANTIC")

        click.secho(
            ('Finished Organizing by date:{}'.format(keyword)), fg='green')
    else:
        organize_files_by_keyword(keyword, current_path)


@main.command()
@click.argument('current_path', default='./')
@click.option(
    '--extension', '-e', help="Specify Extension to Sort By: Default is .txt")
def organize_by_ext(current_path, extension):
    # print("Hello World")
    """ Organize Files and Sort Them Into Folders By Extension

        eg. python3 junk_file_organizer organize-by-ext [Default Path]

        eg. python3 junk_file_organizer organize-by-ext [Path] --extension txt

        eg. python3 junk_file_organizer organize-by-ext  [Path] --extension
        .csv

    """
    # print("extension=",extension)
    # print("current Path=",current_path)
    # print(os.listdir(current_path))

    folder_dict = {
        "HTML": [".html5", ".html", ".htm", ".xhtml"],
        "IMAGES": [
            ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
            ".heif", ".psd"
        ],
        "VIDEOS": [
            ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
            ".qt", ".mpg", ".mpeg", ".3gp"
        ],
        "DOCUMENTS": [
            ".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
            ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg",
            ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"
        ],
        "ARCHIVES": [
            ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg",
            ".rar", ".xar", ".zip"
        ],
        "AUDIO": [
            ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
            ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
        ],
        "PLAINTEXT": [".txt", ".in", ".out"],
        "PDF": [".pdf"],
        "PYTHON": [".py"],
        "XML": [".xml"],
        "EXE": [".exe"],
        "SHELL": [".sh"],
        "YAML": [".yaml"]
    }
    # print('extension=',extension)

    if extension is None:
        # print("Ima here")
        FILE_FORMATS = {
            file_format: directory
            for directory, file_formats in folder_dict.items()
            for file_format in file_formats
        }

        # print("FILE FORMAT = ",FILE_FORMATS)
        for entry in os.scandir(path=current_path):

            if entry.is_dir():
                continue

            file_path = Path(entry)
            # print("file path=",file_path)
            file_format = file_path.suffix.lower()
            # print("file format =",file_format)
            if file_format in FILE_FORMATS:
                # print("file_format",file_format)
                directory_path = Path(current_path + FILE_FORMATS[file_format])
                # print("directory path=",directory_path)
                directory_path.mkdir(exist_ok=True)
                if (current_path == '.'):
                    file_path.rename(directory_path.joinpath(file_path))
                else:
                    file_path.rename(directory_path.joinpath(entry.name))
                # print("rename file path =",file_path)

            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except Exception:
                    None
        click.secho(
            ('Finished Moving to their respective  folder Path: {}'.format(
                directory_path)),
            fg='green')

    else:
        for file in os.listdir(current_path):
            ext = extension
            new_dir = ""
            if fnmatch.fnmatch(file, '*' + ext):
                click.secho(('Found File:{}'.format(file)), fg='blue')
                # If the file is truly a file...
                # print(file)
                if os.path.isfile:
                    try:
                        # print("ty")
                        # Make a directory with the extension name...
                        if (current_path == '.'):
                            new_dir = ext.strip(".").upper()
                        else:
                            new_dir = current_path + ext.strip(".").upper()
                        # print("newdir=",new_dir)
                        os.makedirs(new_dir)
                    except Exception:
                        None
                # Copy that file to the directory with that extension name
                print(current_path + new_dir)
                if current_path == '.':
                    shutil.move(file, new_dir)
                else:
                    shutil.move(current_path + file, new_dir)
                print("helo")
        click.secho(
            ('Finished Moving{}to:{}folder'.format(file, new_dir)), fg='green')


if __name__ == '__main__':
    main()
