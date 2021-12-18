from hikvision_camera import Camera

if __name__ == '__main__':
    camera = Camera('192.168.1.152', 'admin', 'Tfs123456')

    r = camera.getAnprPlates()

    xml = r.content.decode("utf-8")

    # print(xml)

    import xmltodict, json

    o = xmltodict.parse(xml)
    f = json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
    print(f)