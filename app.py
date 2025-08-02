from flask import Flask, render_template, request, redirect

app = Flask(__name__)

links = {
    "YouTube": "https://www.youtube.com/",
    "OneDrive": "https://librefutbol.su/eventos/?r=aHR0cHM6Ly9jYW5kbGVyLmJlYXV0eS92b2QuaHRtbD9nZXQ9aHR0cHM6Ly92b29kYy5jb20vZW1iZWQvODU4YTkzOTBhMTg0OGE5Mzg3OTk4MzhiOTU4Yjk4ODU4Yjk2Lmh0bWw=",
    "ecuabet": "https://ecuabet.com/deportes/partido/10613354?utm_source=Directa&utm_medium=Invasivo&utm_campaign=Evento_Tactico_ECU_Oct2024&utm_term=Evento&utm_content=Evento_Tactico_ECU_Oct2024",
    "mega": "https://www.bilibili.tv/en/video/2042945247",
    "mega2": "https://getbootstrap.com/docs/5.0/getting-started/introduction/",
    "mega3": "https://reclutamiento.tia.com.ec/buscar",
}

@app.route('/')
def index():
    return render_template('index.html', links=links)

@app.route('/load', methods=['POST'])
def load():
    url = request.form.get('url')
    if url:
        return redirect(url)
    #return redirect('/')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(host='0.0.0.0', debug=True) # python app.py