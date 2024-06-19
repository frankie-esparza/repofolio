# ---------------------------------------------------------------
# TODO: Add Projects that don't have public repos in Github here
# ---------------------------------------------------------------
# Examples: 
# 1) You have a project from working at a company that doesn't share their code publicly, 
#    so you want to describe the project (or link a video) but you don't have a public repo associated with it 
# 2) You're like me & you changed fields/careers, so you have some work that you want to share but it wasn't software & doesn't have a repo
# 3) Maybe you want to split a project into multiple videos, one video has a repo associated with it and the other doesn't
# 
# Instructions: 
# 1) Go to the "models.py" file to familiarize yourself with all of the properties of the 'Repo' class
# 2) Come back here and create objects for all of your "Projects without Repos", note that all of these "Projects without Repos" 
#    will be instances of the "Repo" class since they're going to show up on the website with similar styling as the projects that have repos
PROJECTS_WITHOUT_REPOS = [
     {
        'name': 'plenty-lights',
        'display_name': 'custom led lights',
        'description': '''
            Delivered 2 generations of air & water-cooled LED lights from concept to production that are
            now used in farms that use 90% less water and 1% of the land compared to conventional farms.
        ''',
        'video_filename': 'plenty-lights.mp4',
        'thumbnail_filename': 'plenty-lights.png',
        'priority': 2,
        'highlighted': True,
    },
    {
        'name': 'plenty-heatsinks',
        'display_name': 'cost optimization',
        'description': '''
            Wrote a Matlab model to cost-optimize the design of the heatsinks of air-cooled LED Lights for a novel 
            thermal management system (US Patent 63,007,016).\n 
        ''',
        'topics': [
            'matlab'
        ],
        'video_filename': 'plenty-heatsinks.mp4',
        'thumbnail_filename': 'plenty-heatsinks.png',
        'language': 'matlab',   
        'priority': 3,
        'highlighted': True
    },
    {
        'name': 'neuralink-testing',
        'display_name': 'automated testing',
        'description': '''
            Wrote a Python script to automatically check for manufacturing defects for a brain implant.
        ''',
        'topics': [
            'python',
            'signal-processing'
        ],
        'language': 'python',
        'video_filename': 'neuralink.mp4',
        'thumbnail_filename': 'neuralink.png',
        'priority': 4,
        'highlighted': True

    },
    {
        'name': 'streetcode',
        'display_name': 'streetcode',
        'description': '''
            Designed curriculum and hands-on workshops empowering students to bring their ideas to life 
            using the design process, code, electronics, 3D printing, and CAD modeling
        ''',
        'video_filename': 'streetcode.mp4',
        'thumbnail_filename': 'streetcode.png',
         'priority': 5,
         'highlighted': True
    },
]