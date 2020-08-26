get /_cat/indices


GET /reptile_new1/_search
{
    "query": {
        "match_all": {}
    },
    "size": -1
}

GET /hy_gather_weather/_search
{
    "query": {
        "match_none": {}
    }
}

GET /reptile_new1/_mapping

GET /reptile_new1/_search
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "title": "保险"
                    }
                },
                {
                    "match": {
                        "author": "迷恋_墨染锦年"
                    }
                }
            ]
        }
    }
}

GET /reptile_new1/_search
{
    "query": {
        "match": {
            "title": {
                "query": "保险 祖父",
                "operator": "or"
            }
        }
    }
}

GET /reptile_new1/_search
{
    "query": {
        "match": {
            "title": {
                "query": "小伙 走",
                "minimum_should_match": 3
            }
        }
    },
    "size": -1
}


GET /reptile_new1/_search
{
    "query": {
        "match_phrase": {
            "title": "小伙走"
        }
    }
}
GET /reptile_new1/_search
{
    "query": {
        "match_phrase": {
            "title": {
                "query": "小伙进",
                "slop": 1
            }
        }
    }
}



GET /reptile_new1/_search
{
    "query": {
        "match_phrase_prefix": {
            "content": {
                "query": "you"
            }
        }
    }
}
GET /reptile_new1/_search
1{
    "query": {
        "multi_match": {
            "query": "小伙 洪雅",
            "fields": [
                "title",
                "content"
            ]
        }
    }
}