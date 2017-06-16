from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #标题
    title = models.CharField(max_length= 255)

    #用于URLs, 该标签只包含字母，数字，下划线或连接线, 用于构建友好URL.
    slug = models.SlugField(max_length = 255, unique_for_date='publish')

    #外键，关联到Django权限系统的User模型，多对一，多篇博文对一个作者.
    author = models.ForeignKey(User,related_name= 'blog_post')
    #博文主体.
    body = models.TextField()
    #发布日期;
    publish = models.DateTimeField(default= timezone.now)
    #创建日期;
    created = models.DateTimeField(auto_now_add=True)
    #更新日期;
    updated = models.DateTimeField(auto_now = True)
    #帖子展示状态;
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    #元数据类，告诉Django查询数据库的时候默认返回的是根据publish字段进行降序排列过的结果。我们使用负号来指定进行降序排列。
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title