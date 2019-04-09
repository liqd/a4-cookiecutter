"""
Does the following:
# 1. Removes the mapideas app-folder if it's not wanted
# 2. Removes the polls templates if polls are not wanted
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
    test_location = os.path.join(
        PROJECT_DIRECTORY,
        'tests/mapideas'
    )
    shutil.rmtree(test_location)

def remove_polls(project_directory):
    location = os.path.join(
        PROJECT_DIRECTORY,
        '{{ cookiecutter.project_slug }}/templates/a4polls'
    )
    shutil.rmtree(location)

def remove_documents(project_directory):
    location = os.path.join(
        PROJECT_DIRECTORY,
        'apps/documents'
    )
    shutil.rmtree(location)

# 1. Removes the mapideas app-folder if it's not wanted
if '{{ cookiecutter.add_maps_and_mapideas_app }}' != 'y':
    remove_mapideas(PROJECT_DIRECTORY)
# 2. Removes the polls templates if polls are not wanted
if '{{ cookiecutter.add_polls_app }}' != 'y':
    remove_polls(PROJECT_DIRECTORY)
# 3. Removes the documents templates if documents are not wanted
if '{{ cookiecutter.add_documents_app }}' != 'y':
    remove_documents(PROJECT_DIRECTORY)
