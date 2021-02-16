from django import forms


class PostForm(forms.Form):
    image = forms.ImageField(label='イメージ画像', required=False)
    title = forms.CharField(max_length=50, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())