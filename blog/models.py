from django.conf import settings
from django.db import models
from django.utils import timezone

# class ModelName (models.Model):
# class: Indicates that we are defining an object.
# ModelName: The name of model, start with uppercase letter.s
# models.Model: Lets Django know that this model will be saved to DB.

class Post(models.Model): # Create a method called Post.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey(link): Links to another model.
    title = models.CharField(max_length=200)
    # models.CharField (length): Define text with limited number of characters.
    text = models.TextField()
    # models.TextField(): Define long text without character limit.
    created_date = models.DateTimeField(default=timezone.now)
    # models.DateTimeField(): Date and time format.
    published_date = models.DateTimeField(blank=True, null=True)

    # Define publish function with self parameter.
    def publish(self):
        # self parameters publish data will be current time in given timezone.
        self.published_date = timezone.now()
        self.save()

    # Define __str__ function with self parameter.
    def __str__(self):
        # __str__ function return title of the post.
        return self.title