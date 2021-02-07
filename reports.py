#!/usr/bin/env python3

'''
This script if for generating pdf reports. It will be called by other scripts
'''

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_paragraph = Paragraph(paragraph)
    report.build([report_title, report_paragraph])
