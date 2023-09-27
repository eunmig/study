
#1.  static 파일 기본 설정
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static/assets/'
]

#2.  media 파일 기본 설정
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/uploaded_files/'