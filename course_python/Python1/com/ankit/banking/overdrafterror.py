class Over_draft_error(Exception):
    def __init__(self, message=''):
        super().__init__(message)