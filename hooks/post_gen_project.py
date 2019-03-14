"""
Does the following:
# 1. Removes the mapideas app-folder if it's not wanted
"""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_mapideas(project_directory):
    # Determine the local_setting_file_location
    location = os.path.join(
        PROJECT_DIRECTORY,
        'apps/mapideas'
    )
    shutil.rmtree(location)

# 1. Removes the mapideas app-folder if it's not wanted
if '{{ cookiecutter.use_maps_and_mapideas }}' != 'y':
    remove_mapideas(PROJECT_DIRECTORY)
