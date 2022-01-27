from rest_framework.views import APIView
from rest_framework.response import Response


class CongView(APIView):
    # 따로 정의한 기능
    # 유저 이메일은 잠깐 보류..
    version = ''

    #헤더영역
    def dispatch(self, request, *args, **kwargs):
        self.version = request.headers.get('version', '1.0')
        ## dispatch 부분을 APIView보다 CongView에서 먼저 처리한다..?
        return super(CongView, self).dispatch(request, *args, **kwargs)



def CommonResponse(resultCode, resultMsg, data):
    return Response(status=200,
                    data=dict(
                        resultCode=resultCode,
                        resultMsg=resultMsg,
                        data=data
                        )
                    )

def SuccessResponse():
    return Response(status=200,
                    data=dict(
                        resultCode=0,
                        resultMsg="success"
                        )
                    )

def SuccessResponseWithData(data):
    return Response(status=200,
                    data=dict(
                        resultCode=0,
                        resultMsg="success",
                        data=data
                        )
                    )

def ErrorResponse():
    return Response(status=200,
                    data=dict(
                       resultCode=999,
                       resultMsg="error!!!"
                            )
                    )