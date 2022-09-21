import json
import os
import shutil

from template_generator.dirs import get_manifest_file_path, get_plugin_directory_path, get_extension_directory_path, \
    get_sync_file_path, get_debug_file_path
from template_generator.generators import manifest_generator, debug_generator, sync_generator


def get_config():
    f = open('config.json')
    return json.load(f)


def create_manifest_file(config):
    file = open(get_manifest_file_path(config), "w")
    file.write(manifest_generator.generate(config))
    file.close()
    pass


def create_debug_file(config):
    file = open(get_debug_file_path(config), "w")
    file.write(debug_generator.generate(config))
    file.close()
    pass


def create_sync_file(config):
    file = open(get_sync_file_path(config), "w")
    file.write(sync_generator.generate(config))
    file.close()
    pass


def create_project_folder(config):
    remove_directory_with_files(get_plugin_directory_path(config))
    shutil.copytree("helper_items", get_plugin_directory_path(config))
    shutil.copytree("plugin", get_extension_directory_path(config))


def remove_directory_with_files(directory):
    if directory in os.listdir():
        shutil.rmtree(directory)
