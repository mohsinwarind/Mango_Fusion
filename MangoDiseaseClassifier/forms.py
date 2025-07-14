from django import forms

MODEL_CHOICES = [
    ('convnext_tiny', 'ConvNeXt Tiny'),
    ('resnet50', 'ResNet-50'),
    ('efficientnet_b0', 'EfficientNet-B0'),
    ('mobilenetv2_100', 'MobileNetV2'),
]

MODE_CHOICES = [
    ('leaf', 'Leaf Only'),
    ('fruit', 'Fruit Only'),
    ('fusion', 'Fusion'),
]

class ImageUploadForm(forms.Form):
    model_choice = forms.ChoiceField(choices=MODEL_CHOICES, widget=forms.RadioSelect)
    mode = forms.ChoiceField(choices=MODE_CHOICES, widget=forms.RadioSelect)
    leaf_image = forms.ImageField(required=False)
    fruit_image = forms.ImageField(required=False)


from django import forms

class PredictionForm(forms.Form):
    MODEL_CHOICES = [
        ('convnext_tiny', 'ConvNeXt'),
        ('resnet50', 'ResNet-50'),
        ('efficientnet_b0', 'EfficientNet-B0'),
        ('mobilenetv2_100', 'MobileNetV2'),
    ]

    MODE_CHOICES = [
        ('leaf', 'Leaf'),
        ('fruit', 'Fruit'),
        ('fusion', 'Fusion'),
    ]

    model_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=MODEL_CHOICES)
    mode = forms.ChoiceField(widget=forms.RadioSelect, choices=MODE_CHOICES)
    leaf_image = forms.ImageField(required=False)
    fruit_image = forms.ImageField(required=False)
