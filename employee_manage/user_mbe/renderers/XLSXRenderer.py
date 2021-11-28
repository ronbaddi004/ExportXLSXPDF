import openpyxl

import os

from rest_framework.renderers import BaseRenderer
from rest_framework.response import Response

import random


class XLSXRenderer(BaseRenderer):
    media_type = 'application/xlsx'
    format = 'xlsx'
    charset = 'utf-8'
    # header = {'Content-Disposition': 'attachment; filename=employee_list.xlsx'}

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if hasattr(data, 'items'):
            for key, value in data.items():
                if key == 'results':
                    results = [('first_name', 'last_name', 'id_number', 'phone_number', 'email', 'job_title')] + [tuple(x.values()) for x in value]

                    wb = openpyxl.Workbook()
                    sheet = wb.active
                    for row in range(1, len(results) + 1):
                        for col in range(1, len(results[0]) + 1):
                            _ = sheet.cell(column=col, row=row, value="{0}".format(results[row - 1][col - 1]))
                    
                    temp_file = f"temporary_{random.randint(0,100000)}.xlsx"
                    wb.save(filename=temp_file)

                    with open(temp_file, 'rb') as f:
                        excel_data = f.read()

                    os.remove(temp_file)

                    # return Response(excel_data, headers=self.header)
                    return excel_data
        return None
