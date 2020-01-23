"""An example of how to use the light parser for parsing UBX messages from a serial device.

You will need to change the port name to that of the port you want to connect to. Also make sure that the baud rate is
correct and that the device has been setup to output the messages via UBX protocol to your desired port!

The serial package could easily be replaced with an alternative.
"""

import serial

from ubxtranslator.core import Parser
from ubxtranslator.predefined import NAV_CLS, ESF_CLS


def run():
    port = serial.Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', baudrate=115200, timeout=0.1)

    parser = Parser([
        NAV_CLS, ESF_CLS
    ])

    print("Starting to listen for UBX packets")

    try:
        while True:
            try:
                msg = parser.receive_from(port)
                print(msg)
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()
#data types here https://www.u-blox.com/en/docs/UBX-13003221#page=123&zoom=auto,-195,6
# 5
# z-axis gyroscope angular rate
# deg/s *2^-12
# signed
# 12
# gyroscope temperature
# deg Celsius * 1e-
# 2
# signed
# 13
# y-axis gyroscope angular rate
# deg/s *2^-12
# signed
# 14
# x-axis gyroscope angular rate
# deg/s *2^-12
# signed
# 16
# x-axis accelerometer specific force
# m/s^2 *2^-10
# signed
# 17
# y-axis accelerometer specific force
# m/s^2 *2^-10
# signed
# 18
# z-axis accelerometer specific force
# m/s^2 *2^-10
# signed
# ('ESF', 'RAW', RAW(reserved1=68134, RB=[RB(data=data(dataType=16, dataField=8387013), sTtag=1735191), RB(data=data(dataType=17, dataField=2067), sTtag=1735191), RB(data=data(dataType=18, dataField=8378200), sTtag=1735191), RB(data=data(dataType=14, dataField=905), sTtag=1735191), RB(data=data(dataType=13, dataField=8387546), sTtag=1735191), RB(data=data(dataType=5, dataField=93), sTtag=1735191), RB(data=data(dataType=12, dataField=2601), sTtag=1735191), RB(data=data(dataType=16, dataField=8386998), sTtag=1735447), RB(data=data(dataType=17, dataField=2061), sTtag=1735447), RB(data=data(dataType=18, dataField=8378200), sTtag=1735447), RB(data=data(dataType=14, dataField=624), sTtag=1735447), RB(data=data(dataType=13, dataField=8388108), sTtag=1735447), RB(data=data(dataType=5, dataField=8388545), sTtag=1735447), RB(data=data(dataType=12, dataField=2599), sTtag=1735447), RB(data=data(dataType=16, dataField=8386986), sTtag=1735701), RB(data=data(dataType=17, dataField=2081), sTtag=1735701), RB(data=data(dataType=18, dataField=8378224), sTtag=1735701), RB(data=data(dataType=14, dataField=437), sTtag=1735701), RB(data=data(dataType=13, dataField=8387858), sTtag=1735701), RB(data=data(dataType=5, dataField=0), sTtag=1735701), RB(data=data(dataType=12, dataField=2600), sTtag=1735701), RB(data=data(dataType=16, dataField=8387008), sTtag=1735956), RB(data=data(dataType=17, dataField=2100), sTtag=1735956), RB(data=data(dataType=18, dataField=8378204), sTtag=1735956), RB(data=data(dataType=14, dataField=874), sTtag=1735956), RB(data=data(dataType=13, dataField=8387733), sTtag=1735956), RB(data=data(dataType=5, dataField=405), sTtag=1735956), RB(data=data(dataType=12, dataField=2602), sTtag=1735956), RB(data=data(dataType=16, dataField=8386998), sTtag=1736212), RB(data=data(dataType=17, dataField=2083), sTtag=1736212), RB(data=data(dataType=18, dataField=8378216), sTtag=1736212), RB(data=data(dataType=14, dataField=1248), sTtag=1736212), RB(data=data(dataType=13, dataField=8388139), sTtag=1736212), RB(data=data(dataType=5, dataField=187), sTtag=1736212), RB(data=data(dataType=12, dataField=2599), sTtag=1736212), RB(data=data(dataType=16, dataField=8386998), sTtag=1736466), RB(data=data(dataType=17, dataField=2082), sTtag=1736466), RB(data=data(dataType=18, dataField=8378201), sTtag=1736466), RB(data=data(dataType=14, dataField=468), sTtag=1736466), RB(data=data(dataType=13, dataField=8387765), sTtag=1736466), RB(data=data(dataType=5, dataField=249), sTtag=1736466), RB(data=data(dataType=12, dataField=2606), sTtag=1736466), RB(data=data(dataType=16, dataField=8386995), sTtag=1736721), RB(data=data(dataType=17, dataField=2082), sTtag=1736721), RB(data=data(dataType=18, dataField=8378228), sTtag=1736721), RB(data=data(dataType=14, dataField=905), sTtag=1736721), RB(data=data(dataType=13, dataField=8387889), sTtag=1736721), RB(data=data(dataType=5, dataField=218), sTtag=1736721), RB(data=data(dataType=12, dataField=2598), sTtag=1736721), RB(data=data(dataType=16, dataField=8387017), sTtag=1736976), RB(data=data(dataType=17, dataField=2078), sTtag=1736976), RB(data=data(dataType=18, dataField=8378222), sTtag=1736976), RB(data=data(dataType=14, dataField=905), sTtag=1736976), RB(data=data(dataType=13, dataField=8388046), sTtag=1736976), RB(data=data(dataType=5, dataField=468), sTtag=1736976), RB(data=data(dataType=12, dataField=2604), sTtag=1736976), RB(data=data(dataType=16, dataField=8386998), sTtag=1737231), RB(data=data(dataType=17, dataField=2068), sTtag=1737231), RB(data=data(dataType=18, dataField=8378199), sTtag=1737231), RB(data=data(dataType=14, dataField=936), sTtag=1737231), RB(data=data(dataType=13, dataField=8387952), sTtag=1737231), RB(data=data(dataType=5, dataField=93), sTtag=1737231), RB(data=data(dataType=12, dataField=2604), sTtag=1737231), RB(data=data(dataType=16, dataField=8387011), sTtag=1737486), RB(data=data(dataType=17, dataField=2057), sTtag=1737486), RB(data=data(dataType=18, dataField=8378233), sTtag=1737486), RB(data=data(dataType=14, dataField=530), sTtag=1737486), RB(data=data(dataType=13, dataField=8388108), sTtag=1737486), RB(data=data(dataType=5, dataField=187), sTtag=1737486), RB(data=data(dataType=12, dataField=2602), sTtag=1737486)]))