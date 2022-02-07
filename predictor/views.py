from django.shortcuts import render
import pickle
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

@csrf_exempt
def home(request):
    context={}
    if request.method=='POST':
        temp={}
        temp['GRE']=float(request.POST['GRE'])
        temp['TOEFL']=float(request.POST['TOEFL'])
        temp['CGPA']=float(request.POST['CGPA'])
        temp['SOP']=float(request.POST['SOP'])
        temp['LOR']=float(request.POST.get('LOR'))
        temp['RANKING']=float(request.POST.get('RANKING'))
        model=pickle.load(
            open('E:/user backup/Desktop/CODING/Pred/admit/src/predictor/admissionPrediction/model.sav','rb')
            )
        temp2=temp.copy()
        temp2['GRE Score']=temp['GRE']
        temp2['TOEFL Score']=temp['TOEFL']
        temp2['University Rating']=temp['RANKING']
        temp2.pop('GRE')
        temp2.pop('TOEFL')
        temp2.pop('RANKING')
        print(temp.keys(),temp2.keys())
        data=pd.DataFrame(temp2,index=[0])
        print(data)
        prediction=model.predict(data)[0]
        prediction=prediction*100
        context={'prediction':prediction,'temp':temp}
        print(prediction)
        
    return render(request,'form.html',context)