# coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WeixinUser(models.Model):

    '''WeixinUser profile'''

    auth_user = models.OneToOneField(User, blank=True)  # 拓展用户
    nickname = models.CharField(max_length=30, blank=True, verbose_name=u'昵称')
    nickname2 = models.CharField(max_length=30, blank=True, verbose_name=u'昵称2')
    openid = models.CharField(
        max_length=40, unique=True, verbose_name=u'OpenID')
    tel = models.CharField(max_length=40, blank=True, verbose_name=u"电话")

    def __unicode__(self):
        return u"%s %s" % (self.id, self.openid)


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = WeixinUser()
        profile.user = instance
        profile.save()


def create_weiuser(openid, password):
    user = User()
    user.set_password(password)
    user.username = 'UnNamedUser'
    user.save()

    profile = WeixinUser()
    profile.auth_user = user
    profile.openid = openid
    profile.save()
