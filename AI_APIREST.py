from flask import Flask, request, jsonify
import joblib
import cv2
import numpy as np

app = Flask(__name__)

def load_model():
    model_path = "D:/User/fbdio/OneDrive/Área de Trabalho/PORTRESP_IA_ENTREGA4/modelo_rf.joblib"
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        return f"Erro ao carregar o modelo: {str(e)}", 500  # Código de status 500 para erro interno do servidor

@app.route('/predict', methods=['POST'])
def predict():
    # Carregar o modelo
    model = load_model()

    if not model:
        return jsonify({'error': 'Erro ao carregar o modelo'}), 500

    # Obter os dados da imagem da solicitação
    try:
        data = request.get_json(force=True)
        image_data = data.get('image')

        if not image_data:
            return jsonify({'error': 'Dados da imagem ausentes'}), 400  # Código de status 400 para solicitação inválida

        # Preprocessar a imagem
        common_size = (100, 100)
        image = cv2.resize(np.array(image_data), common_size)
        image_flatten = image.flatten().reshape(1, -1)

        # Fazer a previsão
        prediction = model.predict(image_flatten)

        # Enviar a resposta
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': f'Erro ao processar a solicitação: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
