import {
  Box,
  Alert,
  Code,
  Heading,
  Link,
  Text,
  Separator,
} from "@chakra-ui/react";
import { useColorMode } from "./ui/color-mode";
import NextLink from "next/link";

const CustomLink = (props) => {
  const { colorMode } = useColorMode();
  const color = {
    light: "blue.500",
    dark: "blue.500",
  };

  const href = props.href;
  const isInternalLink = href && (href.startsWith("/") || href.startsWith("#"));

  if (isInternalLink) {
    return (
      <NextLink href={href} passHref legacyBehavior>
        <Link color={color[colorMode]} {...props} />
      </NextLink>
    );
  }

  return <Link color={color[colorMode]} target="_blank" rel="noopener noreferrer" {...props} />;
};

const Quote = (props) => {
  const { colorMode } = useColorMode();
  const bgColor = {
    light: "blue.50",
    dark: "blue.900",
  };

  return (
    <Alert.Root
      mt={4}
      w="98%"
      bg={bgColor[colorMode]}
      variant="subtle"
      status="info"
    >
      <Alert.Indicator />
      <Alert.Content>
         <Box
          css={{
            "> *:first-of-type": {
              marginTop: 0,
            },
          }}
          {...props}
        />
      </Alert.Content>
    </Alert.Root>
  );
};

const DocsHeading = (props) => (
  <Heading
    css={{
      scrollMarginTop: "100px",
      "&[id]": {
        pointerEvents: "none",
      },
      "&[id]:before": {
        display: "block",
        height: " 6rem",
        marginTop: "-6rem",
        visibility: "hidden",
        content: `""`,
      },
      "&[id]:hover a": { opacity: 1 },
    }}
    {...props}
    mb="1em"
    mt="2em"
  >
    <Box pointerEvents="auto">
      {props.children}
      {props.id && (
        <Box
          aria-label="anchor"
          as="a"
          color="blue.500"
          fontWeight="normal"
          outline="none"
          _focus={{
            opacity: 1,
            boxShadow: "outline",
          }}
          opacity="0"
          ml="0.375rem"
          href={`#${props.id}`}
        >
          #
        </Box>
      )}
    </Box>
  </Heading>
);

const Hr = () => {
  const { colorMode } = useColorMode();
  const borderColor = {
    light: "gray.200",
    dark: "gray.600",
  };

  return <Separator borderColor={borderColor[colorMode]} my={4} w="100%" />;
};

const MDXComponents = {
  h1: (props) => <Heading as="h1" size="xl" my={4} {...props} />,
  h2: (props) => <DocsHeading as="h2" size="lg" fontWeight="bold" {...props} />,
  h3: (props) => <DocsHeading as="h3" size="md" fontWeight="bold" {...props} />,
  h4: (props) => <DocsHeading as="h4" size="sm" fontWeight="bold" {...props} />,
  h5: (props) => <DocsHeading as="h5" size="sm" fontWeight="bold" {...props} />,
  h6: (props) => <DocsHeading as="h6" size="xs" fontWeight="bold" {...props} />,
  inlineCode: (props) => (
    <Code colorPalette="yellow" fontSize="0.84em" {...props} />
  ),
  br: (props) => <Box height="24px" {...props} />,
  hr: Hr,
  a: CustomLink,
  p: (props) => <Text as="p" mt={0} lineHeight="tall" {...props} />,
  ul: (props) => <Box as="ul" pt={2} pl={4} ml={2} {...props} />,
  ol: (props) => <Box as="ol" pt={2} pl={4} ml={2} {...props} />,
  li: (props) => <Box as="li" pb={1} {...props} />,
  blockquote: Quote,
};

export { CustomLink };
export default MDXComponents;
