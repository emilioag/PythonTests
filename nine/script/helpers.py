from jinja2 import Template
import pdfkit


def create_pdf(table, out):
    width = int(100 / len(table[0]))
    headers = table[0]
    rows = table[1:]

    html = Template("""
    <table border="0" align="center" width="90%">
        <thead><tr>{% for header in headers %}<th width="{{ width }}%">{{ header }}</th>{% endfor %}</tr></thead>
        <tbody>
            {% for row in rows %}
            <tr>{% for col in row %}<td >{{ col }}</td>{% endfor %}</tr>
            {% endfor %}
        </tbody>
    </table>
    """).render(width=width, headers=headers, rows=rows)

    pdfkit.from_string(html, output_path=out)