import React, { useState } from "react";
import Head from "next/head";
import {
  useColorMode,
  Heading,
  Text,
  Flex,
  Stack,
  Avatar,
} from "@chakra-ui/react";
import hydrate from "next-mdx-remote/hydrate";

import { getAllPosts, getPostBySlug, getPosts } from "../lib/getPosts";
import MDXComponents from "../components/MDXComponents";
import Container from "../components/Container";
import { formatDate } from "../lib/formatDate";


export default function Blog({mdxSource, frontMatter }) {

  const content = hydrate(mdxSource, {
    components: MDXComponents,
  });
  const { colorMode } = useColorMode();
  const textColor = {
    light: "gray.700",
    dark: "gray.400",
  };
  const slug = frontMatter.slug;
  const user = frontMatter.user

  return (
    <Container>
      <Head>
        <title>{slug} - Blog - {user}</title>
      </Head>
      <Stack
        as="article"
        spacing={8}
        justifyContent="center"
        alignItems="flex-start"
        m="0 auto 4rem auto"
        maxWidth="700px"
        w="100%"
        px={2}
      >
        <Flex
          flexDirection="column"
          justifyContent="flex-start"
          alignItems="flex-start"
          maxWidth="700px"
          w="100%"
        >
          <Heading letterSpacing="tight" mb={2} as="h1" size="xl">
            {frontMatter.title}
          </Heading>
          <Flex
            justify="space-between"
            align={["initial", "center"]}
            direction={["column", "row"]}
            mt={2}
            w="100%"
            mb={4}
          >
            <Flex align="center">
              <Avatar
                size="xs"
                name={frontMatter.user}
                // src="../images/portrait.jpeg"
                mr={2}
              />
              <Text fontSize="sm" color={textColor[colorMode]}>
                {frontMatter.user}
                {" / "}
                {formatDate(frontMatter.published_at)}
              </Text>
            </Flex>
            <Text fontSize="sm" color="gray.500" minWidth="100px" mt={[2, 0]}>
              {frontMatter.readingTime.text}
            </Text>
          </Flex>

        </Flex>
        {content}
      </Stack>
    </Container>
  );
}

export async function getStaticPaths() {
  const data = await getAllPosts();

  return {
    paths: data.map((p) => ({
      params: {
        slug: p["slug"],
      },
    })),
    fallback: false,
  };
}

export async function getStaticProps({ params }) {
  const post = await getPostBySlug(params.slug);

  return { props: post }
}
