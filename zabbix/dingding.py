import requests
class SendMsg(object):
    def __init__(self, content):
        self.msg = {
            "msgtype": "text",
            "text": {
                "content": "Test "+content,
            },
            "at": {
                "atMobiles": [
                    # @工作群里的某人, 直接手机号"
                    "185****",
                ],
                "isAtAll": False
            }
        }
        self.send()

    def send(self):
        response = requests.post(
            # dingding token，推送至工作群，支持钉、飞书、企业微信等
            # url="https://oapi.dingtalk.com/robot/send?access_token=fcc5717ad895ea02fe0f337366a7fe7b443c2078f7a0ae191ef85e20e1312a",
            url='https://oapi.dingtalk.com/robot/send?access_token=fcc5717ad895ea02fe0f337366a7fe7b443c2078f7a0ae191ef85e20e13125',
           json=self.msg,
        )
        print(response.content)
