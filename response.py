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
