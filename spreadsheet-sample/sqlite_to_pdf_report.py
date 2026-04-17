# Read data from a SQLite database and export it as a PDF report
#
# This script:
#   1. Connects to a SQLite database
#   2. Reads all rows from a specified table
#   3. Generates a formatted PDF report with:
#      - A title and timestamp
#      - A summary section (total rows, column stats)
#      - A data table with all rows
#
# Usage:
#   python sqlite_to_pdf_report.py
#   python sqlite_to_pdf_report.py --db my_database.db --table employees --output report.pdf

import argparse
import os
import sqlite3
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def read_from_database(db_path, table_name):
    """Read all rows and column names from a SQLite table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns_info = cursor.fetchall()
    if not columns_info:
        print(f"Error: Table '{table_name}' not found in '{db_path}'.")
        conn.close()
        return None, None

    column_names = [col[1] for col in columns_info]

    # Get all rows
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    conn.close()

    print(f"Read {len(rows)} row(s) from '{table_name}' in '{db_path}'")
    return column_names, rows


def compute_summary(column_names, rows):
    """Compute basic summary statistics for numeric columns."""
    summary = []
    summary.append(f"Total rows: {len(rows)}")
    summary.append(f"Columns: {', '.join(column_names)}")

    # Find numeric columns and compute stats
    for i, col_name in enumerate(column_names):
        values = []
        for row in rows:
            val = row[i]
            if isinstance(val, (int, float)):
                values.append(val)

        if values:
            avg_val = sum(values) / len(values)
            min_val = min(values)
            max_val = max(values)
            summary.append(
                f"{col_name}: min={min_val:,.2f}, max={max_val:,.2f}, avg={avg_val:,.2f}"
            )

    return summary


def generate_pdf(column_names, rows, output_path, table_name):
    """Generate a formatted PDF report from the database data."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(A4),
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=20,
        spaceAfter=12,
    )
    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.grey,
        spaceAfter=20,
    )

    elements = []

    # Title
    elements.append(Paragraph(f"Database Report: {table_name}", title_style))
    elements.append(
        Paragraph(
            f"Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}",
            subtitle_style,
        )
    )

    # Summary section
    elements.append(Paragraph("Summary", styles["Heading2"]))
    summary_lines = compute_summary(column_names, rows)
    for line in summary_lines:
        elements.append(Paragraph(line, styles["Normal"]))
    elements.append(Spacer(1, 20))

    # Data table
    elements.append(Paragraph("Data", styles["Heading2"]))

    # Build table data: headers + all rows
    header_row = [Paragraph(f"<b>{col}</b>", styles["Normal"]) for col in column_names]
    table_data = [header_row]

    for row in rows:
        formatted_row = []
        for val in row:
            if isinstance(val, float):
                formatted_row.append(f"{val:,.2f}")
            elif val is None:
                formatted_row.append("")
            else:
                formatted_row.append(str(val))
        table_data.append(formatted_row)

    # Calculate column widths based on available space
    available_width = landscape(A4)[0] - 1 * inch
    col_width = available_width / len(column_names)

    table = Table(table_data, colWidths=[col_width] * len(column_names))
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4472C4")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#D6E4F0")]),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    elements.append(table)
    elements.append(Spacer(1, 20))

    # Footer
    elements.append(
        Paragraph(
            f"Report contains {len(rows)} record(s) from table '{table_name}'.",
            subtitle_style,
        )
    )

    doc.build(elements)
    print(f"PDF report saved to '{output_path}'")


def main():
    parser = argparse.ArgumentParser(
        description="Read from a SQLite database and export a PDF report.",
    )
    parser.add_argument(
        "--db", default="data.db",
        help="Path to the SQLite database file (default: data.db)",
    )
    parser.add_argument(
        "--table", default="employees",
        help="Name of the table to export (default: employees)",
    )
    parser.add_argument(
        "--output", default="report.pdf",
        help="Path for the output PDF file (default: report.pdf)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.db):
        print(f"Error: Database '{args.db}' not found.")
        print("Run 'python spreadsheet_to_sqlite.py' first to create the database.")
        return

    # Step 1: Read from database
    column_names, rows = read_from_database(args.db, args.table)
    if column_names is None:
        return

    # Step 2: Generate the PDF report
    generate_pdf(column_names, rows, args.output, args.table)


if __name__ == "__main__":
    main()
