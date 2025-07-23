import pandas as pd

def export_summary_to_excel(summary_dict, filename="ecommerce_analysis_report.xlsx"):
   
    with pd.ExcelWriter(filename) as writer:
        for sheet, data in summary_dict.items():
            if isinstance(data, pd.Series):
                data.to_frame().to_excel(writer, sheet_name=sheet)
            else:
                data.to_excel(writer, sheet_name=sheet)
    print(f"✅ Excel report saved as: {filename}")
