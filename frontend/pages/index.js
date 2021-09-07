import React, { useState } from 'react';
import Head from 'next/head';
import NextLink from "next/link";
import {
  Heading,
  Flex,
  Center,
  Stack,
  Box,
  Input,
  InputGroup,
  InputRightElement,
  Button,
  HStack,
  Spacer,
  Icon,
  Text,
} from '@chakra-ui/react';

import Container from '../components/Container';
import { getPosts, getAllPosts } from '../lib/getPosts';
import BlogPost from '../components/BlogPost';

import { ArrowBackIcon, ArrowForwardIcon } from '@chakra-ui/icons';

export default function Blog({ posts }) {
  const BlogPosts = posts['items'];
  console.log(posts['total']);
  const totalItems = posts['total'];
  const pageSize = 50;
  const TotalPages = Math.trunc(totalItems / pageSize);
  const ListPages = [...Array(TotalPages + 1).keys()];
  console.log(ListPages);
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
              Blog ({posts['total']} posts)
            </Heading>
            {BlogPosts.map((frontMatter) => (
              <BlogPost key={frontMatter.title} {...frontMatter} />
            ))}

              <Flex>
                <Box>
                <ArrowBackIcon w={6} h={6} color="red.500" />
                </Box>
                <Spacer />
                <Box px={200}>
                <Text
                  fontSize="sm"
                  color="gray.500"
                  minWidth="100px"
                  align="center"
                >
                  {ListPages}
                </Text>
                </Box>
                <Box px={100}>
                <ArrowForwardIcon w={6} h={6} color="red.500" />

                </Box>

              </Flex>

          </Flex>
        </Stack>
      </Container>
    </>
  );
}

export async function getStaticProps() {
  const posts = await getPosts('http://backend:8000/posts?page=0&size=50');

  return { props: { posts } };
}
