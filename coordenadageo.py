#
# Author: Mauricio Perea
# Mail: mauricio.perea@correounivalle.edu.co
# Abstract: Calcula una coordenada en grados decimales 
# Version: 1.0 for PyWPS 4.0
# 

from math import sqrt
from pywps import Process, LiteralInput,  LiteralOutput

class gradodecimal(Process):
    def __init__(self):
        inputs = [ LiteralInput('x1', 'Grados', data_type='float'),
        LiteralInput('x2', 'Minutos', data_type='float'),
        LiteralInput('x3', 'Segundos', data_type='float') ]
        
        outputs = [LiteralOutput('resultado', 'Resultado Calculo', data_type='float' )]

        super(gradodecimal, self).__init__(
            self._handler,
            identifier='coordenadageo',
            version='None',
            title='Coordenadas decimales',
            abstract='Calcula una coordenadas en grados decimales',
            profile='',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        #bloque para realizar los calculos
        x1a= float(request.inputs['x1'][0].data)
        x2a= float(request.inputs['x2'][0].data)
        x3a= float(request.inputs['x3'][0].data)
        mdo = (x1a)
        mdx = (x2a/60)
        mdy = (x3a/3600)
        gradodecimalgeo = (mdo+mdx+mdy)
        response.outputs['resultado'].data = float(gradodecimalgeo)
        return response
    