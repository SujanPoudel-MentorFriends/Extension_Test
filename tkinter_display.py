import tkinter as tk
from tkinter import scrolledtext

def generate_report(report):
    report_lines = [
        f"URL: {report['url']}",
        f"Question: {report['question']}",
        f"Expected Answer: {report['expected_answer']}",
        f"Actual Response: {report.get('actual_response', 'N/A')}",
        f"Boom Button Text: {report.get('boom_button_text', 'N/A')}",
        f"Boom Button Status: {report.get('boom_button_status', 'N/A')}",
        f"Response Match: {report.get('response_match', 'N/A')}",
    ]
    
    if report['errors']:
        report_lines.append("Errors:")
        for error in report['errors']:
            report_lines.append(f"- {error}")
    
    return "\n".join(report_lines)


def display_report(report):
    report_text = generate_report(report)
    
    # Create the main window
    root = tk.Tk()
    root.title("YouChat Report")

    # Create a ScrolledText widget to display the report
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    text_area.pack(padx=10, pady=10)

    # Insert the report text
    text_area.insert(tk.END, report_text)
    text_area.configure(state='disabled')  # Make the text area read-only

    # Start the Tkinter event loop
    root.mainloop()
