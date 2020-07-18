from django import forms

from .models import Book
from .models import ref


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')


class refForm(forms.ModelForm):
    class Meta:
        model = ref
        fields = ('title', 'author', 'pdf', 'cover')
