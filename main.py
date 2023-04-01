import sys

from post_page_parser import PostPageParser
from post import Post

if __name__ == '__main__':
    post_id = sys.argv[1]

    post_page_parser = PostPageParser()
    post = Post(post_id=post_id, post_page_parser=post_page_parser)

    print(post.fetch_post())
