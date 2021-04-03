import React from "react";
import NextLink from "next/link";
import { useColorMode, Heading, Text, Flex, Box, Link } from "@chakra-ui/react";
import { formatDate } from "../lib/formatDate";

const BlogPost = ({ title, published_at, summary, slug }) => {
  const { colorMode } = useColorMode();
  const secondaryTextColor = {
    light: "gray.700",
    dark: "gray.400",
  };

  return (
    <NextLink href={`/${slug}`} passHref>
      <Link w="100%" _hover={{ textDecoration: "none" }}>
        <Box mb={10} display="block" width="100%">
          <Flex
            width="100%"
            align="flex-start"
            justifyContent="space-between"
            flexDirection={["column", "row"]}
          >
            <Flex
              flexDirection="column"
              align="flex-start"
              justifyContent="start"
              width="100%"
            >
              <Heading size="md" as="h3" mb={1} fontWeight="medium">
                {title}
              </Heading>
            </Flex>

            <Text
              color="gray.500"
              minWidth="140px"
              textAlign={["left", "right"]}
              mb={[4, 0]}
            >
              {formatDate(published_at)}
            </Text>
          </Flex>
          <Text color={secondaryTextColor[colorMode]}>{summary}</Text>
        </Box>
      </Link>
    </NextLink>
  );
};

export default BlogPost;
