from django.utils import timezone
from django.db import models

class NoMillisecDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            # Before
            # value = datetime.date.today()

            # After
            value = timezone.now().replace(microsecond=0)
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

class TimeStampModel(models.Model):
    created_at = NoMillisecDateTimeField(auto_now_add=True)
    updated_at = NoMillisecDateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def is_updated(self):
        """Tips: 추후 obj에서 update 여부 체크를 위함"""
        return self.created_at != self.updated_at