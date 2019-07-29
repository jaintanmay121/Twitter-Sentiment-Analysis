import urllib.request as req
import bs4

def mineTweets(userName):
    r=req.urlopen('https://twitter.com/'+userName)
    p=bs4.BeautifulSoup(r,"html.parser")

    a=p.find('ol',class_='stream-items js-navigable-stream')
    post_id=[]
    b=a.find_all('li')
    for i in b:
        try:
            post_id.append(i['data-item-id'])
        except:
            pass

    list_of_comments=[]
    for i in post_id:
        resp=req.urlopen('https://twitter.com/'+userName+'/status/'+i)
        page=bs4.BeautifulSoup(resp"html.parser")

        a=page.find_all('li',class_='js-stream-item stream-item stream-item')
        n=1

        for i in a:
            b=i.find('div',class_='content')
            c=b.find('div',class_='js-tweet-text-container')
            comments=b.p.text
            if len(comments)>3 and comments.find('.com')==-1 :
                list_of_comments.append(comments)
            
    return list_of_comments