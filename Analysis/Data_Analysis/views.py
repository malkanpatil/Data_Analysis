from django.shortcuts import render, redirect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from rest_framework.views import APIView
from .forms import UploadFileForm
import os

class UploadFileAPIView(APIView):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'Data_Analysis/upload.html', {'form': form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = request.FILES['file']
                df = pd.read_csv(file)
                request.session['data'] = df.to_dict()
                return redirect('results')
            except pd.errors.EmptyDataError:
                form.add_error(None, 'The uploaded file is empty.')
            except pd.errors.ParserError:
                form.add_error(None, 'Error parsing the file. Ensure it is a valid CSV.')
            except Exception as e:
                form.add_error(None, f'An unexpected error occurred: {e}')
        return render(request, 'Data_Analysis/upload.html', {'form': form})


class ResultsAPIView(APIView):
    def get(self, request):
        data = request.session.get('data')
        if data:
            try:
                df = pd.DataFrame.from_dict(data)
                
                head = df.head().to_html()
                summary_stats = df.describe().to_html()
                
                missing_values = df.isnull().sum().to_dict()
                
                histograms = {}
                for column in df.select_dtypes(include=[np.number]).columns:
                    plt.figure()
                    sns.histplot(df[column].dropna())
                    plt.title(f'Histogram of {column}')
                    plt.savefig(f'static/{column}_histogram.png')
                    plt.close()  
                    histograms[column] = f'{column}_histogram.png'
                
                context = {
                    'head': head,
                    'summary_stats': summary_stats,
                    'missing_values': missing_values,
                    'histograms': histograms,
                }
                return render(request, 'Data_Analysis/results.html', context)
            except Exception as e:
                return render(request, 'Data_Analysis/results.html', {'error': f'An unexpected error occurred: {e}'})
        return redirect('/')
