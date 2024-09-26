# -------------------------------------------
# TODO: Add your name, email, & Github
# -------------------------------------------
NAME= 'Frankie Esparza'
SHORT_NAME = 'Frankie'      # short version of your name shows up on mobile devices
EMAIL='fwesparza@gmail.com' # doesn't need to be a gmail account
GITHUB_USERNAME = 'frankie-esparza'
MAX_REPOS_IN_GET_QUERY = 50 # number of repos the Github API will GET, set this to the max number of repos you think you'll have in your Github set to public

# -------------------------------------------
# TODO: Add your LinkedIn public profile url 
# - More details here: https://www.linkedin.com/help/linkedin/answer/a542685/manage-your-public-profile-url?lang=en
# -------------------------------------------
LINKEDIN_USERNAME = 'frankie-willcox-esparza'

# -------------------------------------------------------------------
# TODO: Set how often you want your page to re-GET repos from Github
# -------------------------------------------------------------------
SECONDS_PER_DAY = 60*60*24
FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER = SECONDS_PER_DAY # frequency that repofolio will re-GET repos from Github & database

# -------------------------------------------
# TODO: Set up storage of static files
# -------------------------------------------
# 
# Suggested Method:
# -----------------
# 1. Use the free tier of Google Cloud Storage & make a "bucket" 
# 2. in the bucket, create the following file structure (replacing 'your-google-cloud-bucket' and 'name-of-repo' with the appropriate names)
#
#    your-google-cloud-bucket/
#    ├── documents/
#    │   ├── resume.pdf
#    ├── images/
#    │   ├── profile_pic.png
#    │   ├── favicon.png
#    ├── thumbnails/
#    │   ├── name-of-repo-1.js
#    │   ├── name-of-repo-2.js
#    │   └── name-of-repo-3.js
#    ├── videos/
#    │   ├── name-of-repo-1.js
#    │   ├── name-of-repo-2.js
#    │   └── name-of-repo-3.js
#
# - Here's how to set up a free Google Cloud Storage bucket - https://cloud.google.com/storage/docs/discover-object-storage-console
# - Here's how to make data public - https://cloud.google.com/storage/docs/access-control/making-data-public#:~:text=In%20the%20list%20of%20buckets,The%20Grant%20access%20dialog%20appears.
# 
# 
# Alternate Method: 
# --------------------
# - put all your videos on a YouTube channel and make STATIC_FILES_URL_START the beginning of the YouTube URL for all your videos
# - put the rest of the files (resume, images, thumbnails) in a static folder & use whitenoise (already in the Pipfile) to serve them
# --------------------------------------------------------------------------------------------------------------------------------------
STATIC_FILES_URL_START = f'https://storage.googleapis.com/frankie-esparza-portfolio' # see notes above Google Cloud Storage & other methods

# set the filetypes that all of your static files are saved in 
FILE_TYPE_FOR_DOCUMENTS = '.pdf'
FILE_TYPE_FOR_IMAGES = '.png'
FILE_TYPE_FOR_VIDEOS = '.mp4'

RESUME_FILENAME = f'resume{FILE_TYPE_FOR_DOCUMENTS}' 
PROFILE_PIC_FILENAME = f'profile_pic{FILE_TYPE_FOR_IMAGES}' 
FAVICON_FILENAME = f'favicon{FILE_TYPE_FOR_IMAGES}'

RESUME_URL = f'{STATIC_FILES_URL_START}/documents/{RESUME_FILENAME}'
PROFILE_PIC_URL = f'{STATIC_FILES_URL_START}/images/{PROFILE_PIC_FILENAME}'
FAVICON_URL = f'{STATIC_FILES_URL_START}/images/{FAVICON_FILENAME}'