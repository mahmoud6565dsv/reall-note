from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# from ckeditor.fields import RichTextField
# Create your models here.
class Note (models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    slug    = models.SlugField(null=True,blank=True)
    content = RichTextField()
    crated  = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank=True, max_length=50)
    
    img     = models.ImageField(upload_to='notes-img/', default='', null=True , blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)   
        

    def __str__(self):
        return self.title
    
    
class Comment (models.Model):
    comment = models.TextField(blank=True, max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    noteComment = models.ForeignKey(Note,on_delete=models.CASCADE)
    created  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
    
    
# class Comment(models.Model):
#     post = models.ForeignKey(Note,on_delete=models.CASCADE,related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)