
GET /_cat/indices
{}


GET /reptile_v1/_mapping
{

}

GET /reptile/_search
{
    "query":{
      "match_phrase": {
        "author":"贴吧用户: 灿撂谮"
      }
    }
}

POST  /reptile/_delete_by_query
{
    "query":{
      "match_phrase": {
        "author": "贴吧用户: 黄老师🌻🌺🌻🍁"
      }
    }
}


POST  /reptile/_delete_by_query
{
    "query":{
      "match_phrase": {
        "author": "贴吧用户: 灿撂谮"
      }
    }
}


POST hotel_base_info/doc/_update_by_query
{
  "query": {
    "bool": {
      "must": [
        {
          "terms": {
            "stationId": [
              "5114230006",
              "5114230202",
              "5114239626",
              "5114239391",
              "5114239733",
              "5114239412",
              "5114239475",
              "5114239458",
              "5114239739",
              "5114239508",
              "5114239525",
              "5114239510",
              "5114239562",
              "5114230031",
              "5114239586",
              "5114239625",
              "5114239585",
              "5114239521",
              "5114239631",
              "5114239523",
              "5114239640",
              "5114239637",
              "5114239465",
              "5114239742",
              "5114239520",
              "5114239572"
            ]
          }
        }
      ]
    }
  },
  "script":{
    "source": "ctx._source.isFocus=true",
    "lang": "painless"
  }
}


GET /hotel_base_info/_count