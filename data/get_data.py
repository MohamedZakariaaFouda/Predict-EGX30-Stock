import investpy

data = investpy.indices.get_index_historical_data(
    index='EGX 30',
    country='egypt',
    from_date='12/01/2021',
    to_date='12/01/2025'
)
data.to_csv('data/EGX30.csv', index=False)