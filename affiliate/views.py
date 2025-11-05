from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from affiliate.models import AffiliateLinks
from django.contrib import messages

def dashboard(request):
    if request.method == "POST":
        id = request.POST.get('product')
        selected_post = Post.objects.get(id=id)
        name = request.POST.get('name')
        affiliate_link = AffiliateLinks.objects.create(product=selected_post, author_id=request.user, name=name)
        messages.success(request, 'Affiliate link created successfully!')
        

    if request.user.is_authenticated:
        user_posts = Post.objects.filter(author_id=request.user).order_by('-date_listed')
        return render(request, 'home.html', {'title': 'Affiliate Dashboard', 'posts': user_posts})
    else:
        return redirect('login')



def list(request):
    if request.user.is_authenticated:
        user_affiliate_links = AffiliateLinks.objects.filter(author_id=request.user).order_by('-date_listed')
        return render(request, 'list.html', {
        'title': 'My Affiliate Products',
        'affiliate_links': user_affiliate_links
    })
    else:
        return redirect('login')

def promote(request, affiliate_id): 
    
    affiliate_link = get_object_or_404(AffiliateLinks, unique_id=affiliate_id)
    if affiliate_link.author_id != request.user:
        affiliate_link.clicks_count += 1
        affiliate_link.save()
    product = affiliate_link.product
    return render(request, 'affiliate_view.html',{
            'title': 'Promote Product',
            'affiliate_link': affiliate_link,
            'product_title': product.title,
            'product_content': product.content,
        })
