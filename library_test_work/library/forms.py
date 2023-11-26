from django import forms

from library.models import Book, User


class AddNewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year', 'isbn']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_input'}),
            'author': forms.TextInput(attrs={'class': 'form_input'}),
            'year': forms.TextInput(attrs={'class': 'form_input'}),
            'isbn': forms.TextInput(attrs={'class': 'form_input'}),
        }
        labels = {
            'name': 'Name',
            'author': 'Author',
            'year': 'Year',
            'isbn': 'ISBN',
        }


class AddNewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
