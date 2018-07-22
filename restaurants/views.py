from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "my_list": [
            {
                "restaurant_name":"The Bowl",
                "food_type":"Healthy",
            },
            {
                "restaurant_name":"Al Makan",
                "food_type":"Korean",
            },
            {
                "restaurant_name":"Solo",
                "food_type":"Pizza",
            },
        ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {
        "my_object": {
            "restaurant_name":"Solo",
            "food_type":"Pizza",
        },
    }
    return render(request, 'detail.html', context)
