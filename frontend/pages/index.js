import React, { useState } from "react";
import Head from "next/head";
import {
  Heading,
  Flex,
  Stack,
  Input,
  InputGroup,
  InputRightElement,
} from "@chakra-ui/react";

import Container from "../components/Container";
import { getPosts } from "../lib/getPosts";
import BlogPost from "../components/BlogPost";

import { SearchIcon } from "@chakra-ui/icons";

export default function Blog({ posts }) {
  // const [searchValue, setSearchValue] = useState("");

  const BlogPosts = posts
  //   .sort(
  //     (a, b) =>
  //       Number(new Date(b.published_at)) - Number(new Date(a.published_at))
  //   )
  //   .filter((frontMatter) =>
  //     frontMatter.title.toLowerCase().includes(searchValue.toLowerCase())
  //   );

  return (
    <>
      <Head>
        <title>ABlogsys - FastAPI and Next.js</title>
      </Head>
      <Container>
        <Stack
          as="main"
          spacing={8}
          justifyContent="center"
          alignItems="flex-start"
          m="0 auto 4rem auto"
          maxWidth="700px"
        >
          <Flex
            flexDirection="column"
            justifyContent="flex-start"
            alignItems="flex-start"
            maxWidth="700px"
            px={4}
          >
            <Heading letterSpacing="tight" mb={4} as="h1" size="xl">
              Blog ({posts.length} posts)
            </Heading>
            {BlogPosts.map((frontMatter) => (
              <BlogPost key={frontMatter.title} {...frontMatter} />
            ))}
          </Flex>
        </Stack>
      </Container>
    </>
  );
}

export async function getStaticProps() {
  const posts = await getPosts("http://backend:8000/posts?page=0&size=50");
  return { props: { posts } };
}
