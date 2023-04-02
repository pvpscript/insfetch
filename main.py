import sys

from post_page_parser import PostPageParser
from post_handler import PostHandler

if __name__ == '__main__':
    post_id = sys.argv[1]

    post_page_parser = PostPageParser()
    post_handler = PostHandler(post_id=post_id,
                               post_page_parser=post_page_parser)

    print(post_handler.article_body())
    print(post_handler.author_username())
    print(post_handler.author_name())
    print(post_handler.author_image())

    image_data = post_handler.image
    print(image_data.quantity())
    print(image_data.dimensions(0))
    print(image_data.url(0))
