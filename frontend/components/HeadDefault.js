import Head from 'next/head'

const HeadDefault = () => {
  return (
    <div>
      <Head>
        <title>A blog system based on the FastAPI and Next.js</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
    </div>
  );
};

export default HeadDefault;