ADDED_PROPS_FOR_EXISTING_REPOS = {
    'thyme': {
        'priority': 1,
        'highlighted': True
    },
    'kanban': {
        'priority': 6,
        'highlighted': True
    },
    'ube': {
        'priority': 7,
        'highlighted': False
    },
    'yuca': {
        'priority': 8,
        'highlighted': False
    },
     'repofolio': {
        'priority': 9,
        'highlighted': False
    },
     'crayons': {
        'priority': 10,
        'highlighted': False
    },
       'tropical': {
        'priority': 11,
        'highlighted': False
    }
}


def get_video_filename_from_repo_name(name):
    return f'{name}.mp4'


def get_thumbnail_filename_from_repo_name(name):
    return f'{name}.png'
