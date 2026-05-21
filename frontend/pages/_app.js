import React from 'react'
import { Provider } from '../components/ui/provider'
import { useColorMode } from '../components/ui/color-mode'
import { Global, css } from '@emotion/react'
import { prismLightTheme, prismDarkTheme } from '../styles/prism'

const GlobalStyle = ({ children }) => {
  const { colorMode } = useColorMode()

  return (
    <>
      <Global
        styles={css`
          ${colorMode === 'light' ? prismLightTheme : prismDarkTheme};
          ::selection {
            background-color: #90CDF4;
            color: #fefefe;
          }
          ::-moz-selection {
            background: #ffb7b7;
            color: #fefefe;
          }
          html {
            min-width: 356px;
            scroll-behavior: smooth;
          }
          #__next {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background: ${colorMode === 'light' ? 'white' : '#171717'};
          }
        `}
      />
      {children}
    </>
  )
}

function MyApp({ Component, pageProps }) {
  return (
    <Provider>
        <GlobalStyle>
          <Component {...pageProps} />
        </GlobalStyle>
    </Provider>
  )
}

export default MyApp
