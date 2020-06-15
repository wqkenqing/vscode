PUT /lib3
{
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 0
    },
    "mappings": {
        "user": {
            "properties": {
                "name": {
                    "type": "text"
                },
                "address": {
                    "type": "text"
                },
                "age": {
                    "type": "integer"
                },
                "interests": {
                    "type": "text"
                },
                "birthday": {
                    "type": "date"
                }
            }
        }
    }
}


GET /_cat/indices


GET /hy_gather_weather/_search

GET /hy_gather_weather/_search
{
  "query": {
    "bool": {
      "must": [
        {"range": {
          "gatherTime": {
            "gte": "2020-02-15 10:42:00"
          }
        }}
      ]
    }
  }
}