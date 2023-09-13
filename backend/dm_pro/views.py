import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CSVFile
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from .models import CSVFile
from .serializers import CSVFileSerializer
import pandas as pd
from scipy.stats import chi2_contingency
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.tree import export_text
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
from django.http import FileResponse
import uuid
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score



class CSVFileUploadView(APIView):
    parser_classes = ( MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = CSVFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def home(request):
    return HttpResponse("Hello homepage")


def assignment1(request):
    node=CSVFile.objects.all()
    print(node[0].name)

    if len(node)==0 :
        return HttpResponse("No csv file in database !!")
    


    data = pd.read_csv(node[0].file)
    mean_data=data.mean()
    median_data = data.median()
    mode_data = data.mode().iloc[0]  
    var_data = data.var()
    sd_data = data.std()


    print("mean",mean_data[0])
    print("median",median_data[0])
    print("mode",mode_data[0])
    print("variance",var_data[0])
    print("standard deviation",sd_data[0])
    

    my_data={
        "name":node[0].name,
        "mean":mean_data.to_dict(),
        "median":median_data.to_dict(),
        "mode":mode_data.to_dict(),
        "variance":var_data.to_dict(),
        "std":sd_data.to_dict()
    }
    return JsonResponse(my_data)



def assignment2(request):
    node=CSVFile.objects.all()
    print(node[0].name)

    if len(node)==0 :
        return HttpResponse("No csv file in database !!")
    

    Attr1="sepal.length"
    Attr2="sepal.width"

    print("boundary 1")

    data = pd.read_csv(node[0].file)
    df = pd.DataFrame(data)
    contingency_table = pd.crosstab(df[Attr1], df[Attr2])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    alpha=0.7  # we have set that.....
    fl=0

    if p <= alpha:
        print(f"The p-value ({p}) is less than or equal to the significance level ({alpha}).")
        print("The selected attributes are correlated.")
        fl=1
    else:
        print(f"The p-value ({p}) is greater than the significance level ({alpha}).")
        print("The selected attributes are not correlated.")
        fl=0
    
    print(expected)
    correlation_coefficient = df[Attr1].corr(df[Attr2])
    covariance = df[Attr1].cov(df[Attr2])

    min_value = df[Attr1].min()
    max_value = df[Attr1].max()

    df[Attr2] = (df[Attr1] - min_value) / (max_value - min_value)

    mean = df[Attr1].mean()
    std_dev = df[Attr1].std()
    df[Attr2] = (df[Attr1] - mean) / std_dev


    mean = df[Attr1].mean()
    std_dev = df[Attr1].std()
    df[Attr2] = (df[Attr1] - mean) / std_dev

    max_abs = df[Attr1].abs().max()
    df[Attr2] = df[Attr1] / (10 ** len(str(int(max_abs))))



    if fl:
       my_data={
        "name":node[0].name,
        "result":"correlated",
        "p":p,
        "chi2":chi2,
        "dof":dof,
        "a1":Attr1,
        "a2":Attr2
       }

       return JsonResponse(my_data)
    
    my_data={
        "name":node[0].name,
        "result":"not correlated",
        "p":p,
        "chi":chi2,
        "dof":dof,
        "a1":Attr1,
        "a2":Attr2
       }

    return JsonResponse(my_data)



def assignment3(request):
    node=CSVFile.objects.all()
    print(node[0].name)

    strr="info"
    
    if len(node)==0 :
        return HttpResponse("No csv file in database !!")

   
    print("boundary 1")
    data = pd.read_csv(node[0].file)
    df = pd.DataFrame(data)
    file_name=node[0].name
    X = df.drop('variety', axis=1)
    Y = df['variety']

    if strr=="info":
       clf = DecisionTreeClassifier(criterion='entropy')
    elif strr=="gini":
       clf= DecisionTreeClassifier(criterion="entropy", splitter="best", random_state=42)
    elif strr=="gain":
       clf = DecisionTreeClassifier(criterion='entropy', splitter='best')




    clf.fit(X, Y)
    decision_tree_text = export_text(clf, feature_names=X.columns.tolist())
    tree.plot_tree(clf, filled=True, feature_names=X.columns.tolist(), class_names=list(map(str, clf.classes_)))
    tree_image_path = 'static/plot/image.png'
    os.makedirs(os.path.dirname(tree_image_path), exist_ok=True)
    plt.savefig(tree_image_path)
    my_data={"name":file_name,"text":decision_tree_text}
    return JsonResponse(my_data)
               




def assignment3_confuse_matrix(request):
    node=CSVFile.objects.all()
    print(node[0].name)

    if len(node)==0 :
        return HttpResponse("No csv file in database !!")

    print("boundary 1")
    data = pd.read_csv(node[0].file)
    df = pd.DataFrame(data)
    file_name=node[0].name
    X = df.drop('variety', axis=1)
    Y = df['variety']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier(criterion='entropy', splitter='best')
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    conf_matrix = confusion_matrix(y_test, y_pred)

    accuracy = accuracy_score(y_test, y_pred)
    misclassification_rate = 1 - accuracy
    sensitivity = recall_score(y_test, y_pred, average='macro')
    precision = precision_score(y_test, y_pred, average='macro')

    response_data = {
        'confusion_matrix': conf_matrix.tolist(),
        'accuracy': accuracy,
        'misclassification_rate': misclassification_rate,
        'sensitivity': sensitivity,
        'precision': precision,
    }

    return JsonResponse(response_data, status=status.HTTP_200_OK)


def assignment4(request):
    node=CSVFile.objects.all()
    print(node[0].name)

    if len(node)==0 :
        return HttpResponse("No csv file in database !!")

    print("boundary 1")
    data = pd.read_csv(node[0].file)
    df = pd.DataFrame(data)
    file_name=node[0].name
    X = df.drop('variety', axis=1)
    Y = df['variety']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier(criterion='entropy', splitter='best')
    clf.fit(X_train, y_train)


    rules = export_text(clf, feature_names=list(X.columns.tolist()))

    y_pred = clf.predict(X)
    accuracy = accuracy_score(Y, y_pred)

    coverage = len(y_pred) / len(Y) * 100

    rule_count = len(rules.split('\n'))

    my_data = {
        "name":file_name,
        'rules': rules,
        'accuracy': accuracy,
        'coverage': coverage,
        'toughness': rule_count,
    }
    return JsonResponse(my_data)


def assignment5(request):
    node=CSVFile.objects.all()
    print(node[0].name)

    if len(node)==0 :
        return HttpResponse("No csv file in database !!")

    print("boundary 1")
    data = pd.read_csv(node[0].file)
    df = pd.DataFrame(data)
    file_name=node[0].name
    X = df.drop('variety', axis=1)
    Y = df['variety']
    my_data={
        "name":file_name
    }
    return JsonResponse(my_data)