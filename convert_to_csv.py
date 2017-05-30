import re


def convert(file):
    """
    To convert normal spaced data to CSV
    """
    conversion_1 = re.sub(r'([^0-9])\s+([0-9])', r'\g<1>,\g<2>', file.read())
    conversion_2 = re.sub(r'([0-9])\s+([a-zA-Z])', r'\g<1>\n\g<2>', conversion_1)
    conversion_3 = re.sub(r'([0-9])\s+([0-9])', r'\g<1>,\g<2>', conversion_2)
    final_csv = re.sub(r'([^0-9])\s+([^0-9])', r'\g<1>_\g<2>', conversion_3)
    return final_csv
