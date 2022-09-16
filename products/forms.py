from .models import Rating, Review
from django import forms


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].label = ""


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_text'].label = "Add Your Review"
