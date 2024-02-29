import requests

class TestApi:
    def test_get_token(self):
        url="https://api.weixin.qq.com/cgi-bin/token"
        datas={
            "grant_type":"client_credential",
            "appid":"wx74a8627810cfa308",
            "secret":"e40a02f9d79a8097df497e6aaf93ab80"
        }
        res=requests.get(url,params=datas)
        print(res.json())

if __name__ == '__main__':
    TestApi().test_get_token()