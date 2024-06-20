# -----------------------------------------------------
# TODO (OPTIONAL): Set up storage of your static files
# -----------------------------------------------------
# Suggested Method:
# -----------------
# Use the free tier of Google Cloud Storage & make a "bucket" 
# in the bucket, add folders for each type of file ( /videos, /images, /thumbnails, /documents )
# upload your files to the bucket 
# - Here's how to set up a free Google Cloud Storage bucket - https://cloud.google.com/storage/docs/discover-object-storage-console
# - Here's how to make data public - https://cloud.google.com/storage/docs/access-control/making-data-public#:~:text=In%20the%20list%20of%20buckets,The%20Grant%20access%20dialog%20appears.
# 
# Other Methods: 
# -----------------
# - put all your videos on YouTube and use the YouTube URL
# - put the rest of the files (resume, images, thumbnails) in a static folder
# --------------------------------------------------------------------
SECONDS_PER_DAY = 60*60*24
FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER = SECONDS_PER_DAY # frequency that repofolio will re-GET repos from Github & database
MAX_REPOS_IN_GET_QUERY = 50 # number of repos the Github API will GET, set this to the max number of repos you think you'll have in your Github set to public
STATIC_FILES_URL_START = f'https://storage.googleapis.com/frankie-esparza-portfolio' # see notes above Google Cloud Storage & other methods

# -----------------------------------------------------
# TODO: Add your name, email, & Github
# -----------------------------------------------------
NAME= 'Frankie Esparza'
SHORT_NAME = 'Frankie'      # short version of your name shows up on mobile devices
EMAIL='fwesparza@gmail.com' # doesn't need to be a gmail account
GITHUB_USERNAME = 'frankie-engineer'

# -----------------------------------------------------
# TODO: Add your LinkedIn public profile url 
# - More details: https://www.linkedin.com/help/linkedin/answer/a542685/manage-your-public-profile-url?lang=en
# -----------------------------------------------------
LINKEDIN_USERNAME = 'frankie-willcox-esparza'

# -----------------------------------------------------
# TODO: Add your resume, profile pic, & favicon
# -----------------------------------------------------
RESUME_FILENAME = 'resume.pdf' 
PROFILE_PIC_FILENAME = 'profile_pic.png' 
FAVICON_FILENAME = 'favicon.png'

RESUME_URL = f'{STATIC_FILES_URL_START}/documents/{RESUME_FILENAME}'
PROFILE_PIC_URL = f'{STATIC_FILES_URL_START}/images/{PROFILE_PIC_FILENAME}'
FAVICON_URL = f'{STATIC_FILES_URL_START}/images/{FAVICON_FILENAME}'
