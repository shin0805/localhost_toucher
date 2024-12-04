def onHTTPRequest(webServerDAT, request, response):
  response['statusCode'] = 200  # OK
  response['statusReason'] = 'OK'
  choptos = [op("chopto1"), op("chopto2"), op("chopto3"), op("chopto4"), op("chopto5")]
  response['statusReason'] = 'OK'
  response['data'] = '<b>TouchDesigner: </b>'
  nums = []
  for i in range(5):
    nums = nums + [choptos[i].rows()[0][0]]
    response['data'] += ", " + str(nums[i])

  return response
