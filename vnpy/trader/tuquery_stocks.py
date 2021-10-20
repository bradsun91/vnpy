import tushare as ts
from vnpy.trader.object import HistoryRequest,BarData
from vnpy.trader.constant import Exchange
from datetime import  datetime
print("/Users/miaoyuesun/Code_Workspace/vnpy/vnpy/trader/tuquery.py")

class TushareData:
    def __init__(self):
        ts.set_token('f54f66391ef9cf7675004be86d1ea74740d6df4df971cc10b3bbad91')
        return
    def exchange_bond(self,exchange:Exchange):
        # 期货交易所
        if exchange.value == "SHFE":
            return "SHF"
        elif exchange.value == "CZCE":
            return  "ZCE"
        elif exchange.value == "DCE":
            return  "DCE"
        elif exchange.value == "CFFEX":
            return  "CFX"
        # 股票交易所
        # elif exchange.value == "SZSE":
        #     return  "SZSE"
        # elif exchange.value == "SSE":
        #     return  "SSE"    
        else :
            return  exchange.value
        
    def tuquery(self,req:HistoryRequest):
        symbol = req.symbol
        exchange = req.exchange
        interval = req.interval
        print(exchange)
        # print(req.start)
        # print(req.start.strftime('%Y%m%d'))

        start = req.start.strftime('%Y%m%d')
        end = req.end.strftime('%Y%m%d')
        tcode = f'{symbol}'+'.'+ self.exchange_bond(exchange)
        pro = ts.pro_api();
        # df = pro.fut_daily(ts_code= tcode, start_date= start, end_date= end)
        df = ts.pro_bar(ts_code=tcode, adj='qfq', start_date=start, end_date=end)
        df.sort_values("trade_date", inplace = True)
        print(df)
        data: List[BarData] = []

        if df is not None:
            for ix, row in df.iterrows():
                date = datetime.strptime(row.trade_date,'%Y%m%d')
                bar = BarData(
                    symbol=symbol,
                    exchange=exchange,
                    interval=interval,
                    datetime=date,
                    open_price=row["open"],
                    high_price=row["high"],
                    low_price=row["low"],
                    close_price=row["close"],
                    volume=row["amount"],
                    gateway_name="TU"
                )
                print(bar)
                data.append(bar)
        return data
# print("TUQUERY_MAIN_CW")
tusharedata = TushareData()