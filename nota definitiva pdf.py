from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.text(10 , 15, 'fecha: 18/11/2023')
pdf.text(10, 30, 'nombre de la materia:')
pdf.text(10, 40, 'nombre del profesor:')
pdf.text(10, 50, 'nombre del estudiante:')
pdf.dashed_line 
pdf.output('nota.pdf', 'F') 