import logging
from urllib2 import Request, urlopen, HTTPError
from suds import WebFault

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('main')
from suds.client import Client
CONF = {
    'wsdl' : 'http://webservices.telus.com/wsdl/parlayx_sms_send_service_2_3.wsdl'
}
wsdl_url = CONF['wsdl']
client = Client(wsdl_url, nosend = True, prettyxml = True)
log.info(client)
charging = client.factory.create('ns0:ChargingInformation')
charging.description = 1
charging.currency = 2
charging.amount = 3
charging.code = 4
log.info(charging)
reference = client.factory.create('ns0:SimpleReference')
reference.endpoint = 1
reference.interfaceName = 2
reference.correlator = 3
log.info(reference)

req_ctx = client.service.sendSms(['tel:+123'], 'tel:12345', charging, 'test', reference)
urlx = req_ctx.client.location()
headers = req_ctx.client.headers()
xml = req_ctx.envelope

log.info('url %s' % urlx)
log.info('headers %s' % headers)
log.info('xml %s' % xml)

req = Request(urlx, data=xml, headers=headers)

try:
    result = urlopen(req)
except HTTPError as e:
    result = e
xml = result.read()
log.info(xml)
try:
    obj_result = req_ctx.succeeded(xml)
    log.info(obj_result)
except WebFault as e:
    log.error(e.fault)
    log.error(e.document)
