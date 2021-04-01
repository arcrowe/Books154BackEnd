import os
from datetime import datetime

import pandas as pd
import pandas_datareader.data as web
from django.http import HttpResponse

IEX_KEY = os.environ.get('IEXCLOUD_KEY')


# Create your views here.
def getData(request):
    global out
    start_date = request.GET.get("startdate", "")
    end_date = request.GET.get("enddate", "")
    comptemp = request.GET.get("companies", "")
    pctChange = request.GET.get("pctChange", "")
    companies = comptemp.split(',')
    if len(start_date) == 0:
        return HttpResponse("none")

    # company = 'CVX'
    # start_date = '2021-01-21'
    # end_date = '2021-02-03'
    start = datetime.strptime(start_date, '%Y-%m-%d')

    end = datetime.strptime(end_date, '%Y-%m-%d')
    count = 1
    for company in companies:
        df = web.DataReader(company, 'iex', start, end, api_key=IEX_KEY)
        df['date'] = df.index
        df.reset_index(drop=True, inplace=True)
        new = df[['date', 'close']]
        new = new.rename(columns={'close': company})
        # new.columns = ['DATE', company]
        new = new.T
        # print(f'new :  ${new}')
        if count == 1:
            out = new.copy()
        else:
            out = out.append(new.iloc[[1]])
        count += 1

    if pctChange == 'true':
        date = out.iloc[[0]]
        out = out.iloc[1:, :].T.apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100)).T
        out = pd.concat([date, out])
    # print(f'out ${out}')
    out = out.to_json(orient='split')
    return HttpResponse(out)
