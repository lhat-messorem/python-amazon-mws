from mws import mws

abc = mws.MWS(access_key='AKIAIMJD6TQYTB5IUEMQ', secret_key='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', account_id='A10KER2CNUDHJL', auth_token='amzn.mws.5eacda7c-15c0-33c7-5c81-5fcb167d8949')
abc.enumerate_param_obj('FeesEstimateRequestList.FeesEstimateRequest.', [{'MarketplaceId': 'ATVPDKIKX0DER', 'IdType': 'ASIN', 'IdValue': 'B002KT3XQM',\
'IsAmazonFulfilled': True, 'Identifier': 'randomstring',\
'PriceToEstimateFees.ListingPrice.CurrencyCode': 'USD',\
'PriceToEstimateFees.ListingPrice.Amount': '30.00',\
'PriceToEstimateFees.Shipping.CurrencyCode': 'USD',\
'PriceToEstimateFees.Shipping.Amount': '3.99',\
'PriceToEstimateFees.Points.PointsNumber': '0'},])


from mws import mws
abc = mws.Products(access_key='AKIAIMJD6TQYTB5IUEMQ', secret_key='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', account_id='A10KER2CNUDHJL', auth_token='amzn.mws.5eacda7c-15c0-33c7-5c81-5fcb167d8949')

a = abc.get_my_fees_estimate([{'MarketplaceId': 'ATVPDKIKX0DER', 'IdType': 'ASIN', 'IdValue': 'B002KT3XQM',\
'IsAmazonFulfilled': 'true', 'Identifier': 'randomstring',\
'PriceToEstimateFees.ListingPrice.CurrencyCode': 'USD',\
'PriceToEstimateFees.ListingPrice.Amount': '30.00',\
'PriceToEstimateFees.Shipping.CurrencyCode': 'USD',\
'PriceToEstimateFees.Shipping.Amount': '3.99',\
'PriceToEstimateFees.Points.PointsNumber': '0',},])

a.parsed.get('FeesEstimateResultList', {}).get('FeesEstimateResult', {}).get('FeesEstimate', {}).get('TotalFeesEstimate', {}).get('Amount', {}).get('value')