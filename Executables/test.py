import json
if __name__ == '__main__':
    l = ('hi','no')
    d = {"l":False}
    d = json.dumps(d)
    if isinstance(d["l"],str):
        print("yess")
    st = ""
