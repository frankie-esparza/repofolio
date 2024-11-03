from app.customizations.settings import (
    LINKEDIN_USERNAME, 
    GITHUB_USERNAME, 
    RESUME_URL, 
    EMAIL
)

PAGES = { 
    'Home': '/',
    'Highlights' : '/highlights',
    'More' : '/more',
}

RESUME_BUTTON_NAME = 'Download Resume'
EMAIL_ME_URL = f'https://mail.google.com/mail/u/0/?fs=1&to={EMAIL}&tf=cm'

HEADER_ICON_BUTTONS = [
    {
        'name': 'Github',
        'url': f'https://github.com/{GITHUB_USERNAME}',
        'icon': 'fa-brands fa-github'
    },
    {
        'name': 'LinkedIn',
        'url': f'https://www.linkedin.com/in/{LINKEDIN_USERNAME}/',
        'icon': 'fa-brands fa-linkedin'
    },
    {
        'name': f'{RESUME_BUTTON_NAME}',
        'url': RESUME_URL,
        'icon': 'fa-regular fa-file'
    },
    {
        'name': 'Email Me',
        'url': EMAIL_ME_URL,
        'icon': 'fa fa-envelope'
    }
]