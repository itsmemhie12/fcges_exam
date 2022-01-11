from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def trading(request):
    if request.method == "POST" and "buy" in request.POST:
        stock_name = request.POST['StockName']
        print(stock_name)
        stock_id = request.POST['StockID']
        stock_price = request.POST['StockPrice']
        lot_num = request.POST['LotNumber']
        print(stock_name, stock_id, stock_price, lot_num)
    return render(request, 'index.html')
