from django.shortcuts import render


def main_view(request):
    data={
        'Object': { 'Temperature': -12, 'Gyro': -22, 'Current': 124, 'Battery': 335 },
        # 'Object1': { 'Temperature': -11, 'Gyro': -2, 'Current': 34, 'Battery': 535 },
        # 'Object2': { 'Temperature': -1, 'Gyro': -20, 'Current': 54, 'Battery': 435 },
        # 'Object3': { 'Temperature': -121, 'Gyro': -22, 'Current': 24, 'Battery': 135 },
    }
    
    context={'data':data,'tableheader':['Temperature','Gyro','Current','Battery']}
    return render(request, 'dash/Dashboard.html', context)


# 'temperature':{'name':'Temperature','values':45},
#         'current':{'name':'Current','values':50},
#         'Gyro':{'name':'Gyro','values':90},
#         'battery':{'name':'Battery','values':87},