REPOS_IN_PRIORITY_ORDER_WITH_HIGHLIGHT = {
    'fullscript': {'highlighted': True},
    'thyme': {'highlighted': True},
    'plenty-lights': {'highlighted': True},
    'plenty-heatsinks': {'highlighted': True},
    'neuralink': {'highlighted': True},
    'streetcode': {'highlighted': True},
    'kanban': {'highlighted': True},
    'thyme-resource-guide': {'highlighted': True},
    'thyme-architecture': {'highlighted': True},
    'thyme-database': {'highlighted': True},
    'ube': {},
    'yuca': {},
    'repofolio': {},
    'crayons': {},
    'tropical': {},
    'pokemon': {},
    'museum': {},
    'palm': {},
    'island-finder': {},
    'binary-search-tree': {},
    'friends': {},
    'authenticate': {},
    'data-structs-and-algos': {},
}

def add_priority_prop(repos):
    result = {}
    for index, repo in enumerate(repos):
        result[repo] = {
            **repos[repo],
            'priority': index 
        }
    return result

REPOS_WITH_PRIORITY_OR_HIGHLIGHT = add_priority_prop(REPOS_IN_PRIORITY_ORDER_WITH_HIGHLIGHT)
