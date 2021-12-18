from hikvision_camera import Camera

if __name__ == '__main__':
    camera = Camera('192.168.1.152', 'admin', 'Tfs123456')

    # r = camera.getHttpHostsCapabilities()

    # print(r.content.decode("utf-8"))

    r = camera.getAnprPlates()

    print(r.content.decode("utf-8"))

    r = camera.getAnprPicture()

    print(r.content.decode("utf-8"))