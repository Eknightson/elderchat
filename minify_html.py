import pdfkit

# Set the path to wkhtmltopdf manually
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Read the original HTML file
input_html = r'C:\Users\erika\Downloads\ElderGuardChatGPT\chat.html'
output_pdf = r'C:\Users\erika\Downloads\ElderGuardChatGPT\chat.pdf'

# Convert HTML to PDF
pdfkit.from_file(input_html, output_pdf, configuration=config)

print("HTML file has been successfully converted to PDF!")
