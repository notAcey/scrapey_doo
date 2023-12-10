from flask import Flask, request, jsonify, render_template, url_for
from openpyxl import Workbook
from Classes.Altex_Scraper import Altex_Scraper
from Classes.OLX_Scraper import OLX_Scraper
from Classes.PCGarage_Scraper import PCGarage_Scraper
from Modules.UI_Module import UI
import os
import csv

app = Flask(__name__)

ui = UI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    if "altex" in url:
        scraper = Altex_Scraper(url)
    elif "olx" in url:
        scraper = OLX_Scraper(url)
    elif "pcgarage" in url:
        scraper = PCGarage_Scraper(url)
    else:
        return jsonify({"error": "URL necunoscut"}), 400

    products = scraper.get_products()
    return jsonify(products)

@app.route('/get_products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)
    products = ui.get_product_list()

    start = (page - 1) * per_page
    end = start + per_page
    page_products = products[start:end]

    has_next = end < len(products)
    return jsonify({"products": page_products, "has_next": has_next})

@app.route('/initialize_scraper', methods=['POST'])
def initialize_scraper():
    try:
        data = request.json
        link = data.get('link')
        ui.initialize_scraper(link)
        products = ui.get_product_list()
        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/clear_filters', methods=['POST'])
def clear_filters():
    return jsonify({'message': 'Filters cleared'})

def generate_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Header1', 'Header2', 'Header3'])  # Modificați anteturile
        for row in data:
            writer.writerow([row['field1'], row['field2'], row['field3']])

def generate_excel(data, file_path):
    wb = Workbook()
    ws = wb.active
    ws.append(['Header1', 'Header2', 'Header3'])  # Modificați anteturile

    for row in data:
        ws.append([row['field1'], row['field2'], row['field3']])

    wb.save(file_path)

def generate_export_file(export_type, data):
    file_name = f"exported_data.{export_type}"
    file_path = os.path.join('static', file_name)

    if export_type == 'csv':
        generate_csv(data, file_path)
    elif export_type == 'excel':
        generate_excel(data, file_path)
    else:
        raise ValueError("Invalid export type")

    return file_name

def get_export_data():
    # Logică pentru obținerea datelor
    # Depinde de structura internă a aplicației
    pass

@app.route('/export_products', methods=['GET'])
def export_products():
    export_type = request.args.get('type')
    if export_type not in ['csv', 'excel']:
        return jsonify({'error': 'Invalid export type'}), 400

    data = get_export_data()  # Presupunem că avem o funcție care returnează datele

    try:
        file_name = generate_export_file(export_type, data)
        file_url = url_for('static', filename=file_name, _external=True)
        return jsonify({'fileUrl': file_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(host='0.0.0.0', port=5000)