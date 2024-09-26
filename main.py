from collections import Counter

# Read the input text file and convert it to HTML format
def txt_to_html(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Count occurrences of each size
    sizes = [line.split()[1] for line in lines if line.strip()]
    size_counts = Counter(sizes)

    # Create the basic structure of the HTML file
    html_content = '''<html>
    <head>
        <title>Dirsearch Output</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Dirsearch Results</h2>
        <table>
            <tr>
                <th>Status Code</th>
                <th>Size</th>
                <th>URL</th>
            </tr>'''

    # Loop through the lines and add them to the HTML table
    for line in lines:
        if line.strip():  # Ignore empty lines
            parts = line.split()
            status_code = parts[0]
            size = parts[1]
            url = parts[2]

            # Only add rows with sizes that appear 5 times or less
            if size_counts[size] <= 5:
                html_content += f'''
            <tr>
                <td>{status_code}</td>
                <td>{size}</td>
                <td><a href="{url}" target="_blank">{url}</a></td>
            </tr>'''

    # Close the HTML table and body
    html_content += '''
        </table>
    </body>
    </html>'''

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Use the function to convert the txt to html
txt_to_html('dirsearch.txt', 'dirsearch_output.html')
