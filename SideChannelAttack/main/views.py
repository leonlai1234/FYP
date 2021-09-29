from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import glob, os, os.path
import datetime

#172.19.0.2

trainfilename_list = []
testfilename_list = []

def index(response):
    return render(response, "home.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def guide(request):
    return render(request, "guide.html")

def tools(request):
    return render(request, "tools.html")

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        #Get form ip address value
        ip = str(request.POST.get('ipadd'))
        #Initialize counter
        i = 0
        x = 0
        total_files = 0

        #Loop through the form FILES list and save the files
        while x < 10:
            for f in request.FILES.getlist('uploadfile' + str(x)):
                if(i % 2 == 0):
                    #Spliting the files into Train folder and save the name of the file into a list
                    trainfilename_list.append('train_pcap_uploadfile' + str(x) + '.' + str(i))
                    fss = FileSystemStorage('TrainData','TrainData')
                    fss.save('train_pcap_uploadfile' + str(x) + '.' + str(i), f)
                    total_files += 1
                else:
                    #Spliting the files into Test folder and save the name of the file into a list
                    testfilename_list.append('test_pcap_uploadfile' + str(x) + '.' + str(i))
                    fss = FileSystemStorage('TestData','TestData')
                    fss.save('test_pcap_uploadfile' + str(x) + '.' + str(i), f)
                    total_files += 1
                i = i + 1
            if (bool(request.FILES.getlist('uploadfile' + str(x))) == False):
                break
            i = 0
            x += 1
            
        dt = datetime.datetime.now()
        dt = dt.strftime("%d/%m/%Y %H:%M:%S")
        
        #In case Wrong IP input, it will show 0% as result
        with open("result.txt", "w") as f:
            f.write("0\n")
            f.write("0\n")
            f.write("0")
    
        with open("main/static/result-view.txt", "w") as fs:
            fs.write("Side Channel Attack Detection Tools\n")
            fs.write("----------------------------------------------------------\n")
            fs.write("Date and Time : " + str(dt) + "\n")
            fs.write("Number of Files Processed : " + str(total_files) + "\n")
            fs.write("IP address : " + str(ip) + "\n")
            fs.write("----------------------------------------------------------\n")
            fs.write("Result of Files Detection Rate\n")
            fs.write("----------------------------------------------------------\n")
            fs.write("Bayesian Classifier Performance\n")
            fs.write("Average True Positive rate : " + "0%\n")
            fs.write("Average False Positive rate : " + "0%\n")
            fs.write("Average Non-detection rate : " + "0%\n\n")
            fs.write("Nearest Neighbour Classifier Performance\n")
            fs.write("Average True Positive rate : " + "0%\n")
            fs.write("Average False Positive rate : " + "0%\n")
            fs.write("Average Non-detection rate : " + "0%\n\n")
            fs.write("Hybrid Classifier Performance\n")
            fs.write("Average True Positive rate : " + "0%\n")
            fs.write("Average False Positive rate : " + "0%\n")
            fs.write("Average Non-detection rate : " + "0%\n")
            fs.write("----------------------------------------------------------\n")

        #Putting list into user's environment
        os.environ['Total_Files'] = str(total_files)
        os.putenv('totalupload',str(x))
        os.putenv('trainfilename_list',' '.join(trainfilename_list))
        os.putenv('testfilename_list',' '.join(testfilename_list))
        os.putenv('ipadd',ip)
        subprocess.run('bash main/tools/populate_objectsdb.sh', shell=True)
        subprocess.run('bash main/tools/train_classifiers.sh', shell=True)
        #subprocess.run('python main/tools/determine_classifier_accuracy.py')
        
        result=""

        p = subprocess.Popen('python main/tools/determine_classifier_accuracy.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        res = p.communicate()
        if p.returncode:
            result = "Error Occured! Check your IP address!"
        
        #Read the result text file and append it into mylist
        with open('result.txt', 'r') as out:
            line = out.readlines()
            mylist = []
            for i in line:
                mylist.append(i)
        
        filelist = glob.glob(os.path.join("TrainData/", "train_pcap_*"))
        for f in filelist:
            os.remove(f)

        filelist = glob.glob(os.path.join("TestData/", "test_pcap_*"))
        for f in filelist:
            os.remove(f)

        filelist = glob.glob(os.path.join("", "*.json"))
        for f in filelist:
            os.remove(f)
    # return render(request, 'result.html',{})   
    return render(request, 'tools.html',{'data1':mylist[0],'data2':total_files,'data3':result})
