import os
from datetime import datetime

import pandas as pd
from jinja2 import Template

TEMPLATE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Strategy Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 40px; }
        th, td { border: 1px solid #aaa; padding: 8px; text-align: center; }
        th { background-color: #444; color: white; }
        .summary { background-color: #e6f7ff; font-weight: bold; }
    </style>
</head>
<body>
    <h1>📊 Strategy Report — {{ date }}</h1>

    {% for strategy in strategies %}
        <h2>{{ strategy.name }}</h2>
        {% if strategy.data.empty %}
            <p>No data available.</p>
        {% else %}
            <table>
                <thead>
                    <tr>
                        {% for col in strategy.data.columns %}
                            <th>{{ col }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for row in strategy.data.itertuples(index=False) %}
                        <tr>
                            {% for item in row %}
                                <td>{{ item }}</td>
                            {% endfor %}
                        </tr>
                {% endfor %}
                </tbody>
            </table>
            <p class="summary">Total Trades: {{ strategy.total_trades }} | Net Profit: ₹{{ strategy.total_profit }}</p>
        {% endif %}
    {% endfor %}
</body>
</html>
"""


def generate_report():
    log_folder = os.path.join(os.getcwd(), "logs")
    strategies = []

    files = {"RSI": "rsi_trades.csv", "MACD+BB": "macd_trades.csv", "Meta": "meta_trades.csv"}

    for name, filename in files.items():
        path = os.path.join(log_folder, filename)
        try:
            df = pd.read_csv(path)
            df["profit"] = df["profit"].astype(float)

            strategies.append(
                {
                    "name": name,
                    "data": df,
                    "total_trades": len(df),
                    "total_profit": round(df["profit"].sum(), 2),
                }
            )
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")
            strategies.append(
                {"name": name, "data": pd.DataFrame(), "total_trades": 0, "total_profit": 0.0}
            )

    if not any(s["total_trades"] > 0 for s in strategies):
        print("❌ No valid logs to report.")
        return None

    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    template = Template(TEMPLATE_HTML)
    html_content = template.render(strategies=strategies, date=today)

    html_path = os.path.join(os.getcwd(), "strategy_report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Strategy report saved to {html_path}")

    # PDF Export
    pdf_path = os.path.join(os.getcwd(), "strategy_report.pdf")
    try:
        from weasyprint import CSS, HTML

        HTML(string=html_content).write_pdf(
            pdf_path, stylesheets=[CSS(string="body { font-family: Arial; }")]
        )
        print(f"✅ PDF report saved to {pdf_path}")
    except Exception as e:
        print(f"⚠️ PDF export failed: {e}")
        pdf_path = None

    return html_path, pdf_path
