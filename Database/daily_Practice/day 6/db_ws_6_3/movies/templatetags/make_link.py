from django import template

register = template.Library()

# custom filter 만들기 
@register.filter
def hashtag_link(word):
    # 공백까지 인식할 수 있게 해야함  
    content = word.content + ' '
    hashtags = word.hashtags.all()
    # hashtag를 한개씩 목록을 돌면서 찾는다
    for hashtag in hashtags:
        content = content.replace(hashtag.content+' ', f'<a href="/movies/{hashtag.pk}/hashtag/">{hashtag.content}</a> ')
    return content