import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'

function GetPosts({ posts }) {
  return(
    <div className={styles.container}>
      <Head>
        <title>FastAPI + NextJS blog engine</title>
        <link rel="icon" href="/favicon.icon" />
      </Head>
      <div className={styles.main}>
        <h1 className={styles.title}>
          A blog project using FastAPI and NextJS!
        </h1>

        <p className={styles.description}>
          These are amazing posts!
        </p>
        <ul>
            This is a { posts }
        </ul>
      </div>
    </div>
  )
}

export async function getStaticProps() {
  const res = await fetch("http://backend:8000/posts?page=0&size=2")
  const json = await res.json()

  return {
    props: {
      posts: json.items
    },
  }
}

export default GetPosts