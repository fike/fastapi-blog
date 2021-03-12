import React, { useState, useEffect } from 'react';
const url = 'http://localhost:8000/posts?page=0&size=50';

const ListPostsData = () => {
  const [posts, setPosts] = useState([]);

  const getPosts = async () => {
    const response = await fetch(url);
    const posts_raw = await response.json();
    const posts = posts_raw['items']
    setPosts(posts);
  };

  useEffect(() => {
    getPosts();
  }, []);
  return (
    <>
      <div>
      {/* <div>github users</div> */}
      <div className="max-w-screen-md mx-auto align-middle flex items-center flex-wrap p-3">
        {posts.map((post) => {
          const { id, title, body, slug, published, author_id } = post;
          return (
            <div key={id} className="max-w-screen-md mx-auto align-middle flex items-center flex-wrap p-3">
            {/* <div key=> */}
              <div> 
              <a href={slug}>
              <p className="text-xl font-bold">{title}</p>
              </a>
              </div>
              <div>
                <div className="text-md">
                <a href={slug}>
                <article className="prose lg:prose">{body}</article>
                </a>
                </div>
              </div>
            </div>
          );
        })}
      </div>
      </div>
    </>
  );
};

export default ListPostsData;