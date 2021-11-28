from django.template.loader import render_to_string
from rest_framework.renderers import BaseRenderer
from rest_framework.response import Response

import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    format = 'pdf'
    charset = 'utf-8'
    # header = {'Content-Disposition': 'attachment; filename=employee_list.pdf'}

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if hasattr(data, 'items'):
            for key, value in data.items():
                if key == 'results':
                    html_string = render_to_string('user_mbe/EmployeeList.html', {'header': ('first_name', 'last_name', 'id_number', 'phone_number', 'email', 'job_title'), 'data': [tuple(x.values()) for x in value]})
                    result = pdfkit.from_string(html_string, output_path=False, configuration=config)
                    # return Response(result, headers=self.header)
                    return result
        return None
