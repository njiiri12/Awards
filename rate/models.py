from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    '''
    Class that defines the project objects
    '''
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    link = models.URLField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pubdate = models.DateTimeField(auto_now_add=True, null = True)
    voters = models.ManyToManyField(User, related_name="votes")
    design_score = models.IntegerField(default=0)
    usability_score = models.IntegerField(default=0)
    content_score = models.IntegerField(default=0)
    average_design = models.FloatField(default=0,)
    average_usability = models.FloatField(default=0)
    average_content = models.FloatField(default=0)
    average_score = models.FloatField(default=0)


    def __str__(self):
        return self.title


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def voters_count(self):
        return self.voters.count()




    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod 
    def search_project(cls,name):
        return Project.objects.filter(title__icontains = name)

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)



class Profile(models.Model):
    '''
    Class that defines the profile objects
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField()
    picture = CloudinaryField('image')
    email = models.EmailField()
    github_link = models.URLField()

    def __str__(self):
        return self.user.username 

@receiver(post_save, sender = User)
def create_profile(sender, instance,created, **kwargs):
     if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile( sender, instance, **kwargs):
    instance.profile.save()
