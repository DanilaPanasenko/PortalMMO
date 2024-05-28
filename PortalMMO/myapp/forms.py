from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import ModelForm
from myapp.models import Advertisement, Responses


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


class ResponseForm(ModelForm):


    class Meta:
        model = Responses
        fields = [
            'text',
        ]
