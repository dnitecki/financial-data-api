from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import yfinance as yf

class GetStockInfo(APIView):
    def get(self,request):
        if request.method =='GET':
            ticker = request.GET.get('ticker',"")
            if ticker == "":
                return Response("Missing Required Parameters: Ticker", status=status.HTTP_400_BAD_REQUEST)
            stockInfo = yf.Ticker(ticker).info
            return Response({'data':stockInfo}, status=status.HTTP_200_OK)

class GetStockNews(APIView):
    def get(self,request):
        if request.method =="GET":
            ticker = request.GET.get('ticker',"")
            if ticker =="":
                return Response("Missing Required Parameters: Ticker", status=status.HTTP_400_BAD_REQUEST)
            stockNews = yf.Ticker(ticker).news
            return Response({'data':stockNews}, status=status.HTTP_200_OK)
        
class GetStockHistory(APIView):
    def get(self,request):
        if request.method =="GET":
            ticker = request.GET.get('ticker',"")
            period = request.GET.get('period',"")
            if ticker =="":
                return Response("Missing Required Parameters: Ticker", status=status.HTTP_400_BAD_REQUEST)
            elif period == "":
                data = yf.Ticker(ticker)
                stockHistory = data.history(period='1mo')
                return Response({'data':stockHistory}, status=status.HTTP_200_OK)
            elif period:
                data = yf.Ticker(ticker)
                #['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
                stockHistory = data.history(period='12mo')
                return Response({'data':stockHistory}, status=status.HTTP_200_OK)