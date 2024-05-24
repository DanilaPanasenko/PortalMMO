from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import ModelForm
from myapp.models import Advertisement


class PostForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'headline',
            'text',
            'category',
        ]
        widgets = {
            'text': CKEditorUploadingWidget(),
        }
