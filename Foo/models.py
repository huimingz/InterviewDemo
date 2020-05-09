from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Course(models.Model):
    COURSE_TYPES = (
        (1, "兴趣单课"),
        (2, "体系单课"),
        (3, "兴趣专辑课"),
        (4, "体系专辑课")
    )

    title = models.CharField(verbose_name="标题", max_length=255)
    type = models.SmallIntegerField(verbose_name="类型", choices=COURSE_TYPES, default=1)
    basic_introduce = models.CharField(verbose_name="说明", max_length=255)
    detail = models.TextField(verbose_name="详细")
    first_price = models.DecimalField(verbose_name="原价", decimal_places=2, max_digits=12)
    real_price = models.DecimalField(verbose_name="现价", decimal_places=2, max_digits=12)
    pic = models.ImageField(verbose_name="图片", upload_to="img/%Y/%m/")
    thumbnail = models.ImageField(verbose_name="缩略图", upload_to="img/%Y/%m/")
    url = models.URLField(verbose_name="URL", max_length=255)
    fake_people = models.PositiveIntegerField(verbose_name="fake people", default=0)
    has_free_chapter = models.BooleanField(verbose_name="有免费章节", default=True)
    share = models.CharField(verbose_name="分享", max_length=100)
    recomment_times = models.IntegerField(verbose_name="推荐次数", default=0)
    recomment_look_times = models.IntegerField(verbose_name="推荐浏览次数", default=0)
    course_index = models.IntegerField(verbose_name="专辑排序")

    category = models.ForeignKey(to="Category", to_field="id", on_delete=models.SET_NULL, null=True)
    parent_course = models.ForeignKey(to="Course", to_field="id", blank=True, null=True, on_delete=models.CASCADE)
    gift_category = models.ForeignKey(to="GiftCategory", to_field="id", on_delete=models.SET_NULL, null=True)

    is_coding = models.BooleanField(verbose_name="is coding", default=True)
    is_active = models.BooleanField(verbose_name="有效性", default=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程"
        constraints = [
            # 约束价格，防止价格为负
            # 提示：这里的受条件约束的字段名必须为数据库表名
            models.CheckConstraint(check=models.Q(first_price__gte='0'), name="course_first_price_non_negative"),
            models.CheckConstraint(check=models.Q(real_price__gte='0'), name="course_real_price_non_negative"),
        ]

    @property
    def mobile_url(self):
        return reverse('course', kwargs={"id": self.id})

    @property
    def type_name(self):
        try:
            _, name = self.COURSE_TYPES[self.type - 1]
            return name
        except IndexError:
            return ""

    def __str__(self):
        print(self.__dict__)
        return f"<Course {self.title}>"


class Category(models.Model):
    """类别表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=255, unique=True)
    desc = models.CharField(verbose_name="描述", max_length=255)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"

    def __str__(self):
        return f"<Category {self.name}>"


class GiftCategory(models.Model):
    """礼物套装表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=255, unique=True)
    desc = models.CharField(verbose_name="描述", max_length=255)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "礼物套装"
        verbose_name_plural = "礼物套装"

    def __str__(self):
        return f"<GiftCategory {self.name}>"


class Chapter(models.Model):
    """章节表"""
    CHAPTER_TYPES = (
        (1, "单词"),
        (2, "句型"),
        (3, "测试"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=255)
    url = models.URLField(verbose_name="URL", max_length=255)
    type = models.SmallIntegerField(verbose_name="类型", name="chapter_type", choices=CHAPTER_TYPES, default=1)
    study_words = models.CharField(verbose_name="学习内容", max_length=255)
    study_audio = models.BinaryField(verbose_name="音频")
    unit = models.ForeignKey(to="Unit", to_field="id", on_delete=models.CASCADE)

    is_try = models.BooleanField(verbose_name="体验章节", default=False)
    is_active = models.BooleanField(verbose_name="有效性", default=True)

    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = "章节"

    @property
    def type_name(self):
        try:
            _, name = self.CHAPTER_TYPES[self.type-1]
            return name
        except IndexError:
            return ""

    def __str__(self):
        return f"<Chapter {self.name}>"


class Unit(models.Model):
    """单元表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=255)
    planning_des = models.TextField(verbose_name="学习计划描述", name="planning_des")
    course = models.ForeignKey(to="Course", to_field="id", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(verbose_name="有效性", default=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "单元"
        verbose_name_plural = "单元"

    def __str__(self):
        return f"<Unit {self.name}>"
