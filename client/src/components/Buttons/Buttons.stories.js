import React from 'react';
import { CalendarButton as CB, PersonButton as PB } from './index.js';

export default { title: 'Buttons' };

const withBackground = (component) => (
  <div style={{
    backgroundColor: 'lightblue',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    height: 200,
    width: 200
  }}>
    {component}
  </div>
)

export const CalendarButton = () => withBackground(<CB />)

export const PersonButton = () => withBackground(<PB />)