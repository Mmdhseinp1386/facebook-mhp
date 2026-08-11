from django.db import models

# Create your models here.

class CountryChoices(models.TextChoices):
    IRAN = ('iran','ایران')
    FRANCE = ('france','فرانسه')

class User(models.Model):
    username =  models.CharField(max_length=50, verbose_name='نام کاربری')
    password = models.CharField(max_length=20, verbose_name = 'رمز عبور')
    name = models.CharField(max_length=50, verbose_name='نام')
    birthdate = models.DateField(null=True, verbose_name='روز تولد')
    email = models.EmailField(verbose_name='ایمیل')
    country = models.CharField(max_length=20, choices=CountryChoices.choices, default=CountryChoices.IRAN, verbose_name='کشور')
    phone = models.CharField(max_length=11, verbose_name='تلفن همراه')
    height = models.PositiveSmallIntegerField(null=True, verbose_name='قد')
    income = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='درآمد')

    def __str__(self):
        return f'{self.username}: {self.email}'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست')
    body = models.CharField(max_length=1024, verbose_name='توضیحات  ')

    def __str__(self):
        return f'{self.user.username}: {self.body}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'