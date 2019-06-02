# update a map while creating backup information
def map_update(current_map, update_info, delete_key):
    assert(type(current_map) is dict)
    assert(type(update_info) is dict)
    assert(type(delete_key) is list or type(delete_key) is dict)

    if delete_key is None:
        delete_key = list()

    restore_update = dict()
    restore_delete = list()
    for key in update_info.keys():
        if key in current_map:
            if type(current_map[key]) == dict:
                # TODO update to the proper way to delete keys
                restore_update[key] = map_update(current_map[key], update_info[key], [])
            else:
                restore_update[key] = current_map[key]
                current_map[key] = update_info[key]
        else:
            restore_delete.append(key)
            current_map[key] = update_info[key]

    for key in delete_key:
        if key in current_map:
            restore_update[key] = current_map[key]
            del current_map[key]

    return restore_update, restore_delete


# restore a map using backup information
def map_restore(current_map, restore_info):
    update, delete = restore_info
    for key in update:

        if type(current_map[key]) is dict:
            map_restore(current_map[key], update[key])
        else:
            current_map[key] = update[key]

    for key in delete:
        del current_map[key]


