from template_generator.service import get_config, create_project_folder, create_manifest_file, create_debug_file, \
    create_sync_file


def create():
    config = get_config()
    create_project_folder(config)
    create_manifest_file(config)
    create_debug_file(config)
    create_sync_file(config)


create()
