import fetch from "isomorphic-fetch"
import { serialize } from 'next-mdx-remote/serialize'
import readingTime from 'reading-time'

import remarkGfm from 'remark-gfm'
import rehypeSlug from 'rehype-slug'
import rehypeAutolinkHeadings from 'rehype-autolink-headings'
import rehypePrismPlus from 'rehype-prism-plus'

const ITEMS_PAGE = 20


export async function getPosts() {
  const response = await fetch(`${process.env.BACKEND_URI}/posts?page=1&size=50`);
  const respJson = await response.json();
  const posts = respJson;

  return posts;
}

export async function getAllPosts() {

  const pageSize = 50
  const response = await fetch(`${process.env.BACKEND_URI}/posts?page=1&size=1`)
  const respJson = await response.json()
  const totalItems = respJson['total']
  const totalPages = Math.ceil(totalItems / pageSize)

  const allPosts = []

  for (let page = 1; page <= totalPages; page++) {
    const responsePosts = await fetch(`${process.env.BACKEND_URI}/posts?page=${page}&size=${pageSize}`);
    const respPostsJson = await responsePosts.json();
    const posts = respPostsJson['items']
    posts.forEach(element => allPosts.push(element));
  }

  return allPosts
}

export async function getPostBySlug(slug) {
  const data = {}
  const response_slug = await fetch(`${process.env.BACKEND_URI}/posts/${slug}`);
  const RespJsonSlug = await response_slug.json();

  data['title'] = RespJsonSlug['title']
  data['summary'] = RespJsonSlug['summary']
  data['published_at'] = RespJsonSlug['published_at']
  const content = RespJsonSlug['body']

  const response_user = await fetch(`${process.env.BACKEND_URI}/users/user?user_id=${RespJsonSlug['author_id']}`);
  const RespJsonUser = await response_user.json()
  data['user'] = RespJsonUser['username']

  const mdxSource = await serialize(content, {
    mdxOptions: {
      remarkPlugins: [remarkGfm],
      rehypePlugins: [
        rehypeSlug,
        [rehypeAutolinkHeadings, { behavior: 'wrap' }],
        [rehypePrismPlus, { ignoreMissing: true }]
      ],
      format: 'mdx'
    }
  })

  return {
    mdxSource,
    frontMatter: {
      wordCount: content.split(/\+s/gu).length,
      readingTime: readingTime(content),
      slug: slug || null,
      ...data
    }
  };

}
