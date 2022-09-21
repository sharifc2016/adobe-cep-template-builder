from os import path


def get_plugin_directory_path(config):
    return path.join("extensions", config["ExtensionBundle"]["Name"])


def get_extension_directory_path(config):
    return path.join(get_plugin_directory_path(config), config["ExtensionBundle"]["Id"])


def get_manifest_file_path(config):
    return path.join(get_extension_directory_path(config), "CSXS", "manifest.xml")


def get_sync_file_path(config):
    return path.join(get_plugin_directory_path(config), "sync.py")


def get_debug_file_path(config):
    return path.join(get_extension_directory_path(config), ".debug")
