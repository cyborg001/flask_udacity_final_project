import subprocess

def my_prediction():
    PIPE=subprocess.PIPE
    prediction = subprocess.run("./make_predict_azure_app.sh",stdout=PIPE, stderr=PIPE)
    return str(prediction.stdout)


if __name__ == '__main__':
    my_prediction()
# print(my_prediction())
