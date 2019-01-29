#  -*- coding: utf-8 -*-
import requests

def getInterfaces():
    url = 'http://caas-uip.caasdev.cs2025.cn/v2/api-docs'
    r = requests.get(url).json()
    data1 = r["tags"]
    data = r["paths"]
    # print(len(data))
    interfaces = []

    for k, v in data.items():

        # print("-----------parse start-----------")
        # print("一：%s,%s" %(k,v))
        for _k, _v in v.items():
            interface = {}
            # print("二：%s,%s" %(_k,_v))
            params_dict = {}
            if _v.get("parameters"):
                # print("一：%s,%s" % (_k, _v))
                for i in _v.get("parameters"):
                    # print(i)
                    params_dict[i.get("name")] = ''
                for param in params_dict:
                    if param.find("data.") >= 0:
                        params_dict.pop("data")
                        break

            name = _v["summary"]
            url = k
            method = _k.upper()
            # tags = ''.join(_v["tags"])
            params = params_dict
            interface["name"] = name
            interface["times"] = 1
            interface["request"] = {}
            interface["request"]["url"] = url
            interface["request"]["method"] = method
            if "consumes" in _v.keys():
                interface["request"]["json"] = params
            else:
                interface["request"]["params"] = params
            interface["desc"] = {}
            interface["desc"]["header"] = {}
            interface["desc"]["data"] = {}
            interface["desc"]["files"] = {}
            interface["desc"]["params"] = params
            interface["desc"]["variables"] = {}
            interface["desc"]["extract"] = {}

            interfaces.append(interface)


        # print("----------parse end-----------")
    return interfaces

if __name__ == '__main__':
    interfaces = getInterfaces()
    print(interfaces)
    print(len(interfaces))
