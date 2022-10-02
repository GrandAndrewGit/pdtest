from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileManager(BaseUserManager):
    def create_user(self, first_name, last_name, password):
        if not first_name:
            raise ValueError('Users must have first name')
        elif not last_name:
            raise ValueError('Users must have last name')

        user = self.model(
            first_name = first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    first_name = models.CharField(
        verbose_name='first name',
        max_length=30,
        unique=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=30,
        unique=False,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=60,
        unique=False,
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='date of birth')
    contacts = models.CharField(max_length=255, blank=True, null=True, verbose_name='contacts')
    biography = models.TextField(blank=True, null=True, verbose_name='biography')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['last_name']

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.username = self.first_name + ' ' + self.last_name
        super(Profile, self).save(*args, **kwargs) 

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Note(models.Model):
    model_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='model name')
    model_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='model id')
    action_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name


# need to connect this signal to all models
@receiver(post_save, sender=Profile)
def create_note(sender, instance, **kwargs):
    print(sender.__name__)
    print(instance.first_name)
    Note.objects.create(model_name=sender.__name__, model_id=instance.id)
