from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    area = None
    money = None
    
    if request.method == 'POST':
        # Проверяем, был ли загружен файл
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                # ТУТ ЛОГИКА ВАШЕЙ НЕЙРОСЕТИ
                # Для примера ставим тестовые данные:
                area = 150.5 
                money = "4 500 000"
                
    return render_template('index.html', area=area, money=money)

if __name__ == '__main__':
    app.run(debug=True)