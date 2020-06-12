import os, time
import shutil
import datetime



# print(os.path.getmtime(file)
current_path="./"
for file in os.listdir(current_path):
    print(file)
    print(os.path.getmtime(file))
    dirc = os.path.getmtime(file)
    sortByDate = str (datetime.datetime.fromtimestamp(dirc)).split(" ")[0]
    new_dir = sortByDate

    if (not os.path.isdir(new_dir)):
        os.makedirs(new_dir)
    print("Moving File",file)
    shutil.move(file,new_dir)

# click.secho(('Finished moving {} to: {}'.format(file,new_dir)),fg='green')

    