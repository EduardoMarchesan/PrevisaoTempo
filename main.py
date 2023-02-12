
from flask import Flask, render_template,request
import requests
import datetime

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def previsao():
    API_KEY= "d3a3f55d314b7359d6e6c345f911b1c4"
    cidade= request.form.get('name')
    if cidade =='':
        cidade = 'Sao Paulo'
    
    link= f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requi = requests.get(link)
    requi_dic = requi.json()
    clim=requi_dic['weather'][0]['description']
    clima=(f'{clim}'.title())
    tempe = requi_dic['main']['temp'] -273.15
    temp=(f'{tempe :.0f}')
    tempe_ma=requi_dic['main']['temp_max'] -273.15
    tempe_max=(f'{tempe_ma:.0f}')
    tempe_mi=requi_dic['main']['temp_min'] -273.15
    tempe_min=(f'{tempe_mi:.0f}')
    
    #abaixo as novas operações
    sunrise = datetime.datetime.fromtimestamp(requi_dic['sys']['sunrise'])
    sunset = datetime.datetime.fromtimestamp(requi_dic['sys']['sunset'])
    sensaca = requi_dic['main']['feels_like'] -273.16
    sensacao = (f'{sensaca:.0f}')
    humidity = requi_dic['main']['humidity']
    vento = requi_dic['wind']['speed']  
    #############
    
    hoje= datetime.date.today()
    
    link2= f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br"

    previ=requests.get(link2)
    previsao=previ.json()

    ######################################################################################
    
    amanha_mi = previsao['list'][0]['main']['temp_min'] -273.15
    amanha_min=(f'{amanha_mi:.1f}')
    descrica = previsao['list'][0]['weather'][0]['description']
    descricao=(f'{descrica}'.title())
    amanha_ma = previsao['list'][0]['main']['temp_max'] -273.15
    amanha_max=(f'{amanha_ma:.1f}')
    amanha_umi = previsao['list'][0]['main']['humidity']
    data= datetime.date.today()+datetime.timedelta(1)
    
    #########################################################################

    ##########################################################################
    
    amanha_dois_mi =previsao['list'][1]['main']['temp_min'] -273.15
    amanha_dois_min=(f'{amanha_dois_mi:.1f}')
    descricao_doi = previsao['list'][1]['weather'][0]['description']
    descricao_dois=(f'{descricao_doi}'.title())
    amanha_dois_ma = previsao['list'][1]['main']['temp_max'] -273.15
    amanha_dois_max=(f'{amanha_dois_ma:.1f}')
    data_dois= datetime.date.today()+datetime.timedelta(2)
    
    ###############################################################################

    ######################################################################################
    
    amanha_tres_mi = previsao['list'][2]['main']['temp_min'] -273.15
    amanha_tres_min=(f'{amanha_tres_mi:.1f}')
    descricao_tre = previsao['list'][2]['weather'][0]['description']
    descricao_tres=(f'{descricao_tre}'.title())
    amanha_tres_ma = previsao['list'][2]['main']['temp_max'] -273.15
    amanha_tres_max=(f'{amanha_tres_ma:.1f}')
    data_tres= datetime.date.today()+datetime.timedelta(3)
    
    ######################################################################################

    ######################################################################################
    
    amanha_quatro_mi = previsao['list'][3]['main']['temp_min'] -273.15
    amanha_quatro_min=(f'{amanha_quatro_mi:.1f}')
    descricao_quatr = previsao['list'][3]['weather'][0]['description']
    descricao_quatro=(f'{descricao_quatr}'.title())
    amanha_quatro_ma = previsao['list'][3]['main']['temp_max'] -273.15
    amanha_quatro_max=(f'{amanha_quatro_ma:.1f}')
    data_quatro= datetime.date.today()+datetime.timedelta(4)
    
    ######################################################################################

    ######################################################################################
    
    amanha_cinco_mi = previsao['list'][4]['main']['temp_min'] -273.15
    amanha_cinco_min=(f'{amanha_cinco_mi:.1f}')
    descricao_cinc = previsao['list'][4]['weather'][0]['description']
    descricao_cinco=(f'{descricao_cinc}'.title())
    amanha_cinco_ma = previsao['list'][4]['main']['temp_max'] -273.15
    amanha_cinco_max=(f'{amanha_cinco_ma:.1f}')
    data_cinco= datetime.date.today()+datetime.timedelta(5)


    return render_template("index.html", clima=clima, temp=temp, amanha_min=amanha_min, amanha_max=amanha_max, descricao=descricao, amanha_dois_min=amanha_dois_min, amanha_dois_max=amanha_dois_max, descricao_dois=descricao_dois, amanha_tres_max=amanha_tres_max, amanha_tres_min=amanha_tres_min, descricao_tres=descricao_tres,amanha_quatro_min=amanha_quatro_min,amanha_quatro_max=amanha_quatro_max,descricao_quatro=descricao_quatro,amanha_cinco_max=amanha_cinco_max,amanha_cinco_min=amanha_cinco_min,descricao_cinco=descricao_cinco,hoje=hoje,data=data,data_dois=data_dois,data_tres=data_tres,data_quatro=data_quatro,data_cinco=data_cinco,cidade=cidade,tempe_max=tempe_max,tempe_min=tempe_min,sunrise=sunrise, sunset=sunset, sensacao=sensacao, humidity=humidity, vento=vento)



if __name__== "__main__":
    app.run()


