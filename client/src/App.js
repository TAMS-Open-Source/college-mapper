import React from 'react';
import MapView from './components/MapView';
import styled, { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0px;
    font-family: 'IBM Plex Sans', sans-serif;
  }


`

function App() {
  return (
    <>
    <GlobalStyle />
    <Container>
      <MapView />
    </Container>
    </>
  );
}

// Container used to allow for all the components to be positioned relative
// to the screen
const Container = styled.div`
  position: relative;
  height: 100vh;
  width: 100vw;
`

export default App;
