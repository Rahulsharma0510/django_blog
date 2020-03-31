from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User', on_delete= models.CASCADE) # author is connect to 'auth.User'
    title=models.CharField(max_length=250)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

#eventually there will be  list of comments which some will be appoved
#and some will be not appoved
# so we will be grab and filter the comments who are approved and show them along with Post
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

 #once you have created the instance of class 'Post'
 #after creating the 'post' where should i go, goto 'post_detail' page where the primary key of post just created
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})




#string representation its good idea to have !
    def __str__(self):
        return self.title



class Comment(models.Model):
    post=models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False) #'approved_comment' should be same as 'approved_comment' of 'def approve_comments'

    def approve(self):
        self.approved_comment = True
        self.save()
#comments neds to be approved by superuser
#once the user done typing in the comment, it will go back to list of all post.
    def get_absolute_url(self):
        return reverse("post_list") # 'post_list' will be home page where all the list of blogs
    #string representation
    def __str__(self):
        return self.text
