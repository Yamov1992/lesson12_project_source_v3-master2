import json


def load_posts(path='posts.json'):
    posts = []
    with open(path, 'r', encoding='UTF-8') as file:
        posts = json.load(file)
    return posts


def search_post(substr):
    posts_found = []
    post_json = load_posts()
    for post in post_json:
        if substr in post['content']:
            posts_found.append(post)

    return posts_found


def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]
    if filetype not in ['jpg', 'svg', 'jpeg', 'png']:
        return

    picture.save(f'./uploads/images/{filename}')
    return f'uploads/images/{filename}'


def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_posts_to_json(posts)


def save_posts_to_json(posts, path='posts.json'):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(posts, file, ensure_ascii=False)