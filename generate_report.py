from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import glob

# Setup PDF
doc = SimpleDocTemplate("final_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# 1. Add Title
elements.append(Paragraph("Population Data Analysis Report", styles['Title']))
elements.append(Spacer(1, 12))

# 2. Add Summary of Insights
summary_text = """
<b>Summary of Key Insights:</b><br/><br/>
• India and China have the highest populations.<br/>
• Population distribution is heavily skewed toward Asia.<br/>
• Some countries like Monaco show up as outliers with high population density.<br/>
• Africa has many countries with lower population but high growth trends.<br/>
"""
elements.append(Paragraph(summary_text, styles['BodyText']))
elements.append(Spacer(1, 12))

# 3. Add Code Files (insert contents of .py files)
code_files = ['population_scraper.py', 'eda_population.py', 'eda_and_visualization.py']
for file in code_files:
    try:
        with open(file, 'r') as f:
            content = f.read().replace('\n', '<br/>').replace(' ', '&nbsp;')
        elements.append(Paragraph(f"<b>Code: {file}</b>", styles['Heading3']))
        elements.append(Paragraph(content, styles['Code']))
        elements.append(Spacer(1, 12))
    except FileNotFoundError:
        elements.append(Paragraph(f"<i>{file} not found.</i>", styles['BodyText']))
        elements.append(Spacer(1, 12))

# 4. Add Graphs (assumes they are saved as PNG files in the same folder)
image_files = glob.glob("*.png")  # Finds all .png images in the current folder
for image in image_files:
    elements.append(Paragraph(f"<b>Graph: {image}</b>", styles['Heading3']))
    elements.append(Image(image, width=400, height=250))
    elements.append(Spacer(1, 12))

# 5. Build the PDF
doc.build(elements)

print("✅ final_report.pdf has been generated.")
