import requests;
import urllib3;
import pandas;
class HttpRequest:


    def  http_request(self,  request_url, request_data,method,cookie = None):
        header = ""
        # login_res = requests.post(request_url,request_data);
        # print("相应头2：", login_res.headers)
        # print("相应码2：", login_res.status_code)
        # print("相应报文2：", login_res.text)
        # print("cookies：", login_res.cookies);

        # 我学的接口  https://openapiv51.ketangpai.com/CourseApi/semesterList
        # res = requests.post(request_url, request_data);
        # print("登录结果是33：", res);
        urllib3.disable_warnings()
        if method.lower()=="get":
            res = requests.get(request_url, request_data,cookies = cookie,verify=False);
        else:
            reques = {"X-Lemonban-Media-type":"lemonban.v2"};
            res = requests.post(request_url, request_data,cookies = cookie,verify=False,headers=reques);
            #res = requests.post(request_url, request_data);
        return res;

if __name__ == '__main__':
    #url = "https://openapiv5.ketangpai.com//UserApi/login";
    url = "http://api.lemonban.com/futureloan/member/register";

    data = {"mobile_phone": "731569578@qq.com", "password": "wang123"};
    res = HttpRequest().http_request(url,data,'post');
    print("登录结果是：",res.json());