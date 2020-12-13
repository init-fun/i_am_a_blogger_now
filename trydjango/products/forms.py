from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter product title"})
    )
    email = forms.EmailField()

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your description",
                "class": "new-class-name two",
                "rows": 5,
                "cols": 15,
            }
        ),
    )
    price = forms.DecimalField(initial=9.99)
    featured = False

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "featured",
            "email",
        ]  # fields to render in the form

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if title[0] != "P":
            raise forms.ValidationError("Product name should start with P")
        if not "news" in title:
            raise forms.ValidationError("news is not in title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not "@" in email:
            raise forms.ValidationError("no domain")
        if not ".com" in email:
            raise forms.ValidationError("not a .com")
        return email


# this is where we are creating our own custom field

# class RawProductForm(forms.Form):
#     title = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Enter product title"})
#     )
# description = forms.CharField(
#     required=False,
#     widget=forms.Textarea(
#         attrs={"class": "new-class-name two", "rows": 5, "cols": 15}
#     ),
# )
# price = forms.DecimalField()
#     featured = False
