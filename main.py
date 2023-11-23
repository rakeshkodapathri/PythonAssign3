from flask import Flask, request, jsonify,render_template
import requests
import os

app = Flask(__name__)

@app.route('/getweatherdetails', methods=['GET'])

def get_weather():
    api_key = os.getenv('my_api_key')
    city = request.args.get('city')

    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {'key': api_key, 'q': city}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            output_data = {
                'weather': {
                    'cloud': data['current']['cloud'],
                    'gust_kph': data['current']['gust_kph'],
                    'last_updated': data['current']['last_updated'],
                    'precip_mm': data['current']['precip_mm']
                }
            }
            return jsonify(output_data)
        else:
            return jsonify({'error': data}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug = True)
