import React from "react";
import { Button, Flex, Box } from "@chakra-ui/react";
import { useColorMode } from "./ui/color-mode";
import NextLink from "next/link";

import DarkModeSwitch from "../components/DarkModeSwitch";

const Container = ({ children }) => {
  const { colorMode } = useColorMode();

  const bgColor = {
    light: "white",
    dark: "#171717",
  };

  const color = {
    light: "black",
    dark: "white",
  };

  const navHoverBg = {
    light: "gray.600",
    dark: "gray.300",
  };

  return (
    <>
      <Flex
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        maxWidth="800px"
        minWidth="356px"
        width="100%"
        bg={bgColor[colorMode]}
        as="nav"
        px={[2, 6, 6]}
        py={2}
        mt={8}
        mb={[0, 0, 8]}
        mx="auto"
        position="sticky"
        zIndex={10}
        top={0}
        backdropFilter="saturate(180%) blur(20px)"
        transition="height 0.5s, line-height 0.5s"
      >
        <Box>
          <NextLink href="/">
            <Button
              variant="ghost"
              p={[1, 2, 4]}
              _hover={{ backgroundColor: navHoverBg[colorMode] }}
            >
              Home
            </Button>
          </NextLink>
          <NextLink href="/profile">
            <Button
              variant="ghost"
              p={[1, 2, 4]}
              _hover={{ backgroundColor: navHoverBg[colorMode] }}
            >
              Profile
            </Button>
          </NextLink>
          <NextLink href="/login">
            <Button
              variant="ghost"
              p={[1, 2, 4]}
              _hover={{ backgroundColor: navHoverBg[colorMode] }}
            >
              Login
            </Button>
          </NextLink>
        </Box>
        <DarkModeSwitch />
      </Flex>
      <Flex
        as="main"
        justifyContent="center"
        flexDirection="column"
        bg={bgColor[colorMode]}
        color={color[colorMode]}
        px={[0, 4, 4]}
        mt={[4, 8, 8]}
      >
        {children}
      </Flex>
    </>
  );
};

export default Container;
