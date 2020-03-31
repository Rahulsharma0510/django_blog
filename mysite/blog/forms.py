from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('author','title','text')

#widgets is use for css styling widgets is use to connect with css
        widgets= {
              'title':forms.TextInput(attrs={'class':'textinputclass'}), #class is having a css styel
              'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','text')

        widgets= {
             'author':forms.TextInput(attrs={'class':'textinputclass'}), #class is having a css styel
             'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
