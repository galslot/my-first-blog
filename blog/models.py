# открывают доступ к коду из других файлов
from django.db import models
from django.utils import timezone

# эта строка определяет нашу модель (объект)
# Post — это имя нашей модели, мы можем поменять его при желании
# Всегда начинай имена классов с прописной буквы.
class Post(models.Model):

    #author = models.ForeignKey('auth.User')
	
	# так мы определяем текстовое поле с ограничением на количество символов.
    title = models.CharField(max_length=200)
	
	# models.TextField — так определяется поле для неограниченно длинного текста. 
	# Выглядит подходящим для содержимого поста
    text = models.TextField()
	
	# models.DateTimeField — дата и время.
    created_date = models.DateTimeField(
            default=timezone.now)
	
	# models.ForeignKey — ссылка на другую модель.		
    published_date = models.DateTimeField(
            blank=True, null=True)
    
	#метод публикации для записи,
	# def Означает, что создаётся функция/метод, а publish — это название этого метода
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
