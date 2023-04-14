from django.db import models

class Post(models.Model):
    '''Information about post'''
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Text')
    author = models.CharField('author name', max_length=100)
    date = models.DateField('date of publication')
    img = models.ImageField('image', upload_to='images/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
