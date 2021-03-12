import Link from "next/link";
import HeadDefault from "../components/HeadDefault";
import { Navbar } from "../components/NavBar";
import ListPostsData from "../components/Posts";


export default function Home({posts}) {
  return (
    <div className="bg-gray-50">
      <HeadDefault />
      <Navbar />
      <div className="max-w-screen-md mx-auto flex p-3">
      <ListPostsData />
      </div>
    <style global jsx>{`
      html,
      body,
      body > div:first-child,
      div#__next,
      div#__next > div {
        height: 100%;
      }
    `}</style>
    </div>
  )
}

export async function getStaticProps() {
  const res = await fetch('http://backend:8000/posts?page=0&size=3')
  const raw_posts = await res.json()
  const posts = raw_posts['items']
  console.log(posts)
  return {
    props: {
      posts,
    },
  }
}

// function Content({ posts }) {
//   return (
//     <ul>
//       {posts.map((post) => (
//         <div key={post.id}>{post.title}</div>
//       ))}
//     </ul>
//   );
// }

// export async function getStaticProps() {
//   const res = await fetch("http://backend:8000/posts?page=0&size=3");
//   const raw_posts = await res.json();
//   const posts = raw_posts["items"];
//   console.log(posts);
//   return {
//     props: {
//       posts,
//     },
//   };
// }

// export default Content;
