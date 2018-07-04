XENOPS_COURSE_BACKUP_BUCKET = ENV_TOKENS.get('XENOPS_COURSE_BACKUP_BUCKET', '')
XENOPS_COURSE_BACKUP_REGION = 'ap-southeast-2'
XENOPS_COURSE_BACKUP_DIRECTORY = ENV_TOKENS.get('XENOPS_COURSE_BACKUP_DIRECTORY', '')

############# Kenisis backend Stream Name ##########################
XENOPS_TRACKER_KINESIS_STREAM = {
    'kinesis': {
        'stream-name': 'Segment-Stream'
    }
}
