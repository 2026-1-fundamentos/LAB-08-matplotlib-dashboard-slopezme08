"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    # Leer datos
    df = pd.read_csv('files/input/shipping-data.csv')

    # Crear directorio docs si no existe
    os.makedirs('docs', exist_ok=True)

    # 1. Gráfico: Envíos por Warehouse
    fig, ax = plt.subplots(figsize=(10, 6))
    warehouse_counts = df['Warehouse_block'].value_counts().sort_index()
    warehouse_counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
    ax.set_title('Shipping per Warehouse', fontsize=16, fontweight='bold')
    ax.set_xlabel('Warehouse Block', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('docs/shipping_per_warehouse.png', dpi=100, bbox_inches='tight')
    plt.close()

    # 2. Gráfico: Modo de Envío
    fig, ax = plt.subplots(figsize=(10, 6))
    shipment_counts = df['Mode_of_Shipment'].value_counts().sort_index()
    shipment_counts.plot(kind='bar', ax=ax, color='coral', edgecolor='black')
    ax.set_title('Mode of Shipment', fontsize=16, fontweight='bold')
    ax.set_xlabel('Mode of Shipment', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('docs/mode_of_shipment.png', dpi=100, bbox_inches='tight')
    plt.close()

    # 3. Gráfico: Calificación promedio por Warehouse
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_rating = df.groupby('Warehouse_block')['Customer_rating'].mean().sort_index()
    avg_rating.plot(kind='bar', ax=ax, color='lightgreen', edgecolor='black')
    ax.set_title('Average Customer Rating', fontsize=16, fontweight='bold')
    ax.set_xlabel('Warehouse Block', fontsize=12)
    ax.set_ylabel('Average Rating', fontsize=12)
    ax.set_ylim(0, 5)
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('docs/average_customer_rating.png', dpi=100, bbox_inches='tight')
    plt.close()

    # 4. Gráfico: Distribución de peso
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Weight_in_gms'], bins=30, color='mediumpurple', edgecolor='black', alpha=0.7)
    ax.set_title('Weight Distribution', fontsize=16, fontweight='bold')
    ax.set_xlabel('Weight (gms)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/weight_distribution.png', dpi=100, bbox_inches='tight')
    plt.close()

    # 5. Crear HTML dashboard
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shipping Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            padding-top: 20px;
        }
        .dashboard {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        .chart {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 15px;
        }
        .chart img {
            width: 100%;
            height: auto;
        }
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shipping Dashboard</h1>
        <div class="dashboard">
            <div class="chart">
                <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
            </div>
            <div class="chart">
                <img src="mode_of_shipment.png" alt="Mode of Shipment">
            </div>
            <div class="chart">
                <img src="average_customer_rating.png" alt="Average Customer Rating">
            </div>
            <div class="chart">
                <img src="weight_distribution.png" alt="Weight Distribution">
            </div>
        </div>
    </div>
</body>
</html>"""

    with open('docs/index.html', 'w') as f:
        f.write(html_content)

pregunta_01()