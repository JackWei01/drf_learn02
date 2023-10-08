from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning,AcceptHeaderVersioning

# Create your views here.
class GETHomeView(APIView):
    #基于get参数的版本获取
    #配置文件 VERSION_PARAM 决定get 中版本号的名字
    #http://dasdadawd.dadsa/user/?version=1.1.1    默认值为version

    versioning_class = QueryParameterVersioning
    def get(self,request):
        print(request.version)



        print(request.versioning_scheme)
        url_reverse = request.versioning_scheme.reverse("gethome",request=request)
        print("反向生成URL:",url_reverse) #与django不同的是，反向生成的URL包括get参数形式的版本信息

        return Response("gethome!")


class URLHomeView(APIView):
    # 基于URL的版本获取
    # 配置文件 VERSION_PARAM 决定get 中版本号的名字
    # http://dasdadawd.dadsa/user/?version=1.1.1    默认值为version

    versioning_class = URLPathVersioning

    # def get(self, request,version):
    def get(self, request,*args,**kwargs):


        print(request.version)
        url_reverse = request.versioning_scheme.reverse("UrlHome", request=request)
        print("反向生成URL:", url_reverse)  # 与django不同的是，反向生成的URL包括get参数形式的版本信息


        return Response("URLHomeView!")

class HeaderHomeview(APIView):
    #基于请求头的版本获取  前端 Headers的key为 Accept Value为application/json;version=v2
    versioning_class = AcceptHeaderVersioning
    def get(self,request):
        print(request.version)
        url_reverse = request.versioning_scheme.reverse("HeaderHome", request=request)
        print("反向生成URL:", url_reverse)  # 与django不同的是，反向生成的URL包括get参数形式的版本信息

        return Response("HeaderHomeview!")