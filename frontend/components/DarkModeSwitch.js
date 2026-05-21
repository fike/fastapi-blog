import { IconButton } from "@chakra-ui/react";
import { useColorMode } from "./ui/color-mode";
import { Sun, Moon } from "lucide-react";

const DarkModeSwitch = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <IconButton
      aria-label="Toggle dark mode"
      onClick={toggleColorMode}
      variant="ghost"
    >
      {colorMode === "dark" ? <Sun size={20} /> : <Moon size={20} />}
    </IconButton>
  );
};

export default DarkModeSwitch;
