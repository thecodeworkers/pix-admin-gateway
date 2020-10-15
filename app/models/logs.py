from mongoengine import Document, StringField, ReferenceField, DateTimeField
from datetime import datetime

LOG_TYPE = ('ERROR', 'INFO')

class Logs(Document):
    ip = StringField(required=True)
    log_type = StringField(required=True, choices=LOG_TYPE)
    app = StringField(required=True)
    name = StringField(max_length=300, required=True)
    description = StringField(required=True)
    services = StringField(required=True)
    date = DateTimeField(required=True)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.now()
        return super(Logs, self).save(*args, **kwargs) 
