import os
import requests

token = "7279453730:AAEQojqb_w9GaEiCLdgcZOI14NIwSI2FZcY"
chat_id = "6351803919"
ruta_de_tu_carpeta = "/storage/emulated/0/Download"

def enviar_archivo(toke, chat_id, ruta_archivo, max_tamano_mb = 3):
    try:
        #verificar el tama�o del archivo
        tamano_archivo_mb = os.path.getsize(ruta_archivo) / (1024 * 1024) #convertir a megas
        if tamano_archivo_mb > max_tamano_mb:
            print(f"el archivo {ruta_archivo} exede al tama�o maximo permitido ({max_tamano_mb} MB. no se enviaara.")
            return
        # si el tama�o es permitido, proceder con el envio del archivo

        url = f"https://api.telegram.org/bot{token}/sendDocumen"
        files = {'document': open(ruta_archivo, 'rb')}
        params = {'chat_id': chat_id}

        response = requests.post(url, files=files, params=params )

        if response.status_code == 200 and response.json()['ok']:
            print(f'Archivo {os.path.basename(ruta_archivo)} enviado exitosamente.')

        else:
            print(f'Eror al enviar el archivo :{response.json()}')

            return response.json





    except Exception as e:
        print(e)
