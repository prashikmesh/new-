from django.core import validators
from django.forms import ModelForm
from .models import Post, Positions

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['id','title','description','body']

class PositionForm(ModelForm):
    class Meta:
        model = Positions
        fields = ['id','position','description','status']