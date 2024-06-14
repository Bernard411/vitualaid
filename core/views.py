from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageData
from PIL import Image
import pytesseract

def homepage(request):

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            img_obj = Image.open(img)  
            img_obj = img_obj.convert('L')
            text = pytesseract.image_to_string(img_obj)
            imagedata = ImageData(image=img) 
            imagedata.save() 
            return render(request, 'index.html', {'text': text, 'image': imagedata})
    else:
        form = ImageUploadForm()
 
    imagedata= ImageData.objects.all()
    context = {'form': form, 'imagedata': imagedata}
    return render(request, 'index.html', context)

def output_text(request):


    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            img_obj = Image.open(img)  
            img_obj = img_obj.convert('L')
            text = pytesseract.image_to_string(img_obj)
            imagedata = ImageData(image=img) 
            imagedata.save() 
            return render(request, 'index.html', {'text': text, 'image': imagedata})
    else:
        form = ImageUploadForm()
 
    imagedata= ImageData.objects.all()
    context = {'form': form, 'imagedata': imagedata}
    return render(request, 'output.html', context)


def voice_asistance(request):
    return render(request, 'computer_v.html')