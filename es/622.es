

GET /county_industry_consumption/_search
{
    "query":{
        "bool":{
            "range":{
                "dealDay":{
                    "gte":"2"
                }
            }
        }

    }
}