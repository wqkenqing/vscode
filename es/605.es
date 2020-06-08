
GET /_cat/indices

GET /tourist_minute_local_data/_search
{
 "from":0,
 "size":2   
}

GET /tourist_minute_local_data/_search
{
  "query":{
    "match_phrase":{
      "id":"2830030_0_201912201620_minute"
    }
  }
}


GET /tourist_minute_local_data/_search
{
    "query": {
        "bool": {
            "filter": {
                "range": {
                    "time": {
                        "gte": "2019-12-20"
                    }
                }
            }
        }
    },
    "aggs": {
        "num_count": {
            "terms": {
                "field": "scenicName"
            }
        }
    }
}

PUT  /tourist_minute_local_data/_mapping/_doc
{
    "properties": {
    "scenicName": { 
      "type":     "text",
      "fielddata": true
    }
  }
}

GET /_cat/indices