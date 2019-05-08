import quandl


def import_quandl_futures(quandl_code):

    # Parse the Quandl API Key from a local file
    my_quandl_key = open("quandlapikey.txt", "r").read()
    quandl.ApiConfig.api_key = my_quandl_key

    # Query continuous futures data from the Quandl API
    df = quandl.get(quandl_code)

    # Preprocess the pandas DataFrame to accommodate backtrader PandasData feed
    df.rename(columns={
        'Settle': 'Close',
        'Prev. Day Open Interest': 'OpenInterest'},
        inplace=True)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']]

    return df
