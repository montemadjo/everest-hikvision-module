import requests
from requests import auth
from requests.auth import HTTPDigestAuth
from requests.models import Response

class Camera:
    def __init__(self, URL, username, password) -> None:
        self.url_trigger = 'http://' + URL + '/ISAPI/System/IO/outputs/1/trigger'
        self.url_anpr_register = 'http://' + URL + ''
        self.xxx = 'http://admin:Tfs123456@192.168.1.152/ISAPI/Traffic/channels/1/vehicleDetect/plates'
        self.url_anpr_get_cap = 'http://' + URL + '/ISAPI/Event/notification/httpHosts/capabilities'
        self.url_anpr_get_plates = 'http://' + URL + '/ISAPI/Traffic/channels/1/vehicleDetect/plates'
        self.url_anpr_get_picture = 'http://' + URL + '/ISAPI/ContentMgmt/search'

        self.username = username
        self.password = password

        self.raw_high_request = '<IOPortData version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema"><outputState>high</outputState></IOPortData>'
        self.raw_low_request = '<IOPortData version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema"><outputState>low</outputState></IOPortData>'
        self.raw_http_hosts_request = """
        <?xml version="1.0" encoding="UTF-8"?>
        <HttpHostNotificationList version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
            <HttpHostNotification version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
                <id>1</id>
                <url>/</url>
                <protocolType>HTTP</protocolType>
                <parameterFormatType>XML</parameterFormatType>
                <addressingFormatType>ipaddress</addressingFormatType>
                <ipAddress>192.168.1.72</ipAddress>
                <portNo>8080</portNo>
                <userName></userName>
                <httpAuthenticationMethod>none</httpAuthenticationMethod>
                <ANPR>
                    <detectionUpLoadPicturesType opt="all,licensePlatePicture,detectionPicture">detectionPicture</detectionUpLoadPicturesType>
                </ANPR>
            </HttpHostNotification>
        </HttpHostNotificationList>"""
        self.body_anpr_get_plates = """
        <AfterTime>
            <picTime>2020-03-07T21:00:00Z</picTime>
        </AfterTime>
        """
        self.body_anpr_pic_search = """
        <?xml version: '1.0' encoding='utf-8'?>
        <CMSearchDescription version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
            <searchID>C77384AD-66A0-0001-E7C2-1151F04F90B0</searchID>
            <trackIDList>
                <trackID>103</trackID>
            </trackIDList>
            <timeSpanList>
                <timeSpan>
                    <startTime>2020-06-22T02:25:13Z</startTime>
                    <endTime>2022-06-22T02:25:13Z</endTime>
                </timeSpan>
            </timeSpanList>
            <searchTypeList>
            </searchTypeList>
            <contentTypeList>
                <contentType>metadata</contentType>
            </contentTypeList>
            <maxResults>100</maxResults>
            <searchResultPostion>0</searchResultPostion>
            <metadataList>
                <metadataDescriptor>
                //recordType.meta.std-cgi.com
                </metadataDescriptor>
                <SearchProperity>
                </SearchProperity>
            </metadataList>
        </CMSearchDescription>
        """
    def postOutputRequest(self, state) -> None:
        if state is 1:
            response = requests.put(self.url_trigger, data=self.raw_high_request, auth=HTTPDigestAuth(self.username, self.password))
            print(response)
        elif state is 0:
            response = requests.put(self.url_trigger, data=self.raw_low_request, auth=HTTPDigestAuth(self.username, self.password))
            print(response)

    def subscribeToAnpr(self, ip_address, port):
        print(ip_address)
        print(port)
        response = requests.put(self.url_trigger, data=self.raw_http_hosts_request,
                                auth=HTTPDigestAuth(self.username, self.password))
        return response

    def getHttpHostsCapabilities(self):
        response = requests.get(self.url_anpr_get_cap, auth=HTTPDigestAuth(self.username, self.password))

        return response

    def getAnprPlates(self):
        response = requests.post(self.xxx, data=self.body_anpr_get_plates, auth=HTTPDigestAuth(self.username, self.password))

        return response

    def getAnprPicture(self):
        response = requests.post(self.url_anpr_get_picture, data=self.body_anpr_pic_search, auth=HTTPDigestAuth(self.username, self.password))

        return response