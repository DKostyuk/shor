from django.shortcuts import render, redirect
from .forms import *
from products.models import *

import random


def another(request):
    tricks_all = AnotherTrick.objects.filter(is_active=True)
    name = "DimaKostyuk"
    current_day = "24.04.2018"
    form = TestEditorForm()

    return render(request, 'another/another.html', locals())


def card_decks():
    cards = {
        "2_1": 2, "2_2": 2, "2_3": 2, "2_4": 2,
        "3_1": 3, "3_2": 3, "3_3": 2, "3_4": 3,
        "4_1": 4, "4_2": 4, "4_3": 4, "4_4": 4,
        "5_1": 5, "5_2": 5, "5_3": 5, "5_4": 5,
        "6_1": 6, "6_2": 6, "6_3": 6, "6_4": 6,
        "7_1": 7, "7_2": 7, "7_3": 7, "7_4": 7,
        "8_1": 8, "8_2": 8, "8_3": 8, "8_4": 8,
        "9_1": 9, "9_2": 9, "9_3": 9, "9_4": 9,
        "10_1": 10, "10_2": 10, "10_3": 10, "10_4": 10,
        "B_1": 10, "B_2": 10, "B_3": 10, "B_4": 10,
        "D_1": 10, "D_2": 10, "D_3": 10, "D_4": 10,
        "K_1": 10, "K_2": 10, "K_3": 10, "K_4": 10,
        "A_1": 11, "A_2": 11, "A_3": 11, "A_4": 11
    }
    deck = 7
    cards_full = {}
    for key, value in cards.items():
        for i in range(1, deck+1):
            new_key = str(i)+'_'+key
            cards_full[new_key] = value
    #         print(cards_full)
    # len(cards_full)
    return cards_full


# Initial deal
def first_deal(cards):
    player_list = []
    dealer_list = []
    for i in range(2):
        player_card = random.choice(list(cards.keys()))
        player_list.append(cards[player_card])
        del cards[player_card]
        dealer_card = random.choice(list(cards.keys()))
        dealer_list.append(cards[dealer_card])
        del cards[dealer_card]
    return cards, player_list, dealer_list


def totals(player_list, dealer_list):
    player_interim_totals = 0
    dealer_interim_totals = 0
    for i in player_list:
        player_interim_totals += i
    for i in dealer_list:
        dealer_interim_totals += i
    return player_interim_totals, dealer_interim_totals


def check_first_totals(player_first_totals, dealer_first_totals):
    if dealer_first_totals == 21:
        next_step = 7  # stop game, dealer win
    elif player_first_totals == 21 and dealer_first_totals < 21:
        next_step = 6  # stop game, player win
    else:
        next_step = 0
    return next_step


def deal(cards, current_list):
    current_card = random.choice(list(cards.keys()))
    current_list.append(cards[current_card])
    del cards[current_card]
    return cards, current_list


def check_player_totals(player_totals):
    if player_totals > 21:
        next_step = 7  # stop game, dealer win
    elif player_totals == 21:
        next_step = 999  # player stop, dealer turn to play
    else:
        next_step = 0
    return next_step


def check_dealer_totals(dealer_totals):
    if dealer_totals > 21:
        next_step = 6  # stop game, player win
    elif dealer_totals == 21:
        next_step = 7  # player stop, dealer win
    else:
        next_step = 0
    return next_step


        # else:
    #     if player_interim_totals == 21 and dealer_interim_totals > 21:
    #         next_step = 6  # stop game, player win
    #     elif player_interim_totals == 21 and dealer_interim_totals == 21:
    #         next_step = 7  # stop game, dealer win
    #     elif player_interim_totals == 21 and dealer_interim_totals < 21:
    #         next_step = 5  # player stop, dealer turn to play
    #     elif player_interim_totals > 21:
    #         next_step = 7  # stop game, dealer win
    #     elif player_interim_totals < 21 and
    #


def trick_item(request, slug=None):
    trick = AnotherTrick.objects.get(slug=slug, is_active=True)
    url_name = slug.replace('-', '_')
    if slug == "file-upload-regular-user":
        form = ProductFileCSVForm()
        print('9999', form)
        if request.method == 'POST':
            form = ProductFileCSVForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('another')
        else:
            form = ProductFileCSVForm()
    if slug == "crm":
        print()
        products_all = Product.objects.filter(is_active=True)
    if slug == "black-jack":
        black_jack = 21
        if request.method == 'POST':
            next_step = 0
            if request.POST.get('start', '') == "start":
            # form = ProductFileCSVForm(request.POST, request.FILES)
                cards_start = card_decks().copy()
                cards, player_list, dealer_list = first_deal(cards_start)
                player_totals, dealer_totals = totals(player_list, dealer_list)
                print(player_list)
                print(dealer_list)
                print(player_totals)
                print(dealer_totals)
                next_step = check_first_totals(player_totals, dealer_totals)
                print("after first deal  ", next_step)
                if next_step == 7:
                    result_message = 'DEALER WIN'
                    return render(request, 'another/' + url_name + '.html', locals())
                elif next_step == 6:
                    result_message = 'PLAYER WIN'
                    return render(request, 'another/' + url_name + '.html', locals())
                else:
                    return render(request, 'another/' + url_name + '.html', locals())
            while next_step != 999:
                if request.POST.get('hit', '') == "hit":
                    cards, player_list = deal(cards, player_list)
                    player_totals, dealer_totals = totals(player_list, dealer_list)
                    next_step = check_player_totals(player_totals)
                    print(player_totals)
                elif request.POST.get('stop', '') == "stop":
                    next_step = 999
            next_step = 0
            while next_step != 999:
                cards, dealer_list = deal(cards, dealer_list)
                player_totals, dealer_totals = totals(player_list, dealer_list)
                next_step = check_dealer_totals(dealer_totals)
    return render(request, 'another/' + url_name + '.html', locals())


def crm_product_item(request, slug=None):
    products_all = Product.objects.filter(is_active=True)
    # trick = AnotherTrick.objects.get(slug=slug, is_active=True)
    # url_name = slug2.replace('-', '_')
    if slug:
        product = Product.objects.get(slug=slug)
    #     form = ProductFileCSVForm()
    #     print('9999', form)
        if request.method == 'POST':
    #         form = ProductFileCSVForm(request.POST, request.FILES)
            print(9999999)
        if request.method == 'GET':
            print(3333333)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('another')
    #     else:
    #         form = ProductFileCSVForm()
        return render(request, 'another/crm_product_item.html', locals())
    return render(request, 'another/crm_product.html', locals())
