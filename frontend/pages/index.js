import React, { useState } from 'react';
import Head from 'next/head';
import {
  Heading,
  Flex,
  Stack,
  Box,
  Spacer,
  Text,
} from '@chakra-ui/react';

import Container from '../components/Container';
import { getPosts } from '../lib/getPosts';
import BlogPost from '../components/BlogPost';

import { ChevronLeft, ChevronRight } from 'lucide-react';

export default function Blog({ posts }) {
  const BlogPosts = posts['items'];
  const totalItems = posts['total'];
  const pageSize = 50;
  const TotalPages = Math.trunc(totalItems / pageSize);
  const ListPages = [...Array(TotalPages + 1).keys()];

  return (
    <>
      <Head>
        <title>ABlogsys - FastAPI and Next.js</title>
      </Head>
      <Container>
        <Stack
          as="main"
          gap={8}
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

              <Flex align="center" width="100%" pt={8}>
                <Box>
                  <ChevronLeft size={24} color="red" />
                </Box>
                <Spacer />
                <Box>
                <Text
                  fontSize="sm"
                  color="gray.500"
                  minWidth="100px"
                  align="center"
                >
                  {ListPages.join(', ')}
                </Text>
                </Box>
                <Spacer />
                <Box>
                  <ChevronRight size={24} color="red" />
                </Box>

              </Flex>

          </Flex>
        </Stack>
      </Container>
    </>
  );
}

export async function getStaticProps() {
  const posts = await getPosts(`${process.env.BACKEND_URI}/posts?page=1&size=50`);
  return { props: { posts } };
}
