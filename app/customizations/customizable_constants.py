# ------------------------------------------------------------------
# TODO (OPTIONAL): Set up a Google Cloud Storage Bucket to store:
# - resume
# - videos 
# - thumbnails (for videos)
# - images (favicon & profile pic)
# 
# - Here's how I set up a free Google Cloud Storage bucket - https://cloud.google.com/storage/docs/discover-object-storage-console
# - Here's how to make data public - https://cloud.google.com/storage/docs/access-control/making-data-public#:~:text=In%20the%20list%20of%20buckets,The%20Grant%20access%20dialog%20appears.
# 
# Alternate options:
# - put all your videos on YouTube and use the YouTube URL
# - put the rest of the files (resume, images) in static folder
# --------------------------------------------------------------------
SECONDS_PER_DAY = 60*60*24
FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER = SECONDS_PER_DAY # frequency that repofolio will re-GET repos from Github & database
MAX_REPOS_IN_GET_QUERY = 50 # make this number bigger than total repos you want to get from Github
GOOGLE_CLOUD_STORAGE_BUCKET_NAME = 'frankie-esparza-portfolio'
GOOGLE_CLOUD_STORAGE_URL_START = f'https://storage.googleapis.com/{GOOGLE_CLOUD_STORAGE_BUCKET_NAME}'

# ----------------------------------------------------------------------
# TODO: Edit the constants below
# ----------------------------------------------------------------------
NAME= 'Frankie Esparza'
SHORT_NAME = 'Frankie'
EMAIL='fwesparza@gmail.com'
GITHUB_USERNAME = 'frankie-engineer'
LINKEDIN_USERNAME = 'frankie-willcox-esparza'

RESUME_FILENAME = 'resume.pdf' 
PROFILE_PIC_FILENAME = 'profile_pic.png' 
FAVICON_FILENAME = 'favicon.png'

RESUME_URL = f'{GOOGLE_CLOUD_STORAGE_URL_START}/documents/{RESUME_FILENAME}'
PROFILE_PIC_URL = f'{GOOGLE_CLOUD_STORAGE_URL_START}/images/{PROFILE_PIC_FILENAME}'
FAVICON_URL = f'{GOOGLE_CLOUD_STORAGE_URL_START}/images/{FAVICON_FILENAME}'
