from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Card

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def card_list(request):
    list_of_current_cards = Card.objects.all()
    return render(request, "cards/debug_card_list.html", {"list_of_current_cards": list_of_current_cards})

def card_render(request, card_hash_id):
    card = get_object_or_404(Card, card_hash_id=card_hash_id)
    return render(request, "cards/card_template.html", context={"card": card})
