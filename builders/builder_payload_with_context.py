from builders.info import builder_migration_info
from builders.info import builder_developer_info


def build(context):
    #print("Inside Main Builder")
    ret = {
        "migrationInfo": builder_migration_info.build(context),
        "developerInfo": builder_developer_info.build(context)
    }

    return ret
