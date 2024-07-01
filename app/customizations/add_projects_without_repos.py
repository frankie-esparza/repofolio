# ---------------------------------------------------------------
# TODO: Add Projects that don't have public repos in Github here
# ---------------------------------------------------------------
# Use cases: (1) non-disclosable code, (2) career change / non-software work from a past life, 
# (3) you want to split a project into multiple videos
# 
# Instructions: 
# 1) Go to the "models.py" file to familiarize yourself with all of the properties of the 'Repo' class
# 2) Come back here and create an instance of the "Repo" class for all of your "Projects without Repos"

PROJECTS_WITHOUT_REPOS = [
     {
        'name': 'plenty-lights',
        'display_name': 'custom led lights',
        'description': '''
            Delivered 2 generations of air & water-cooled LED lights from concept to production that are
            now used in farms that use 90% less water and 1% of the land compared to conventional farms.
        ''',
    },
    {
        'name': 'plenty-heatsinks',
        'display_name': 'cost optimization',
        'description': '''
            Developed a model to optimize lighting design for cost and efficiency, guiding architecture
            changes that led to a 60% reduction in production and operational costs\n 
        ''',
        'topics': ['matlab'],
        'language': 'matlab',   
    },
    {
        'name': 'neuralink',
        'display_name': 'automated testing',
        'description': '''
            Built software & hardware for an automated test of a critical safety feature of the implant
        ''',
        'topics': ['python', 'signal-processing'],
        'language': 'python',
    },
    {
        'name': 'streetcode',
        'display_name': 'streetcode',
        'description': '''
            Designed curriculum and hands-on workshops empowering students to bring their ideas
            to life using the design process, code, electronics, 3D printing, and CAD modeling
        ''',
    },
     {
        'name': 'resource-guide',
        'display_name': 'Resource Guide',
        'description': '''
            A resource guide for building a web app with an LLM & Google Workspace APIs
            plus lessons that I learned from building Thyme.
        ''',
    },
]