from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'MINDRIC LAB | GITHUB PROTOCOL', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Vibe Coding Workflow', 0, 0, 'C')

def create_cheat_sheet():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Emojis entfernt, damit PDF nicht abstürzt
    steps = [
        ("1. SOURCE CONTROL OEFFNEN", "Klicke links auf das 'Ast-Icon' (Source Control).\nShortcut: Strg + Shift + G"),
        ("2. MESSAGE EINGEBEN", "Schreibe in das Textfeld oben, was du gemacht hast.\n(z.B. 'Neues Tool' oder 'Update')."),
        ("3. COMMIT (VERPACKEN)", "Klicke auf den 'Commit' Button (Haken).\nJetzt ist das Paket geschnuert."),
        ("4. SYNC (HOCHLADEN)", "Klicke auf den blauen Button 'Sync Changes'.\nWarte kurz... Fertig!")
    ]
    
    pdf.set_fill_color(240, 240, 240)
    
    for title, desc in steps:
        pdf.set_font("Arial", 'B', 14)
        # encode('latin-1', 'replace') hilft manchmal, aber wir haben den Text bereinigt
        pdf.cell(0, 10, title, 0, 1, 'L', fill=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, desc)
        pdf.ln(5)
    
    try:
        pdf.output("Github_Cheatsheet.pdf")
        print("✅ PDF erfolgreich erstellt! Check deinen Ordner.")
    except PermissionError:
        print("❌ FEHLER: Bitte schließe die PDF-Datei, falls sie offen ist, und versuche es erneut!")

if __name__ == '__main__':
    create_cheat_sheet()