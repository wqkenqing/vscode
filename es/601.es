## 游客城市来源.
GET /tourist_source_city/doc/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "time": {
              "gte": "2020-06-01"
            }
          }
        },
        {
          "term": {
            "flag": {
              "value": "day"
            }

          }
        }
      ]
    }
  }
}


GET /tourist_source_city/doc/_search
{
  "query": {
    "bool": {
      "must": [
      {
          "range": {
            "time": {
              "gte": "2020-06-01"
            }
          }
        },
        {
          "term": {
            "countryName": {
              "value": "中国"
            }

          }
        }
      ]
    }
  }
}

## 国家来源地
GET /tourist_source_country/doc/_search
{
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "time": {
                            "gte": "2020-05-20"
                        }
                    }
                },
                {
                    "term": {
                        "countryName": {
                            "value": "德国"
                        }
                    }
                }
            ]
        }
    }
}

## 游客入住
GET /hotel_checkin_record/doc/_search
{
  "query": {
    "bool": {
      "must": [
    
          {
           "term": {
            "countryName": {
              "value": ""
            }

          }
        }
      ]
    }
  }
}

## 游客
GET /hotel_checkin_record/doc/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "createTime": {
              "gte": "2020-06-01 00:00:00"
            }
          }
        }
      ]
    }
  }
}


## 操作日志
GET /operation_record/_search
{
  
  "sort": [
    {
      "eventTime": {
        "order": "desc"
      }
    }
  ]
  , "size": 20
}