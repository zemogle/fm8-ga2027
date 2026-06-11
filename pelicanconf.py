AUTHOR = 'Edward Gomez'
SITESUBTITLE = '17 &amp; 18 August 2027 - IAU GA2027 Focus Meeting 8'
SITENAME = 'AI in Astronomy Education and Outreach: Opportunities and Risks'
SITEURL = 'https://fm8-ga2027.zemogle.net/'
# SITEURL = '/'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = 'themes/bulma_profile/'

# Blogroll
LINKS = (
        ('Home','/'),
        ('Scientific Rationale', '/rationale/'),
         ('Talks', '/talks/'),
         ('Posters', '/posters/'),
         ('SOC','/scientific-organizing-committee/')
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

READERS = {"html": None}

STATIC_PATHS = ['images',]

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True