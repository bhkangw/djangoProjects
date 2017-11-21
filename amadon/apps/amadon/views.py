from django.shortcuts import render, redirect

items = [{
    "id": 101,
    "name": "Dojo T-Shirt",
    "price": 19.99,
}, {
    "id": 102,
    "name": "Dojo Sweatshirt",
    "price": 29.99
}, {
    "id": 103,
    "name": "Dojo Mug",
    "price": 9.99
}, {
    "id": 104,
    "name": "Dojo Keychain",
    "price": 4.99
}]

def index(request):
    # # clear out last_transaction from session, so as not to make it seem like we are
    # # charging user multiple times when they view this page
    # if "last_transaction" in request.session.keys():
    #     del request.session['last_transaction']
    context = {"items": items}
    return render(request, 'amadon/index.html', context)

def buy(request, item_id):
    # go through items and check which item_id the URL matches to in the items list
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])
    # handle exceptions for session keys if they do not yet exist
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0
    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')
