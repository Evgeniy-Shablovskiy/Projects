import re


def search_post(s, posts):
    list_of_matches = []
    s = re.split('[,|!|#|«|»| – |\\.\\.\\.| \\.\\.\\. |\\.|:|\\?| ]+', s.lower())
    s = [word for word in s if word]
    if not s:
        return []
    for post in posts:
        describe = re.split('[,|!|#|«|»| – |\\.\\.\\.| \\.\\.\\. |\\.|:|\\?| ]+', post.get("content").lower())
        result = 0
        for word in s:
            if len(word) >= 1 and word in describe:
                result += describe.count(word)
        if result > 0:
            list_of_matches.append({'pk': post['pk'], 'count': result})
    return list_of_matches


def sort_(list_of_matches):
    sort_list = []
    for post in list_of_matches:
        if post.get('count') > 0:
            sort_list.append(post)
    sort_list.sort(key=lambda x: x['count'], reverse=True)
    return sort_list


def top(sort_list, posts):
    list_ = []
    for sorted_post in sort_list:
        for post in posts:
            if sorted_post['pk'] == post['pk']:
                list_.append(post)
                break
    return list_
